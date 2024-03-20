Project Structure
=================

EmpDashboard
------------

The `EmpDashboard` project follows the standard Django project structure with additional files and folders as described below:

Project Root
~~~~~~~~~~~~

- **EmpDashboard/**
  - **settings.py**: Django project settings file.
  - **urls.py**: Django project URL configuration.
  - **wsgi.py**: WSGI application entry point.

Apps
~~~~

Users App
~~~~~~~~~

- **users/**
  - **__init__.py**: Initialization file for the `users` app.
  - **admin.py**: Django admin configuration for the `users` app.
  - **apps.py**: Django application configuration.
  - **forms.py**: Forms definition for the `users` app.
  - **models.py**: Database models definition.
  - **signals.py**: Signals handling logic for the `users` app.
  - **tests.py**: Test cases for the `users` app.
  - **urls.py**: URL configuration specific to the `users` app.
  - **views.py**: Views logic for handling HTTP requests.

Employees App
~~~~~~~~~~~~~

- **employees/**
  - **__init__.py**: Initialization file for the `employees` app.
  - **admin.py**: Django admin configuration for the `employees` app.
  - **apps.py**: Django application configuration.
  - **forms.py**: Forms definition for the `employees` app.
  - **models.py**: Database models definition.
  - **signals.py**: Signals handling logic for the `employees` app.
  - **tests.py**: Test cases for the `employees` app.
  - **urls.py**: URL configuration specific to the `employees` app.
  - **views.py**: Views logic for handling HTTP requests.

Static and Media Files
~~~~~~~~~~~~~~~~~~~~~~

- **static/**: Directory for static files such as CSS, JavaScript, and images.
- **mediafiles/**: Directory for media files uploaded by users.

Utils Module
~~~~~~~~~~~~

- **utils.py**: Utility functions and helpers for the project.

