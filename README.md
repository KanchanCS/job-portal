# Job Portal Project

This is a job portal project built using Django and Python, with HTML, CSS, and Bootstrap for frontend design. The project allows companies to add job listings, users to apply for jobs, and includes registration and login functionalities.

## Technical Information

- **Language:** Python, HTML, CSS
- **Framework:** Django (version 4.1.0) for backend development
- **Frontend Framework:** Bootstrap
- **Operating System:** Windows

## Prerequisites

Before running the project, make sure you have the following installed on your system:

- Python (version 3.10)
- Django (version 4.1.0)
- Other dependencies specified in the project.

## Getting Started

Follow these instructions to set up and run the project on your local machine:

1. Clone the repository:

```bash
git clone https://github.com/KanchanCS/job-portal.git
cd job-portal
```

2. Create a virtual environment (optional but recommended):

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install the project dependencies:

```bash
pip install -r requirements.txt
```

4. Set up the database:

```bash
python manage.py migrate
```

5. Create a superuser (admin) account:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Access the application:

Open your web browser and go to `http://localhost:8000/` to access the job portal.

## Project Structure

Briefly explain the directory structure of your project, highlighting key files and directories.

- `app_name/`: Contains the main Django app (you can change "app_name" to your actual app name).
- `templates/`: Contains HTML templates for the views.
- `static/`: Contains CSS, JavaScript, and other static files.
- `manage.py`: Django's command-line utility for managing the project.
- `requirements.txt`: List of project dependencies.

## Features

Explain the main features of your job portal project here, like:

- Companies can add job listings.
- Users can apply for jobs.
- User registration and login.
