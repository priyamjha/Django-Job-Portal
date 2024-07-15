# Django Job Portal Application

## Introduction
This is a Django-based job portal application that allows recruiters to post job listings and applicants to apply for jobs. The application features user authentication, job management, resume management, and a comprehensive dashboard for both applicants and recruiters.

## Technologies Used
- **Backend:** Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Other Libraries:** Django Filters, Widget Tweaks
- **Authentication:** Custom user model, Django's built-in authentication
- **Deployment:** Suitable for any Django-supported hosting service

## Features Implemented
- **User Authentication:**
  - Separate registration for recruiters and applicants
  - Login and logout functionality

- **Job Management:**
  - Recruiters can create, update, and manage job listings
  - Applicants can view job listings and apply for jobs

- **Resume Management:**
  - Applicants can upload and update their resumes
  - Recruiters can view applicants' resumes

- **Company Management:**
  - Recruiters can update their company information
  - Applicants can view company details

- **Dashboard:**
  - Customized dashboards for recruiters and applicants

## How It Was Developed
The project was developed using Django, following a modular approach by creating separate apps for users, jobs, companies, resumes, and the main website. The database models were designed to handle user roles, job listings, applications, and company details. The frontend was built using HTML and Bootstrap to ensure a responsive and user-friendly interface.

## What It Does
The job portal application allows:
- **Recruiters:** To post job openings, manage job listings, view applicants, and manage company information.
- **Applicants:** To browse and apply for jobs, manage their resumes, and view job details.

## Project Hierarchy
```
django_job_portal/
├── company/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── company/
│           ├── update_company.html
│           └── company_details.html
├── dashboard/
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── dashboard/
│           └── dashboard.html
├── job/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── job/
│           ├── create_job.html
│           ├── manage_job.html
│           ├── applied_jobs.html
│           ├── update_job.html
│           ├── all_applicants.html
│           └── job_details.html
├── resume/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── resume/
│           ├── update_resume.html
│           └── resume_details.html
├── users/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── users/
│           ├── register_applicant.html
│           ├── register_recruiter.html
│           ├── login.html
├── website/
│   ├── filters.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── website/
│           ├── home.html
│           ├── job_listing.html
│           └── job_details.html
├── django_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
└── db.sqlite3
```

## Prerequisites
- Python 3.x
- Django 5.0.6
- SQLite (or any other database supported by Django)

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/your-username/django-job-portal.git
   ```
2. Navigate to the project directory:
   ```
   cd django-job-portal
   ```
3. Create a virtual environment and activate it:
   ```
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```
4. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Apply the migrations:
   ```
   python manage.py migrate
   ```
6. Create a superuser to access the admin panel:
   ```
   python manage.py createsuperuser
   ```
7. Run the development server:
   ```
   python manage.py runserver
   ```

### Access the Application
- Open a web browser and navigate to `http://127.0.0.1:8000/` to access the application.
- Use the admin panel at `http://127.0.0.1:8000/admin/` to manage users, jobs, companies, and resumes.

### Registering and Logging In
- Register as an applicant or recruiter.
- Login using the registered email and password.
- Access the respective dashboard based on your role (applicant or recruiter).

### Managing Jobs
- Recruiters can create and manage job listings through the dashboard.
- Applicants can view and apply for available job listings.

### Managing Resumes
- Applicants can upload and update their resumes.

### Managing Companies
- Recruiters can update their company information.

## Usage
- Register as a recruiter or applicant.
- Recruiters can create and manage job postings from their dashboard.
- Applicants can upload and update their resumes and apply for jobs.
- Both recruiters and applicants can view their activities from their respective dashboards.


---

For more information, feel free to contact me at [priyamj584@gmail.com](mailto:priyamj584@gmail.com).
