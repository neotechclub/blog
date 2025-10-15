import os
import requests
import yaml

github_token = os.getenv('GH_TOKEN')
repo = 'neotechclub/blog'  # Change if needed
headers = {'Authorization': f'token {github_token}'}

def fetch_discussions():
    url = f'https://api.github.com/repos/{repo}/discussions'
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    all_discussions = resp.json()
    # Filter only Announcements category
    return [d for d in all_discussions if d.get('category', {}).get('name', '') == 'Announcements']

def convert_to_hugo_md(discussion):
    import re
    
    title = discussion['title']
    body_raw = discussion.get('body', '')
    
    # Extract existing frontmatter from the body if present
    existing_frontmatter = {}
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', body_raw, flags=re.DOTALL)
    if frontmatter_match:
        try:
            existing_frontmatter = yaml.safe_load(frontmatter_match.group(1)) or {}
        except yaml.YAMLError:
            existing_frontmatter = {}
        # Remove frontmatter from body
        body_raw = body_raw[frontmatter_match.end():]
    
    # Keep body as-is (GitHub Discussions already use markdown)
    body = body_raw.strip()
    
    # Get discussion labels as categories
    labels = discussion.get('labels', [])
    if isinstance(labels, dict):
        labels = labels.get('nodes', [])
    categories = [label['name'] for label in labels] if labels else []
    
    # Build base frontmatter dict
    frontmatter = {
        'title': title,
        'date': discussion.get('created_at', ''),
        'categories': categories
    }
    
    # Merge with existing frontmatter, letting existing values override
    frontmatter.update(existing_frontmatter)
    
    # Generate YAML frontmatter with proper escaping
    yaml_frontmatter = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    md_content = f"""---
{yaml_frontmatter.rstrip()}
---

{body}
"""
    return md_content

def slugify(text):
    """Convert title to URL-friendly slug"""
    import re
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def main():
    discussions = fetch_discussions()
    for d in discussions:
        slug = slugify(d['title'])
        post_dir = f"content/post/{slug}"
        os.makedirs(post_dir, exist_ok=True)
        fname = f"{post_dir}/index.md"
        with open(fname, 'w') as f:
            f.write(convert_to_hugo_md(d))

if __name__ == '__main__':
    main()
