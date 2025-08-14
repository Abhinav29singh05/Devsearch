### DevSearch Project Index

#### Overview
DevSearch is a Django web app for developer portfolios and project showcases. Users can register, manage profiles and skills, publish projects with tags, and review/vote on projects. A REST API with JWT auth exposes project data.

#### Tech Stack
- **Django 5.2.4** with **Django REST Framework** + **SimpleJWT**
- **PostgreSQL** by default (via `DATABASE_URL`), with **SQLite** fallback
- **Cloudinary** for media storage, **Whitenoise** for static files, **CORS** enabled
- Deployed-friendly (e.g., Railway). Email via SMTP (configurable)

### Project Structure
```
devsearch/
├── manage.py
├── devsearch/            # Core settings, URLs, WSGI/ASGI
├── projects/             # Projects app (models, views, forms)
├── users/                # Users app (profiles, skills, messaging)
├── api/                  # DRF endpoints and serializers
├── templates/            # Global templates
├── static/               # Static assets
├── staticfiles/          # Collected static (prod)
└── devsearchapi/         # Client demo assets
```

### URLs
- **Root router** (`devsearch/urls.py`)
  - `admin/`
  - `projects/` → `projects.urls`
  - `` (root) → `users.urls`
  - `api/` → `api.urls`
  - Password reset: `reset_password/`, `reset_password_sent/`, `reset/<uidb64>/<token>/`, `reset_password_complete`

- **Projects** (`projects/urls.py`)
  - `projects/` (list) name=`projects`
  - `projects/project/<id>/` (detail) name=`project`
  - `projects/create-project/` name=`create-project`
  - `projects/update-project/<id>/` name=`update-project`
  - `projects/delete-project/<id>/` name=`delete-project`

- **Users** (`users/urls.py`)
  - `login/`, `logout/`, `register/`
  - `` (profiles list) name=`profiles`
  - `profile/<id>/` name=`user-profile`
  - `account/`, `edit-account/`
  - `create-skill/`, `update-skill/<id>/`, `delete-skill/<id>/`
  - `inbox/`, `message/<id>/`, `send-message/<id>/`

- **API** (`api/urls.py`)
  - Auth: `api/users/token/` (POST), `api/users/token/refresh/` (POST)
  - Projects: `api/` (GET routes list), `api/projects/` (GET), `api/projects/<id>/` (GET), `api/projects/<id>/vote/` (POST, auth), `api/remove-tag/` (DELETE)

### Models
- **users.models**
  - `Profile(user, name, email, username, location, short_intro, bio, profile_image, social_*...)`
  - `Skill(owner → Profile, name, description)`
  - `Message(sender → Profile, recipient → Profile, subject, body, is_read, ...)`

- **projects.models**
  - `Project(owner → Profile, title, description, featured_image, demo_link, source_link, tags, vote_total, vote_ratio, ...)`
    - Computed helpers: `imageURL`, `getVoteCount()`
  - `Review(owner → Profile, project → Project, value ∈ {up, down}, body)` with unique `(owner, project)`
  - `Tag(name)`

### API Endpoints (DRF)
- `GET api/` → route catalog
- `GET api/projects/` → list projects
- `GET api/projects/<id>/` → retrieve project
- `POST api/projects/<id>/vote/` → vote (requires Bearer token)
- `DELETE api/remove-tag/` → remove tag from a project
- `POST api/users/token/` → obtain JWT
- `POST api/users/token/refresh/` → refresh JWT

### Settings Highlights (`devsearch/settings.py`)
- **Installed apps**: `projects`, `users`, `rest_framework`, `corsheaders`, `cloudinary_storage`, `cloudinary`
- **Middleware**: includes `corsheaders` and `whitenoise`
- **Auth**: DRF + SimpleJWT (`Bearer` tokens)
- **Database**: Postgres via `DATABASE_URL`; falls back to SQLite (`db.sqlite3`) if absent
- **Static**: `STATIC_URL = "static/"`, collected to `staticfiles/` (Whitenoise)
- **Media**: `DEFAULT_FILE_STORAGE = cloudinary_storage.storage.MediaCloudinaryStorage`
- **CORS**: `CORS_ALLOW_ALL_ORIGINS = True`
- **Email**: SMTP backend; host/port/TLS and credentials via env

### Environment Variables
Create a `.env` (see `env_template.txt`) and set at minimum:
- `SECRET_KEY`
- `DEBUG` (True/False)
- Database (choose one)
  - `DATABASE_URL` (e.g., postgres) — preferred
  - or `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
- Cloudinary
  - `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`
- Email (optional for password reset)
  - `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USE_TLS`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`
- JWT (optional overrides)
  - `JWT_ACCESS_TOKEN_LIFETIME` (days), `JWT_REFRESH_TOKEN_LIFETIME` (days)

### Local Development Quickstart
```bash
python -m venv env
env\Scripts\activate  # Windows PowerShell
pip install -r requirements.txt
copy env_template.txt .env  # then edit .env with your values
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open `http://127.0.0.1:8000/`.

### Features
- **Auth**: login/logout/register, password reset
- **Profiles**: search, paginate, edit
- **Projects**: create/update/delete, tags, voting, reviews
- **Messaging**: inbox and direct messages
- **API**: JWT-protected endpoints for projects and votes

### Notes
- Production hosts: add to `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS`
- Static files are served by Whitenoise; media is stored on Cloudinary
- CORS is open; restrict as needed for production