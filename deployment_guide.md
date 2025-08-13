# DevSearch Deployment Guide

## Step 1: Set up Cloudinary Account

1. Go to [Cloudinary](https://cloudinary.com/) and sign up for a free account
2. After signing up, go to your Dashboard
3. Copy your:
   - **Cloud Name**
   - **API Key**
   - **API Secret**

## Step 2: Install Required Packages

```bash
pip install -r requirements.txt
```

## Step 3: Create Environment File

Create a `.env` file in your project root with the following content:

```env
# Django Settings
SECRET_KEY=your-new-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com

# Cloudinary Settings
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

# Email Settings (for password reset)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# JWT Settings
JWT_ACCESS_TOKEN_LIFETIME=1
JWT_REFRESH_TOKEN_LIFETIME=30
```

## Step 4: Generate New Secret Key

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Replace `your-new-secret-key-here` with the generated key.

## Step 5: Set up Email (Gmail)

1. Go to your Google Account settings
2. Enable 2-factor authentication
3. Generate an App Password
4. Use the App Password in EMAIL_HOST_PASSWORD

## Step 6: Database Migration

```bash
python manage.py makemigrations
python manage.py migrate
```

## Step 7: Create Superuser

```bash
python manage.py createsuperuser
```

## Step 8: Collect Static Files

```bash
python manage.py collectstatic
```

## Deployment Options

### Option 1: Railway (Recommended - Free)
1. Push your code to GitHub
2. Connect your GitHub repo to Railway
3. Add environment variables in Railway dashboard
4. Deploy automatically

### Option 2: Render (Free)
1. Push your code to GitHub
2. Connect your GitHub repo to Render
3. Add environment variables in Render dashboard
4. Deploy automatically

### Option 3: Heroku (Paid)
1. Install Heroku CLI
2. Create Heroku app
3. Add environment variables
4. Deploy using Git

### Option 4: DigitalOcean App Platform
1. Push your code to GitHub
2. Connect your GitHub repo to DigitalOcean
3. Add environment variables
4. Deploy automatically

## Environment Variables for Production

Make sure to set these in your deployment platform:

- `SECRET_KEY`: Your Django secret key
- `DEBUG`: False
- `ALLOWED_HOSTS`: Your domain
- `CLOUDINARY_CLOUD_NAME`: Your Cloudinary cloud name
- `CLOUDINARY_API_KEY`: Your Cloudinary API key
- `CLOUDINARY_API_SECRET`: Your Cloudinary API secret
- `EMAIL_HOST_USER`: Your email
- `EMAIL_HOST_PASSWORD`: Your email app password

## Testing Locally

1. Create `.env` file with your credentials
2. Run: `python manage.py runserver`
3. Test all functionality
4. Check if images are uploading to Cloudinary

## Security Checklist

- [ ] SECRET_KEY is changed from default
- [ ] DEBUG is set to False in production
- [ ] ALLOWED_HOSTS includes your domain
- [ ] Database credentials are secure
- [ ] Email credentials are secure
- [ ] Cloudinary credentials are secure
- [ ] .env file is in .gitignore
- [ ] Static files are collected
- [ ] HTTPS is enabled (if applicable) 