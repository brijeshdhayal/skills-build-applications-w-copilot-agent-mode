# Copilot Instructions for OctoFit Tracker

## Project Overview
OctoFit Tracker is a fitness tracking web application for Mergington High School. It enables students to log activities, earn badges, and compete in friendly team challenges. Built with Django REST backend, React frontend, and MongoDB database.

**Key Features**: User auth, activity logging, team management, competitive leaderboards, personalized suggestions

## Architecture

### Directory Structure
```
octofit-tracker/
├── backend/          # Django REST API + MongoDB
│   ├── venv/        # Python virtual environment (created via `python3 -m venv octofit-tracker/backend/venv`)
│   ├── octofit_tracker/  # Django project directory
│   └── requirements.txt   # Python dependencies (Django 4.1.7, DRF 3.14.0, Djongo 1.3.6 for MongoDB ORM)
└── frontend/        # React.js with Bootstrap + React Router
```

### Technology Stack
- **Frontend**: React.js with Bootstrap, React Router for navigation
- **Backend**: Django 4.1.7 + Django REST Framework 3.14.0
- **Database**: MongoDB (via Djongo ORM) - use Django models, never direct MongoDB scripts
- **Auth**: django-allauth with dj-rest-auth
- **CORS**: django-cors-headers for frontend-backend communication
- **Dev Environment**: GitHub Codespaces with Docker, Node.js, Python, MongoDB pre-installed

## Critical Workflows

### Port Configuration (Do Not Change)
- **8000** (public): Django REST API
- **3000** (public): React development server  
- **27017** (private): MongoDB

### Backend Setup
1. Activate venv: `source octofit-tracker/backend/venv/bin/activate`
2. Install dependencies: `pip install -r octofit-tracker/backend/requirements.txt`
3. MongoDB starts automatically on codespace start (verify with `ps aux | grep mongod`)

### Frontend Setup
- Commands must point to directory: `npm install --prefix octofit-tracker/frontend`
- Bootstrap CSS imported at top of `src/index.js`: `import 'bootstrap/dist/css/bootstrap.min.css';`
- React Router configured for multi-page navigation

### API Testing
Use `curl` to test Django REST endpoints in terminal.

## Key Developer Conventions

### Django Backend (see [.github/instructions/octofit_tracker_django_backend.instructions.md](.github/instructions/octofit_tracker_django_backend.instructions.md))
- **settings.py**: Must include Codespace URL detection:
  ```python
  ALLOWED_HOSTS = ['localhost', '127.0.0.1']
  if os.environ.get('CODESPACE_NAME'):
      ALLOWED_HOSTS.append(f"{os.environ.get('CODESPACE_NAME')}-8000.app.github.dev")
  ```
- **Serializers**: Convert MongoDB ObjectId fields to strings for JSON serialization
- **URLs**: Use environment variables to set base_url for Codespace vs local:
  ```python
  codespace_name = os.environ.get('CODESPACE_NAME')
  base_url = f"https://{codespace_name}-8000.app.github.dev" if codespace_name else "http://localhost:8000"
  ```

### React Frontend (see [.github/instructions/octofit_tracker_react_frontend.instructions.md](.github/instructions/octofit_tracker_react_frontend.instructions.md))
- Always use `--prefix octofit-tracker/frontend` flag with npm commands
- App image: [docs/octofitapp-small.png](docs/octofitapp-small.png)
- Bootstrap styling included by default

## Command Execution Rules
⚠️ **Never change directories** when agent mode runs commands. Instead, always point to the target directory:
- ✅ `npm install --prefix octofit-tracker/frontend`
- ❌ `cd octofit-tracker/frontend && npm install`

## MongoDB & Django ORM Integration
- Use Django's ORM (models, querysets) exclusively—never run direct MongoDB scripts
- Djongo bridges Django ORM with MongoDB, preserving familiar Django patterns
- Database schema defined through Django migrations and model definitions

## Development Environment
GitHub Codespaces automatically runs `post_create.sh` (MongoDB + Python venv setup) and `post_start.sh` (MongoDB startup + port visibility). Port visibility is enforced via GitHub CLI within the codespace.

## References to Instructions
- Full setup guide: [.github/instructions/octofit_tracker_setup_project.instructions.md](.github/instructions/octofit_tracker_setup_project.instructions.md)
- Django backend patterns: [.github/instructions/octofit_tracker_django_backend.instructions.md](.github/instructions/octofit_tracker_django_backend.instructions.md)
- React frontend patterns: [.github/instructions/octofit_tracker_react_frontend.instructions.md](.github/instructions/octofit_tracker_react_frontend.instructions.md)
- Project story & context: [docs/octofit_story.md](docs/octofit_story.md)
