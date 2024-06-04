
# Role Based Task Management Website

This Django application implements a robust role-based authentication system with distinct dashboards for Admin, Manager, and Employee roles. Each role has specific functionalities and access levels to ensure an organized and efficient workflow within an organization. The application is designed to streamline user management, task assignment, and notifications, enhancing productivity and communication within teams.



## Getting Started

To get started with the Role Based Task Management Website, follow these steps:

- Clone the repository to your local machine.
```bash
  git clone https://github.com/moumitabanik/role_based_task_management.git

```
- Navigate to the Project Directory: Change into the project directory.
```bash
cd role_based_task_management
```
- Create a Virtual Environment: Create a new virtual environment for the project.
``` bash
python -m venv venv
```
- Activate the Virtual Environment: Activate the virtual environment.
On macOS/Linux:
``` bash
source venv/bin/activate
```
On Windows:
```bash
venv\Scripts\activate
```
- Dependencies: Install the required dependencies using pip.
```bash
pip install -r requirements.txt
```
- Database Configuration: Create a MySQL database for the application. Update the database configuration in the settings.py file
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
- Replace 'your_database_name', 'your_database_user', and 'your_database_password' with your actual database information.

- Database Configuration: Create a MySQL database for the application. Update the database configuration in the settings.py file
```bash
python manage.py migrate
```
- Run the Development Server: Start the Django development server.
```bash
python manage.py runserver
```
- Access the Application: Open your web browser and navigate to http://localhost:8000 to access the Health Symptom Recommendation System.
## Tech Stack

**Frontend:** HTML5, CSS3, Vanila JS, TailwindCss, FlowBite, DataTable

**Backend:** Python, Django, REST APIs, MySQL


## Screenshots

[Login Page](https://drive.google.com/file/d/1WD6BwDKBur2bi4QqXzycPhdjbX2VGExd/view?usp=drive_link)

[Admin/Manager Dashboard Page 1](https://drive.google.com/file/d/1nbWmgyWGVBEcQWwkr1n_WtfHYX2LIGpN/view?usp=drive_link)

[Admin/Manager Dashboard Page 2](https://drive.google.com/file/d/1cVL_4TZzq11Cet9T_N7S0LGyGrGYci8d/view?usp=drive_link)

[Users Page](https://drive.google.com/file/d/1EE9cGiLAxe6pNnMRkOMDUnDWTo-ul7YD/view?usp=drive_link)

[Add User Page](https://drive.google.com/file/d/1KtoKbCtFyw3OZ9m7ztwKgHnjxGpPkTcs/view?usp=drive_link)

[Project Statistics](https://drive.google.com/file/d/1xVUCUp_O3LZ0OL1JkrYbu4hN-o8P7i83/view?usp=drive_link)

[Manage Tasks](https://drive.google.com/file/d/18ENskGK9uHzeFxr1tk7PzztKfSNuxUU3/view?usp=drive_link)

[Add Tasks](https://drive.google.com/file/d/1cbH1dWywVx4VWOnS4TkCV8Mv_gOBpZpH/view?usp=drive_link)

[Manage Projects](https://drive.google.com/file/d/1MNEJG1zZutvvLwIJxzKRagP2VHpWv1jh/view?usp=drive_link)

[Add Projects](https://drive.google.com/file/d/1DS_O4-LK1wRd7YfQ7-Vb1ZpSvTsw9-tt/view?usp=drive_link)

[Notification Page](https://drive.google.com/file/d/1t7E_NJejs0YCE93bf-oi-5KWujRL4Zdu/view?usp=drive_link)

[Log out Button](https://drive.google.com/file/d/1TW2F9HW5Q-7BMsffNLaiTPuLIfvat3L4/view?usp=drive_link)

## Demo

Here is the [Demo](https://drive.google.com/file/d/123XQ9qLy3qLLTGWnAb33-hKRImIReeup/view?usp=drive_link) of the project 


## Appendix

- [Django Documentation](https://docs.djangoproject.com/en/5.0/): Official documentation for the Django web framework.
- [REST Framework Documentation](https://www.django-rest-framework.org/): Documentation for Django REST Framework, which is used for building APIs in Django.
- [Flowbite Documentation](https://flowbite.com/): Documentation for Flowbite, which is used to design the html components
- [TailwindCss Documentation](https://tailwindcss.com/docs/installation): Documentation for TailwindCss, which is used to design the html pages
## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/moumita-banik/)

