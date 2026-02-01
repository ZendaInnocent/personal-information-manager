# Elegant Personal Information Manager

A modern Django application to help organize personal data and information with SPA-like interactivity powered by [Datastar](https://data-star.dev).

## Features

- [x] **User Registration and Authentication**
  - Secure registration, login, and logout with Django Allauth
  - Email verification support
  - Password reset functionality

- [x] **Task and To-Do Lists with SPA Interactivity**
  - Create, edit, delete, and toggle todos without page refreshes
  - Drag-and-drop reordering of todo items
  - Real-time form validation and error messages
  - Due date management with calendar picker
  - Powered by [Datastar](https://data-star.dev) for seamless updates

- [x] **Contact Management**
  - Store and manage contacts including names, addresses, phone numbers, email addresses, and additional notes
  - International phone number support (Tanzania)

- [x] **Notes and Memo**
  - Rich text editing with TinyMCE editor
  - Organize notes in different categories or tags
  - Full HTML/Markdown support

- [ ] **Calendar and Event Management**
  - A calendar to schedule, visualize, and manage events, appointments, tasks, and reminders

- [ ] **Search and Filters**
  - Efficient search functionality and filters to quickly find specific information

- [ ] **Customizable Categories and Tags**
  - Create your own custom categories and tags for organizing data

- [ ] **Import and Export**
  - Capability to import existing data and export it in various formats

- [ ] **Reminders and Notifications**
  - Reminders and notifications sent for upcoming events and tasks

- [ ] **File Storage**
  - Safely store and manage files and attachments related to contacts, events, and tasks

## Technology Stack

- **Backend**: Django 5.2+ with Python 3.12+
- **Frontend**: Datastar with SSE (Server-Sent Events) for SPA-like interactivity
- **UI Framework**: Bootstrap 5 with Crispy Forms
- **Editor**: TinyMCE for rich text editing
- **Internationalization**: English (en) and Swahili (sw) support via Django Rosetta
- **Database**: SQLite3 (development), PostgreSQL/MySQL (production ready)
- **Testing**: pytest with pytest-django
- **Code Quality**: Ruff (linting/formatting), Django Lint (templates)

## Getting Started

### Prerequisites

- Python >= 3.12
- Django >= 5.2
- uv package manager (recommended)

### Installation

1. Clone the repository

   ```bash
   git clone https://github.com/<your-username>/personal-information-manager
   cd personal-information-manager
   ```

2. Install project dependencies and activate virtual environment

   ```bash
   uv sync
   ```

3. Create `.env` file from `.env_sample`

   ```bash
   cp .env_sample .env
   ```

4. Set required environment variables in `.env`:
   - `DJANGO_SECRET_KEY` - Generate with: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
   - `DEBUG` - Set to `True` for development, `False` for production
   - `ALLOWED_HOSTS` - Comma-separated list of allowed hosts
   - `EMAIL_HOST`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` - For email functionality

5. Install git hooks for code quality

   ```bash
   pre-commit install
   ```

6. Apply database migrations

   ```bash
   uv run manage.py migrate
   ```

7. Create superuser for admin access

   ```bash
   uv run manage.py createsuperuser
   ```

8. Run development server

   ```bash
   uv run manage.py runserver
   ```

9. Access your app in your browser at `http://localhost:8000`

   For translations: access the Rosetta interface at `http://localhost:8000/rosetta`

## Project Structure

```
personal-information-manager/
├── config/                 # Django project settings
├── pim/                    # Main application package
│   ├── accounts/            # Custom user model and authentication
│   ├── todos/               # Todo management with Datastar SPA
│   ├── contacts/            # Contact management
│   ├── notes/               # Notes with TinyMCE editor
│   ├── appointments/        # Calendar and events
│   ├── billing/             # Billing/invoice management
│   └── main/               # Home page and common views
├── static/                 # Static files (CSS, JS, images)
├── templates/              # Django templates
├── locale/                 # Translation files (en, sw)
├── docs/                  # Project documentation
├── pyproject.toml           # Python project configuration
├── .env                   # Environment variables (not in git)
├── .env_sample            # Sample environment variables
```

## Development

### Running Tests

```bash
# Run all tests with coverage
pytest

# Run specific app tests
pytest pim/todos/tests/

# Run tests without coverage
pytest --no-cov
```

### Code Quality

```bash
# Lint code
ruff check .

# Format code
ruff format .

# Format HTML templates
djlint --reformat .

# Run pre-commit hooks on all files
pre-commit run --all-files
```

### Managing Translations

```bash
# Update translation strings
uv run manage.py makemessages -a

# Compile translations
uv run manage.py compilemessages

# Access Rosetta for web-based translation management
# Visit: http://localhost:8000/rosetta
```

### Database Management

```bash
# Create migrations after model changes
uv run manage.py makemigrations

# Apply migrations
uv run manage.py migrate

# Create database schema visualization
uv run manage.py graph_models -a -o my_project_visualized.png
```

## SPA Features (Todos App)

The todos application uses [Datastar](https://data-star.dev) for SPA-like interactivity:

- **No Page Refreshes**: All CRUD operations use Server-Sent Events (SSE) for seamless updates
- **Real-time Feedback**: Toasts appear at top with click-to-dismiss
- **Loading Indicators**: Buttons show spinner and disable during operations
- **Drag-and-Drop Sort**: Full todo list reordering via Sortable.js
- **Form Validation**: Real-time error display without page reload
- **Datastar Signals**: Reactive UI state management with `$submitting`, `$formErrors`, etc.

### API Endpoints

| Endpoint             | Method     | Description         |
| -------------------- | ---------- | ------------------- |
| `/todos/`            | GET        | List all todos      |
| `/todos/create/`     | POST (SSE) | Create new todo     |
| `/todos/update/<id>` | GET/POST   | Update todo details |
| `/todos/delete/<id>` | POST (SSE) | Delete todo         |
| `/todos/toggle/<id>` | POST (SSE) | Toggle completion   |
| `/todos/sort/`       | POST (SSE) | Reorder todos       |

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow [contributing guide](CONTRIBUTING.md).

Please ensure:

1. All tests pass before submitting a PR
2. Code follows project style guidelines (see AGENTS.md)
3. Commits are descriptive and follow conventional commit format
4. Pull requests are small and focused on a single feature

## License

This project is licensed under the [MIT License](LICENSE)

## Acknowledgments

- [Django](https://www.djangoproject.com/) - Web framework
- [Datastar](https://data-star.dev) - Frontend interactivity framework
- [Bootstrap](https://getbootstrap.com/) - UI framework
- [TinyMCE](https://www.tiny.cloud/) - Rich text editor
- [Django Allauth](https://django-allauth.readthedocs.io/) - Authentication

## Changelog

### v0.2.0 (2025-02-01)

**Breaking Changes:**

- Removed HTMX dependency completely
- Migrated to Datastar for SPA-like interactivity
- Updated Python requirement to 3.12+ and Django to 5.2+

**New Features:**

- SPA behavior with no page refreshes for CRUD operations
- Drag-and-drop todo reordering with Sortable.js
- Loading indicators on different operations

**Technical Updates:**

- Enhanced all todo views with SSE event yielding
- Updated templates with Datastar signals (`data-indicator`, `data-attr`, `data-on`)
- Replaced HTMX JavaScript with Datastar patch event listeners
- Formatted all code with Ruff and DjLint

**Dependencies:**

- Added `datastar-py>=0.6.5`
- Removed `django-htmx>=1.23.2`
