# AGENTS.md

## Cursor Cloud specific instructions

This is a **Jekyll 3.10 + Tailwind CSS 3** static website for SLKone (a consulting firm). No database or external services are required for local development.

### Prerequisites (system-level, installed once)
- **Ruby 3.2+** with Bundler (`sudo apt-get install -y ruby-full build-essential zlib1g-dev && sudo gem install bundler`)
- **Node.js 18+** (pre-installed in cloud VMs)

### Running the dev server
1. `npm run build:css:prod` — builds Tailwind CSS to `assets/css/main.css` (must run before Jekyll serve, or use `npm run build:css` for watch mode)
2. `bundle exec jekyll serve --host 0.0.0.0 --port 4000` — starts dev server at http://localhost:4000

### Building for production
- `bundle exec jekyll build` — outputs to `_site/`

### Key gotchas
- **`vendor` must be in `_config.yml` exclude list.** When gems are installed via `bundle install` with a local path (`vendor/bundle`), Jekyll will try to process files inside vendor and fail. The `_config.yml` includes `vendor` in its exclude list to prevent this.
- **No dedicated lint/test commands exist** in this project. There are no test suites, linters, or CI checks configured. Validation is done by successfully building the site (`bundle exec jekyll build`).
- **`postcss.config.js` references `_includes/tailwind.config.js`** but the actual Tailwind config is at the project root (`tailwind.config.js`). The PostCSS config is used by the `jekyll-postcss` plugin; the `npm run build:css` script uses Tailwind CLI directly which picks up the root config. For development, use the npm scripts to build CSS rather than relying on jekyll-postcss.
- **No `.nvmrc`/`.ruby-version`/`.tool-versions`** files exist. Ruby 3.2.x and Node 18+ are known to work.
