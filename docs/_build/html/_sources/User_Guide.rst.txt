**User Guide**
==============

**User Registration**
**********************

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

ERROR:
~~~~~~~~~
   - 1: Error 204 No content
   - 2: Mismatch password
   - 3: Error 403 Already Exists
   - 4: Form validation Error
   - 5: Csrf verification failed

ERROR HANDLING:
~~~~~~~~~~~~~~~~~~~~~
   - 1: Fill in all the required fields
   - 2: Make sure to match both password fields 
   - 3: Change the username and email if already exists or try to login
   - 4: Make sure to put a proper email format and password should contain Capital Letter, Small Letter, Special characters, Numeric value and minimum length of the password should be greater than 8
   - 5: Reload the page or try in another browser


**User Login**
**************

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

ERROR:
~~~~~~~~~~~~
     - 1: Error 204 No Content
     - 2: Invalid email or Password
     - 3: Authentication Failure
     - 4: Session management error


ERROR HANDLING:
~~~~~~~~~~~~~~~~~~~~~
   - 1: Make sure to provide valid email and password
   - 2: Message will appear as Invalid email and password please recheck and try again
   - 3: Try again later or contact for support for issue
   - 4: Try to Login again to establish new connection


**Update User Profile**
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

ERROR:
~~~~~~~~~~~~
     - 1: Error 401 Unauthorized Access
     - 2: Error 404 Not found
     - 3: Error 403 Forbidden
     - 4: Form validation error


ERROR HANDLING:
~~~~~~~~~~~~~~~~
   - 1: Make sure to Authenticate (Login) before accessing the page.
   - 2: Make sure to register as an Employee
   - 3: Accessed data must be of logged in user
   - 4: Provide proper data type in the field


**Profile Detail**
******************

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


ERROR:
~~~~~~~~~~~~
     - 1: Error 401 Unauthorized Access
     - 2: Error 404 Not Found
     - 3: Error 403 Permission Denied


ERROR HANDLING:
~~~~~~~~~~~~~~~~
   - 1: Make sure to authenticate before accessing the page
   - 2: Must be registered as an Employee
   - 3: Accessing data must be of logged in user cannot view other Employee records

**Update In-Time Attendance**
*****************************

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


ERROR:
~~~~~~~~~~~~
     - 1: Error 403 Forbidden
     - 2: Attendance already registered for the day
     - 3: Error 500 Internal server Error


ERROR HANDLING:
~~~~~~~~~~~~~~~~
   - 1: Make sure to register as an Employee
   - 2: Once created cannot re register again for any query contact Admin department
   - 3: Please try again later


**Update Out-Time Attendance**
******************************

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


ERROR:
~~~~~~~~~~~~
     - 1: Error 400 Bad request
     - 2: Error 403 Permission Denied
     - 3: Error 500 Internal server Error


ERROR HANDLING:
~~~~~~~~~~~~~~~~
   - 1: Provide correct primary key of a Employee Attendance record
   - 2: Cannot re assign Attendance once registered
   - 3: Please try again later



**Change Password**
********************

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

ERROR:
~~~~~~~~~~~~
     - 1: Invalid Credential
     - 2: Session update failure
     - 3: Invalid data type


ERROR HANDLING:
~~~~~~~~~~~~~~~~
   - 1: Make sure the old password is correct and password and confirm password field should match
   - 2: Reload the page and try again
   - 3: Password format must be according to the given instruction


**Resetting Forgotten Password**
*********************************

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



ERROR:
~~~~~~~~~~~~
     - 1: Error 204 No Content
     - 2: Error 404 Not Found
     - 3: Token Generation Failure
     - 4: Mail sent failure


ERROR HANDLING:
~~~~~~~~~~~~~~~~
   - 1: Provide proper email in the input field
   - 2: Register the email address before proceeding to next step
   - 3: Retry again
   - 3: Try after some time
