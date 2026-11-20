# FORMA — Design your everyday

**A polished, interactive e-commerce portfolio website.** FORMA is a fictional design-and-lifestyle brand, featuring 20 original product illustrations, a responsive storefront, functional shopping flows, and a demo admin dashboard.

> **Important:** This is an advanced **front-end demo**, not a production e-commerce service. It uses browser `localStorage` as the demo database and does **not** provide real user authentication, payment processing, order fulfilment, or server-side security. Never enter sensitive personal or payment information.

![FORMA portfolio cover](portfolio-cover.png)

## Features

| Customer experience | Store management |
|---|---|
| Modern mobile-first home page | Interactive admin dashboard |
| 20 illustrated demo products | Revenue and collection visualizations (sample data) |
| Category/price/sale filters and sorting | View sample and locally placed orders |
| Fast keyboard-accessible product search (`Ctrl/⌘ + K`) | Update local order status |
| Product details with color variants, stock and specs | Add, edit, and hide products |
| Quick-view modals and image gallery | Track local newsletter opt-ins |
| Persistent shopping cart and quantity controls | Sample admin sign-in |
| Wishlist and compare up to 3 products | Mobile-friendly admin interface |
| Promo code `FORM10` and free-shipping progress | |
| Validated **demo** checkout and order confirmation | |
| Browser-local order history | |
| Static-hosting friendly; optional offline PWA caching | |

## Tech stack

- **HTML5**, modern **CSS3** (CSS Grid, Flexbox, fluid typography, transitions)
- **Vanilla JavaScript ES2020+** (state management, dynamic templating, hash-based routes, event delegation)
- **localStorage/sessionStorage** (demo persistence)
- **Custom SVG** product artwork—fully bundled; no stock-photo dependency
- **Progressive Web App** manifest and service worker (installed on HTTPS hosting)
- **Node.js built-in modules** for dependency-free smoke tests (optional)

**No package installation, API keys, database setup, external JavaScript framework, or build step required.** Google Fonts are loaded if the visitor is online, with local font fallbacks.

## Run locally

**Option 1 — simplest:** Download/extract the ZIP and double-click `index.html`. The site works as a static website. Some browsers limit storage for `file://` URLs; use the local-server option for consistent storage behavior.

**Option 2 — recommended (Windows / macOS / Linux):** With Python installed, open a terminal in the extracted `forma-ecommerce` folder and run:

```bash
python -m http.server 8000
```

If your Windows installation uses the Python launcher, run `py -m http.server 8000` instead. Open **http://localhost:8000**.

**Run tests (optional):**

```bash
node tests/smoke.test.js
```

This uses Node's standard library; there is no `npm install` step.

## Try these interactions

1. Browse products and change category/price filters on the Shop page.
2. Press **Ctrl + K** (or **⌘ + K** on Mac) and search for “lamp”.
3. Save items to your wishlist or compare up to 3 items.
4. Add products to your bag. Use coupon **`FORM10`** on the demo checkout page.
5. Fill in the sample checkout fields and place a **demo-only** order. No money is charged.
6. View the saved order under **My account**.
7. Open **Admin demo** in the footer, then try the inventory editor and order-status dropdowns.

### Admin demo credentials

```text
Email:    admin@forma.demo
Password: demo1234
```

The password is **intentionally included in the source** because this is a local UI simulation. It is not secure authentication and must not be used for a real store.

## Publish on GitHub Pages (free)

1. Create a new public repository named `forma-ecommerce` on GitHub.
2. Upload the **contents** of this folder, including `index.html`, `styles.css`, `app.js` and `assets/`.
3. Under **Settings → Pages**, choose **Deploy from a branch**, select `main`, then `/(root)` and save.
4. Your site will be published at a URL similar to `https://YOUR_USERNAME.github.io/forma-ecommerce/`.

All navigation uses `#/...` routes and relative asset paths, so GitHub Pages can serve them without a router configuration.

Or push from a terminal after creating your empty repository:

```bash
git init
git add .
git commit -m "Build FORMA e-commerce portfolio demo"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/forma-ecommerce.git
git push -u origin main
```

Then enable Pages as described above. Replace `YOUR_USERNAME` with your actual GitHub username.

## Folder structure

```text
forma-ecommerce/
├── index.html               # Entry point
├── styles.css               # Responsive design system
├── app.js                   # Product data, routes, shopping and admin logic
├── assets/                  # Original SVG product art and favicon
├── create_assets.py         # Regenerate product illustrations (optional)
├── tests/smoke.test.js      # Dependency-free functional smoke tests
├── portfolio-cover.png      # Repository / portfolio artwork
├── manifest.json            # PWA metadata
├── service-worker.js        # Offline asset caching (on HTTPS)
├── LICENSE                  # MIT license
└── README.md
```

## Architecture notes

- **State:** central `state` object with persistent shopping data. All rendering happens in reusable functions.
- **Navigation:** client-side hash routing keeps links working on static hosting.
- **Filtering:** products are filtered by price, category, sale status, and keyword, then sorted/paginated.
- **Checkout:** validates basic input, calculates discount/shipping, stores a demo receipt and clears the bag.
- **Admin:** illustrates storefront management, but credentials/session are browser-local, not real authorization.
- **Illustrations:** original SVG source graphics are shipped in `assets/`. Run `python create_assets.py` to regenerate them.
- **Accessibility:** semantic controls, labels, descriptive alt text, keyboard search, modal semantics, and reduced-motion support. A production app should add focus trapping and full accessibility testing.

## Limitations / what to build next

FORMA is designed for a **public portfolio demonstration**, not commercial deployment. All sales, inventory, reviews, testimonials, and analytics shown are illustrative. Local changes aren't synchronized across devices, and no payments are processed. To make it production-ready, add a real API, database, authenticated roles, transactional stock updates, payment integration, tax/shipping logic, server-side validation, CSRF protection, rate limiting, secure cookies, and automated end-to-end tests.

Good next milestones for an even stronger software engineering portfolio: a React/TypeScript version, Node/NestJS or Django API, PostgreSQL, Stripe test-mode checkout, cloud deployment, CI/CD, and observability.

## Suggested portfolio description

**FORMA — Advanced E-Commerce Storefront & Admin Dashboard**  
Designed and developed a responsive multi-page e-commerce web application featuring interactive product discovery, advanced filtering, persistent cart/wishlist, product comparison, demo checkout, order history, inventory management, and an analytics-inspired admin dashboard. Implemented with semantic HTML, modern CSS, modular UI functions, vanilla JavaScript, local state persistence, and custom SVG artwork; deployable as a zero-dependency static site.

## License

MIT License. Illustrations and code in this project were created for this demo.
