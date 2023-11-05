# Elegant Personal Information Manager

An application to help organize personal data and information.

## Features

- [x] **User Registration and Authentication**

  Register, login and logout securily.

- [x] **Task and To-Do Lists**

  Create and manage to-do lists and tasks with due dates and priority level.

- [x] **Contact Management**

  Store and manage contacts including names, addresses, phone numbers, email addresses, and additional notes.

- [x] **Notes and Memo**

  Capture and organize notes, ideas, and memos in different categories or tags.

- [ ] **Calendar and Event Management**

  A calendar to schedule, visualize and manage events, appointments, tasks and reminders.

- [ ] **Search and Filters**

  Efficient search functionality and filters to quickly find specific information.

- [ ] **Customizable Categories and Tags**

  Create your own custom categories and tags for organizing data.

- [ ] **Import and Export**

  Capability to import existing data and export it in various formats.

- [ ] **Reminders and Notifications**

  Reminders and notifications sent for upcoming events and tasks.

- [ ] **File Storage**

  Safely store and manage files and attachments related to contacts, events and tasks.

## Getting Started

### Prerequisites

- Python >=3.10
- Django >=4.2
- Virtual Environment (optional but recommended)

### Installation

1. Fork the repository

2. Clone the forked repository

   ```bash
   git clone https://github.com/<your-username>/personal-information-manager
   ```

3. Create and activate virtual environment

   ```bash
   py -m venv .venv

   source .venv/bin/activate
   .venv/scripts/activate  # windows
   ```

4. Install Project Dependencies

   ```bash
   pip install pipenv # this project use pipenv to manage packages
   pipenv install --dev
   ```

   Rename '.env_sample' to '.env', the fill the value accordingly.

   Install the git hook script for pre-commit

   ```bash
   pre-commit install
   ```

5. Apply database migrations

   ```bash
   py manage.py migrate
   ```

6. Create superuser for admin access

   ```bash
   py manage.py createsuperuser
   ```

7. Run the development server

   ```bash
   py manage.py runserver
   ```

8. Access your app in your browser at `http://localhost:8000`

For Translations: access the interface at `http://localhost:8000/rosetta`

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow [contributing guide](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE)
