### Setup Instructions

1. Ensure your repository has a valid `GH_TOKEN` secret (usually set automatically for GitHub Actions).
2. Adjust the repository name in the Python script if needed.
3. Enable Giscus in your Hugo config (`config/_default/params.toml`) and set the correct repo/category IDs.
4. Discussions will appear in `content/` and be rendered by Hugo.

#### Giscus Compatibility
Each markdown file includes a `giscus_discussion_id` in its frontmatter, allowing Giscus to link comments to the original discussion.

---

# Hugo Theme Stack Starter Template

This is a quick start template for [Hugo theme Stack](https://github.com/CaiJimmy/hugo-theme-stack). It uses [Hugo modules](https://gohugo.io/hugo-modules/) feature to load the theme.

It comes with a basic theme structure and configuration. GitHub action has been set up to deploy the theme to a public GitHub page automatically. Also, there's a cron job to update the theme automatically everyday.

## Get started

1. Click *Use this template*, and create your repository as `<username>.github.io` on GitHub.
![Step 1](https://user-images.githubusercontent.com/5889006/156916624-20b2a784-f3a9-4718-aa5f-ce2a436b241f.png)

2. Once the repository is created, create a GitHub codespace associated with it.
![Create codespace](https://user-images.githubusercontent.com/5889006/156916672-43b7b6e9-4ffb-4704-b4ba-d5ca40ffcae7.png)

3. And voila! You're ready to go. The codespace has been configured with the latest version of Hugo extended, just run `hugo server` in the terminal and see your new site in action.

4. Check `config` folder for the configuration files. You can edit them to suit your needs. Make sure to update the `baseurl` property in `config/_default/config.toml` to your site's URL.

5. Open Settings -> Pages. Under "Build and deployment", set Source to "GitHub Actions".

6. Once you're done editing the site, just commit it and push it. GitHub Actions will build and deploy the site automatically using artifacts.

---

In case you don't want to use GitHub codespace, you can also run this template in your local machine. **You need to install Git, Go and Hugo extended locally.**

## Update theme manually

Run:

```bash
hugo mod get -u github.com/CaiJimmy/hugo-theme-stack/v3
hugo mod tidy
```

> This starter template has been configured with `v3` version of theme. Due to the limitation of Go module, once the `v4` or up version of theme is released, you need to update the theme manually. (Modifying `config/module.toml` file)

## Deploy to another static page hostings

If you want to build this site using another static page hosting, you need to make sure they have Go installed in the machine. 

<details>
  <summary>Vercel</summary>
  
You need to overwrite build command to install manually Go:

```
amazon-linux-extras install golang1.11 && hugo --gc --minify
```

![](https://user-images.githubusercontent.com/5889006/156917172-01e4d418-3469-4ffb-97e4-a905d28b8424.png)

If you are using Node.js 20, you need to overwrite the install command to install manually Go:

```
dnf install -y golang
```

![image](https://github.com/zhi-yi-huang/hugo-theme-stack-starter/assets/83860323/777c1109-dfc8-4893-9db7-1305ec027cf5)


Make sure also to specify Hugo version in the environment variable `HUGO_VERSION` (Use the latest version of Hugo extended):

![Environment variable](https://user-images.githubusercontent.com/5889006/156917212-afb7c70d-ab85-480f-8288-b15781a462c0.png)
</details>

---

## Orchestrating GitHub Discussions to Hugo Markdown

This project includes an automated system to fetch GitHub Discussions and convert them into markdown files compatible with the Hugo Stack theme, including Giscus comment support.

### How it works

1. **GitHub Actions Workflow**: The deployment workflow `.github/workflows/deploy.yml` is triggered on push, pull requests, or when discussions in the "Announcements" category are created/edited.
2. **Conversion Script**: The Python script at `.github/scripts/discussions_to_markdown.py` converts each discussion to a Hugo page bundle in `content/post/[slug]/index.md`, preserving discussion tags and category. Giscus compatibility is maintained via title-based mapping.
3. **Artifacts Deployment**: The workflow builds the site, uploads it as a GitHub Pages artifact, and deploys it using the modern GitHub Pages deployment action. No commits to master or gh-pages branches needed.

### Setup Instructions

1. Configure GitHub Pages in your repository settings to use \"GitHub Actions\" as the source.
2. Ensure Giscus is enabled in `config/_default/params.toml` with `provider = "giscus"` and correct repo/category IDs.
3. Only discussions in the \"Announcements\" category will be converted to blog posts.
4. Each discussion becomes a post at `content/post/[slugified-title]/index.md` during the build.
5. Giscus automatically links posts to discussions via title matching.


#### Giscus Compatibility

Giscus uses title-based mapping (`mapping = "title"`) to automatically link blog posts to their corresponding GitHub Discussions. When a discussion in the \"Announcements\" category is created, it's converted to a post with the same title, and Giscus handles the linking automatically - no manual IDs needed.

---

## Improved Dark Mode

The dark mode color palette has been updated for a more elegant and accessible experience. Custom colors are defined in `assets/scss/custom.scss` and override the default theme colors for backgrounds, surfaces, text, links, and accents.

To further customize, edit the CSS variables in `custom.scss` under the `:root[data-theme="dark"]` selector.

---
