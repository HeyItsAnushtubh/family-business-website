# 🥭 Kale Mango Farms

Official website for **Kale Mango Farms** — a Devgad Alphonso mango farm. Customers can browse the farm, check prices, place orders, and leave reviews. Orders and reviews are stored in a database and viewable through the Django admin panel.

---

## Pages

| Page | URL | Description |
|------|-----|-------------|
| Home | `/` | Welcome page with farm overview cards |
| Mango Prices | `/mango_prices` | Pricing tiers (single, dozen, full box) |
| Order Mangoes | `/contact` | Order form — saves to database |
| Leave a Review | `/review` | Review form — saves to database |
| Admin Panel | `/admin/` | View and manage all orders and reviews |

---

## Tech Stack

- **Backend:** Python 3.12, Django 6
- **Database:** SQLite (development)
- **Frontend:** Bootstrap 5.3, custom CSS
- **Server:** Django dev server (development), Gunicorn (production)

---

## Setup

### 1. Install dependencies

```bash
pip install django gunicorn
```

### 2. Apply database migrations

```bash
python3 manage.py migrate
```

### 3. Create an admin account

```bash
python3 manage.py createsuperuser
```

### 4. Run the development server

```bash
python3 manage.py runserver 0.0.0.0:5000
```

Visit `http://localhost:5000` in your browser.

---

## Project Structure

```
kmf/                  # Django project settings & URLs
home/                 # Main app (models, views, URLs)
  models.py           # Contact (orders) and Review models
  views.py            # Page view logic
  urls.py             # App URL routing
  migrations/         # Database migration history
templates/            # HTML templates for all pages
static/               # Static images (mango.jpg, prices.jpg, kat.jpg)
manage.py             # Django management utility
```

---

## Admin Panel

Access the admin panel at `/admin/` to view all submitted orders and reviews.

---

## Notes

- `db.sqlite3` is excluded from version control via `.gitignore` — do not commit it
- The site is configured for Replit's proxied environment (`ALLOWED_HOSTS = ['*']`, `CSRF_TRUSTED_ORIGINS` set for `*.replit.dev` / `*.repl.co` / `*.replit.app`)
