User Guide
==========

User Registration
******************

Registration Page
------------------

.. image:: /Images/Register.png
   :width: 400
   :alt: Registration Page
   :align: center

Coding Process
--------------

The `RegisterView` function is used to authenticate the user and login to the system.

Parameters
~~~~~~~~~~

- `request` (HttpRequest): The incoming request object.
- `username` (str): The username of the user.
- `email` (str): The email of the user.
- `password` (str): The password of the user.
- `confirm_password` (str): The confirm password of the user.

Returns
~~~~~~~

- `HttpResponse`: An HTTP response object.

Redirect
~~~~~~~~

Redirect to the Login Page.

Raises
~~~~~~

- `Success_message` (str): A success message to be displayed to the user after successful registration.


User Login
**********

Login Page
----------

.. image:: /Images/Login.png
   :width: 400
   :alt: Login Page

Coding Process
--------------

The `LoginView` function is used to authenticate the user and login to the system.

Parameters
~~~~~~~~~~

- `request` (HttpRequest): The incoming request object.
- `email` (str): The email of the user.
- `password` (str): The password of the user.

Returns
~~~~~~~

- `HttpResponse`: An HTTP response object.

Raises
~~~~~~

- `error_message` (str): An error message to be displayed to the user.


Update User Profile
********************

Profile Update Page
--------------------

.. image:: /Images/emp_update.png
   :width: 400
   :alt: Profile Update Page

Coding Process
--------------

The `EmployeeUpdateView` class is used for updating employee details.

Attributes
~~~~~~~~~~

- `model`: The model class for which the view updates instances.
- `template_name`: The name of the template to be used for rendering the view.
- `fields`: The fields of the model to be included in the form.
- `success_url`: The URL to redirect to after a successful update.

Methods
~~~~~~~

- `test_func`: Checks if the current user has permission to update the employee details.

Profile Detail
**************

Profile Detail Page
--------------------

.. image:: /Images/emp_profile.png
   :width: 400
   :alt: Profile Detail Page

Coding Process
--------------

The `EmployeeDetailView` class is used for displaying employee details.

Attributes
~~~~~~~~~~

- `model`: The model class for which the view displays instances.
- `template_name`: The name of the template to be used for rendering the view.

Methods
~~~~~~~

- `test_func`: Checks if the current user has permission to view the employee details.

Update In-Time Attendance
*************************

Attendance Page
---------------

.. image:: /Images/attendance.png
   :width: 400
   :alt: Attendance Page

Coding Process
--------------

The `IntimeAttendanceReportView` function is used for registering the in-time attendance of an employee.

Parameters
~~~~~~~~~~

- `request`: The HTTP request object.

Returns
~~~~~~~

- If the request method is POST and the attendance is successfully registered, renders the attendance report page.
- If the request method is GET, renders the in-time attendance form page.

Update Out-Time Attendance
**************************

Attendance Page
---------------

.. image:: /Images/attendance.png
   :width: 400
   :alt: Attendance Page

Coding Process
--------------

The `OutTimeAttendanceReportView` function is used for registering the out-time attendance of an employee.

Parameters
~~~~~~~~~~

- `request`: The HTTP request object.
- `pk`: The primary key of the EmployeeAttendance object.

Returns
~~~~~~~

- If the request method is POST and the out-time attendance is successfully registered, renders the leave time report page.
- If the request method is GET, renders the out-time attendance form page.

Change Password
***************

Change Password Page
---------------------

.. image:: /Images/change_password.png
   :width: 400
   :alt: Change Password Page

Coding Process
--------------

The `ChangePasswordView` function is used for changing the password of the logged-in user.

Parameters
~~~~~~~~~~

- `request`: The HTTP request object.

Returns
~~~~~~~

- If the request method is POST and the password change is successful, redirects to the login page.
- If the request method is GET, renders the change password form page.

Resetting Forgotten Password
*****************************

Steps Involved
--------------

1. Fill the Email Address
2. Email Notification
3. Set New Password
4. Success Message

Fill the Email Address
-----------------------

Email Address Filling Page
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /Images/email_input_forgot_password.png
   :width: 400
   :alt: Email Address Filling Page

Coding Process
--------------

The `PasswordResetView` function is used for initiating the password reset process.

Parameters
~~~~~~~~~~

- `request`: The HTTP request object.

Returns
~~~~~~~

- If the request method is POST and the email is registered, sends a password reset email and redirects to the password reset confirmation page.
- If the request method is GET, renders the password reset form page.

Email Notification
~~~~~~~~~~~~~~~~~~

Email Notification Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~

An email will be sent to the provided email address containing a unique link to reset the password.

Set New Password
----------------

Set New Password Page
~~~~~~~~~~~~~~~~~~~~~

.. image:: /Images/forgot_pass_reset.png
   :width: 400
   :alt: Set New Password Page

Coding Process
--------------

The `PasswordResetDoneView` function is used for completing the password reset process.

Parameters
~~~~~~~~~~

- `request`: The HTTP request object.
- `uid`: The user ID encoded in base64.
- `token`: The password reset token.

Returns
~~~~~~~

- If the request method is POST and the password reset is successful, renders the password reset confirmation page.
- If the request method is GET, renders the password reset completion form page.
