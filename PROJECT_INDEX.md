# DevSearch Project Index

## Project Overview
DevSearch is a Django-based web application that serves as a developer portfolio and project showcase platform. It allows developers to create profiles, showcase their projects, and receive reviews/votes from other users.

## Project Structure

### Root Directory
```
devsearch/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database file
├── desktop.ini              # Windows system file
├── env/                     # Virtual environment directory
├── devsearch/               # Main Django project settings
├── projects/                # Projects app
├── users/                   # Users app
├── api/                     # API app
├── templates/               # Global templates
├── static/                  # Static files (CSS, JS, images)
├── staticfiles/             # Collected static files
└── devsearchapi/            # API-related directory
```

## Core Django Configuration

### `manage.py`
- Django's command-line utility for administrative tasks
- Entry point for Django management commands

### `devsearch/` - Main Project Settings
- **`settings.py`** (221 lines): Main Django configuration
  - Database settings (SQLite)
  - Installed apps: projects, users, rest_framework, corsheaders
  - JWT authentication configuration
  - Static and media file settings
  - CORS middleware configuration
- **`urls.py`** (44 lines): Main URL routing
  - Admin interface: `/admin/`
  - Projects: `/projects/`
  - Users: `/` (root)
  - API: `/api/`
  - Password reset functionality
- **`wsgi.py`** (17 lines): WSGI application entry point
- **`asgi.py`** (17 lines): ASGI application entry point

## Applications

### 1. Projects App (`projects/`)

#### Models (`models.py` - 85 lines)
- **Project**: Main project model with fields:
  - owner (ForeignKey to Profile)
  - title, description, featured_image
  - demo_link, source_link
  - tags (ManyToManyField to Tag)
  - vote_total, vote_ratio
  - created timestamp, UUID primary key
  - Methods: reviewers, imageURL, getVoteCount

- **Review**: Project review/voting system
  - owner, project, body, value (up/down vote)
  - created timestamp, UUID primary key
  - Unique constraint: one review per user per project

- **Tag**: Project categorization
  - name, created timestamp, UUID primary key

#### Views (`views.py` - 112 lines)
- `projects()`: Display all projects with search and pagination
- `project(pk)`: Single project view with review form
- `createProject()`: Create new project (login required)
- `updateProject(pk)`: Update existing project (login required)

#### Forms (`forms.py` - 40 lines)
- `ProjectForm`: Form for creating/editing projects
- `ReviewForm`: Form for submitting project reviews

#### URLs (`urls.py` - 12 lines)
- Project listing and detail views
- Project creation and editing

#### Templates (`templates/projects/`)
- `projects.html`: Project listing page
- `single-project.html`: Individual project view
- `project_form.html`: Project creation/editing form

#### Utilities (`utils.py` - 47 lines)
- `searchProjects()`: Search functionality
- `paginateProjects()`: Pagination helper

### 2. Users App (`users/`)

#### Models (`models.py` - 63 lines)
- **Profile**: Extended user profile
  - user (OneToOneField to User)
  - name, email, username, location
  - short_intro, bio
  - profile_image
  - Social media links (GitHub, Twitter, LinkedIn, Website)
  - created timestamp, UUID primary key
  - Methods: imageURL

- **Skill**: User skills
  - owner (ForeignKey to Profile)
  - name, description
  - created timestamp, UUID primary key

- **Message**: User messaging system
  - sender, recipient (ForeignKey to Profile)
  - name, email, subject, body
  - is_read flag, created timestamp, UUID primary key

#### Views (`views.py` - 205 lines)
- `loginUser()`: User authentication
- `logoutUser()`: User logout
- `registerUser()`: User registration
- `profiles()`: Display all user profiles
- `userProfile(pk)`: Individual user profile
- `userAccount()`: User's own account (login required)
- `editAccount()`: Edit profile (login required)
- `createSkill()`: Add skills (login required)
- `updateSkill()`: Edit skills (login required)
- `deleteSkill()`: Delete skills (login required)
- `inbox()`: Message inbox (login required)
- `viewMessage()`: View individual message (login required)
- `createMessage()`: Send message (login required)

#### Forms (`forms.py` - 69 lines)
- `CustomUserCreationForm`: User registration form
- `ProfileForm`: Profile editing form
- `SkillForm`: Skill creation/editing form
- `MessageForm`: Message sending form

#### URLs (`urls.py` - 25 lines)
- Authentication routes (login, logout, register)
- Profile routes (profiles, user-profile, account)
- Skill management routes
- Messaging routes

#### Templates (`templates/users/`)
- `login_register.html`: Login and registration forms
- `profiles.html`: User profiles listing
- `user-profile.html`: Individual user profile
- `account.html`: User's own account
- `profile_form.html`: Profile editing form
- `skill_form.html`: Skill creation/editing form
- `message_form.html`: Message sending form
- `inbox.html`: Message inbox
- `message.html`: Individual message view

#### Utilities (`utils.py` - 44 lines)
- `searchProfiles()`: Profile search functionality
- `paginateProfiles()`: Profile pagination helper

#### Signals (`signals.py` - 51 lines)
- Automatic profile creation when user is created
- Profile update when user is updated

### 3. API App (`api/`)

#### Views (`views.py` - 72 lines)
- `getRoutes()`: API endpoint documentation
- `getProjects()`: Get all projects
- `getProject(pk)`: Get single project
- `projectVote(pk)`: Vote on project (authenticated)
- `removeTag()`: Remove tag from project

#### Serializers (`serializer.py` - 44 lines)
- `ProjectSerializer`: Project model serialization

#### URLs (`urls.py` - 21 lines)
- API endpoints for projects and voting

## Templates

### Global Templates (`templates/`)
- `index.html`: Homepage (277 lines)
- `main.html`: Base template (44 lines)
- `navbar.html`: Navigation component (30 lines)
- `login.html`: Login page (68 lines)
- `signup.html`: Registration page (90 lines)
- `profile.html`: Profile page (242 lines)
- `form-template.html`: Form template (43 lines)
- `pagination.html`: Pagination component (24 lines)
- `delete_template.html`: Delete confirmation (22 lines)
- Password reset templates:
  - `reset_password.html` (49 lines)
  - `reset_password_sent.html` (19 lines)
  - `reset.html` (49 lines)
  - `reset_password_complete.html` (44 lines)

## Static Files

### Styles (`static/styles/`)
- `app.css`: Main application styles (848 lines)
- `main.css`: Additional styles (5 lines)

### JavaScript (`static/js/`)
- `main.js`: Main JavaScript functionality (42 lines)

### Images (`static/images/`)
- Profile and project images storage

### UI Kit (`static/uikit/`)
- UI framework assets

## Database Schema

### Key Relationships
- User → Profile (OneToOne)
- Profile → Project (OneToMany)
- Profile → Skill (OneToMany)
- Profile → Message (OneToMany as sender/recipient)
- Project → Tag (ManyToMany)
- Project → Review (OneToMany)

### Models Summary
- **User**: Django's built-in User model
- **Profile**: Extended user information
- **Project**: Developer projects with voting system
- **Review**: Project reviews/votes
- **Tag**: Project categorization
- **Skill**: User skills
- **Message**: User messaging system

## Features

### Core Functionality
1. **User Authentication**: Login, logout, registration
2. **Profile Management**: Create, edit, view profiles
3. **Project Showcase**: Create, edit, view projects
4. **Voting System**: Up/down vote projects
5. **Search**: Search projects and profiles
6. **Messaging**: Send messages between users
7. **Skills Management**: Add, edit, delete skills
8. **API**: RESTful API for projects and voting

### Technical Features
- JWT Authentication for API
- Image upload and handling
- Pagination
- Search functionality
- Responsive design
- Password reset functionality
- CORS support

## Development Setup
- Django 5.2.4
- SQLite database
- REST Framework
- JWT Authentication
- CORS Headers
- Virtual environment support

## File Count Summary
- Python files: ~20
- Template files: ~15
- Static files: ~5
- Configuration files: ~5
- Total files: ~45

This project serves as a comprehensive developer portfolio platform with social features, project showcasing, and a REST API for external integrations. 