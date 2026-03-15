This directory contains the public-ready static files for the "地域循環コミュニティアプリ" homepage variant.

Files used for publishing:
- `index.html`
- `style.css`
- `script.js`
- `assets/`

Deploy options:
- `Vercel`: set the project root to `variants/chiiki-junkan-community-app`
- `GitHub Pages`: the workflow at `.github/workflows/deploy-community-variant.yml` deploys this directory

Notes:
- `.nojekyll` is included for GitHub Pages
- all asset paths are relative, so the directory can be served as a plain static site
