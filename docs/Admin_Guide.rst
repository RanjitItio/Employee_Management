===================
Admin Journey
===================

Admin Login Page
----------------

.. image:: /Images/admin_login.png
   :alt: Admin Login Page

Coding Process:
~~~~~~~~~~~~~~~~~

Description:
    The login method is responsible for rendering the login form for the admin interface. It first checks if the user is already logged in and redirects to the admin index if so. Otherwise, it renders the login form using Django's built-in authentication views. The admin login process in Django is facilitated by the ``django.contrib.admin.sites.AdminSite.login`` method. This method allows administrators to securely authenticate themselves and access the administrative interface for managing Django models.

Parameters:
    - ``self``: The instance of the admin site.
    - ``request``: The HTTP request object.
    - ``extra_context``: Additional context data to be passed to the login template.

Returns:
    An HTTP response containing the rendered login form.

Dependencies:
    - ``never_cache`` method decorator.
    - ``AdminAuthenticationForm`` from ``django.contrib.admin.forms``.
    - ``LoginView`` from ``django.contrib.auth.views``.

Usage Notes:
    This method is typically used within a custom admin class for a Django model.

Security Considerations:
    Ensure that the ``never_cache`` decorator is applied to prevent caching of sensitive information.

Code Example:
~~~~~~~~~~~~~

.. code-block:: python

    @admin.register(CustomUser)
    class CustomUserAdmin(admin.ModelAdmin):
        def login(self, request, extra_context=None):
            """
            Display the login form for the given HttpRequest.
            """
            if request.method == "GET" and self.has_permission(request):
                # Already logged-in, redirect to admin index
                index_path = reverse("admin:index", current_app=self.name)
                return HttpResponseRedirect(index_path)
            return LoginView.as_view(**defaults)(request)


Admin Home Page
------------------

.. image:: /Images/admin_homepage.png
   :alt: Admin Home Page

Coding Process:
~~~~~~~~~~~~~~~~~

.. code-block:: python

        @user_passes_test(lambda u: u.is_staff, login_url='/login/')
        @login_required
        def HomePage(request):
            """
            View for rendering the home page.
            Args:
                request: The HTTP request object.
            Returns:
                If the user is authenticated, renders the home page with employee details and attendance information.
                If the user is not authenticated, renders the home page without any employee details or attendance information.
            """

            user = request.user
            employee_id = None
            employee_detail = None
            employee_attendance_id = None

            if user.is_authenticated:
                # Retrieve employee details and attendance information
                # ...
            else:
                employee_id = None
                employee_detail = None

            context = {
                'employee_id': employee_id,
                'employee_detail': employee_detail,
                'employee_attendance_id': employee_attendance_id
            }

            return render(request, 'Users/home.html', context)


**All User Interface**
----------------------

.. image:: /Images/all_users.png
   :alt: All User Interface Page

Coding Process:
~~~~~~~~~~~~~~~~~

.. code-block:: python

        @csrf_protect_m
        def changelist_view(self, request, extra_context=None):
            """
            The 'change list' admin view for this model.
            Args:
                request: The HTTP request object.
                extra_context: Additional context data (optional).
            Returns:
                The rendered template response for the change list view.
            """
            from django.contrib.admin.views.main import ERROR_FLAG

            app_label = self.opts.app_label
            if not self.has_view_or_change_permission(request):
                raise PermissionDenied

            try:
                cl = self.get_changelist_instance(request)
            except IncorrectLookupParameters:
                # Wacky lookup parameters were given, so redirect to the main
                # changelist page, without parameters, and pass an 'invalid=1'
                # parameter via the query string. If wacky parameters were given
                # and the 'invalid=1' parameter was already in the query string,
                # something is screwed up with the database, so display an error
                # page.
                if ERROR_FLAG in request.GET:
                    return SimpleTemplateResponse(
                        "admin/invalid_setup.html",
                        {
                            "title": _("Database error"),
                        },
                    )
                return HttpResponseRedirect(request.path + "?" + ERROR_FLAG + "=1")

            # Rest of the code...


**Create New User Interface**
-----------------------------

Create New User Page
~~~~~~~~~~~~~~~~~~~~

.. image:: /Images/create_user.png
   :alt: Create New User Page

Coding Process:
~~~~~~~~~~~~~~~~

.. code-block:: python

    @sensitive_post_parameters_m
    @csrf_protect_m
    def add_view(self, request, form_url="", extra_context=None):
        """
        View for displaying the add form for a new model instance.
        Args:
            request: The HTTP request object.
            form_url: The URL to submit the form to (optional).
            extra_context: Additional context data (optional).

        Returns:
            The rendered template response for the add view.
        """
        with transaction.atomic(using=router.db_for_write(self.model)):
            return self._add_view(request, form_url, extra_context)


**Update a User Detail**
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /Images/update_user.png
   :alt: Update Esisting User

Coding Process:
~~~~~~~~~~~~~~~~

.. code-block:: python

    def change_view(self, request, object_id, form_url="", extra_context=None):
        """
        View for displaying the change form for an existing model instance.
        Args:
            request: The HTTP request object.
            object_id: The ID of the model instance to be changed.
            form_url: The URL to submit the form to (optional).
            extra_context: Additional context data (optional).

        Returns:
            The rendered template response for the change view.
        """
        return self.changeform_view(request, object_id, form_url, extra_context)


**Delete User Interface**
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /Images/delete_user.png
   :alt: Update Existing User


Coding Process:
~~~~~~~~~~~~~~~~

.. code-block:: python

    @csrf_protect_m
    def delete_view(self, request, object_id, extra_context=None):
        """
        View for displaying the delete confirmation page for a model instance.
        Args:
            request: The HTTP request object.
            object_id: The ID of the model instance to be deleted.
            extra_context: Additional context data (optional).

        Returns:
            The rendered template response for the delete view.
        """
        with transaction.atomic(using=router.db_for_write(self.model)):
            return self._delete_view(request, object_id, extra_context)


**All Employee Interface**
--------------------------

All Employee Page
~~~~~~~~~~~~~~~~~~~~~

.. image:: /Images/all_emp.png
   :alt: All Employee


Coding Process:
~~~~~~~~~~~~~~~~

.. code-block:: python

    def changelist_view(self, request, extra_context=None):
        """
        The 'change list' admin view for this model.
        Args:
            request: The HTTP request object.
            extra_context: Additional context data (optional).

        Returns:
            The rendered template response for the change list view.
        """
        from django.contrib.admin.views.main import ERROR_FLAG

        app_label = self.opts.app_label
        if not self.has_view_or_change_permission(request):
            raise PermissionDenied
        try:
            cl = self.get_changelist_instance(request)
        except IncorrectLookupParameters:
            # Wacky lookup parameters were given, so redirect to the main
            # changelist page, without parameters, and pass an 'invalid=1'
            # parameter via the query string. If wacky parameters were given
            # and the 'invalid=1' parameter was already in the query string,
            # something is screwed up with the database, so display an error
            # page.
            if ERROR_FLAG in request.GET:
                return SimpleTemplateResponse(
                    "admin/invalid_setup.html",
                    {
                        "title": _("Database error"),
                    },
                )
            return HttpResponseRedirect(request.path + "?" + ERROR_FLAG + "=1")

        # Rest of the code...


**Create New Employee**
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /Images/create_emp.png
   :alt: Create New Employee Page

Coding Process:
~~~~~~~~~~~~~~~~

.. code-block:: python

    @sensitive_post_parameters_m
    @csrf_protect_m
    def add_view(self, request, form_url="", extra_context=None):
        """
        View for displaying the add form for a new model instance.
        Args:
            request: The HTTP request object.
            form_url: The URL to submit the form to (optional).
            extra_context: Additional context data (optional).

        Returns:
            The rendered template response for the add view.
        """
        with transaction.atomic(using=router.db_for_write(self.model)):
            return self._add_view(request, form_url, extra_context)


**Update Existing Employee**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /Images/update_emp.png
   :alt: Update Existing employee

Coding Process:
~~~~~~~~~~~~~~~~

.. code-block:: python

    def change_view(self, request, object_id, form_url="", extra_context=None):
        """
        View for displaying the change form for an existing model instance.

        Args:
            request: The HTTP request object.
            object_id: The ID of the model instance to be changed.
            form_url: The URL to submit the form to (optional).
            extra_context: Additional context data (optional).

        Returns:
            The rendered template response for the change view.
        """
        return self.changeform_view(request, object_id, form_url, extra_context)


**Delete an Employee**
~~~~~~~~~~~~~~~~~~~~~~

.. image:: /Images/delete_emp.png
   :alt: Delete Existing employee


Coding Process:
~~~~~~~~~~~~~~~~

.. code-block:: python

    @csrf_protect_m
    def delete_view(self, request, object_id, extra_context=None):
        """
        View for displaying the delete confirmation page for a model instance.
        Args:
            request: The HTTP request object.
            object_id: The ID of the model instance to be deleted.
            extra_context: Additional context data (optional).

        Returns:
            The rendered template response for the delete view.
        """
        with transaction.atomic(using=router.db_for_write(self.model)):
            return self._delete_view(request, object_id, extra_context)



**Employee Attendance Interface**
---------------------------------

Employee Attendance Page:
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /Images/emp_attendance.png
   :alt: Employee Attendance Page

Coding Process:
~~~~~~~~~~~~~~

.. code-block:: python

    @csrf_protect_m
    def changelist_view(self, request, extra_context=None):
        """
        The 'change list' admin view for this model.
        Args:
            request: The HTTP request object.
            extra_context: Additional context data (optional).
        Returns:
            The rendered template response for the change list view.
        """
        from django.contrib.admin.views.main import ERROR_FLAG

        app_label = self.opts.app_label
        if not self.has_view_or_change_permission(request):
            raise PermissionDenied

        try:
            cl = self.get_changelist_instance(request)
        except IncorrectLookupParameters:
            # Wacky lookup parameters were given, so redirect to the main
            # changelist page, without parameters, and pass an 'invalid=1'
            # parameter via the query string. If wacky parameters were given
            # and the 'invalid=1' parameter was already in the query string,
            # something is screwed up with the database, so display an error
            # page.
            if ERROR_FLAG in request.GET:
                return SimpleTemplateResponse(
                    "admin/invalid_setup.html",
                    {
                        "title": _("Database error"),
                    },
                )
            return HttpResponseRedirect(request.path + "?" + ERROR_FLAG + "=1")

        # Rest of the code...


**CREATE NEW EMPLOYEE ATTENDANCE**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create Attendance Page:
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /Images/create_emp_attendance.png
   :alt: Create Attendance Page

Coding Process:
~~~~~~~~~~~~~~

.. code-block:: python

    @sensitive_post_parameters_m
    @csrf_protect_m
    def add_view(self, request, form_url="", extra_context=None):
        """
        View for displaying the add form for a new model instance.
        Args:
            request: The HTTP request object.
            form_url: The URL to submit the form to (optional).
            extra_context: Additional context data (optional).

        Returns:
            The rendered template response for the add view.
        """
        with transaction.atomic(using=router.db_for_write(self.model)):
            return self._add_view(request, form_url, extra_context)


**UPDATE EMPLOYEE ATTENDANCE REPORT**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Update Attendance Report Page:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /Images/update_emp_attendance.png
   :alt: Update Attendance Report Page

Coding Process:
~~~~~~~~~~~~~~

.. code-block:: python

    def change_view(self, request, object_id, form_url="", extra_context=None):
        """
        View for displaying the change form for an existing model instance.
        Args:
            request: The HTTP request object.
            object_id: The ID of the model instance to be changed.
            form_url: The URL to submit the form to (optional).
            extra_context: Additional context data (optional).

        Returns:
            The rendered template response for the change view.
        """
        return self.changeform_view(request, object_id, form_url, extra_context)


**DELETE EMPLOYEE ATTENDANCE REPORT**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Delete Attendance Report Page:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /Images/delete_emp_attendance.png
   :alt: Delete Attendance Report Page

Coding Process:
~~~~~~~~~~~~~~

.. code-block:: python

    @csrf_protect_m
    def delete_view(self, request, object_id, extra_context=None):
       """
      View for displaying the delete confirmation page for a model instance.
       Args:
            request: The HTTP request object.
            object_id: The ID of the model instance to be deleted.
            extra_context: Additional context data (optional).

        Returns:
            The rendered template response for the delete view.
       """
        with transaction.atomic(using=router.db_for_write(self.model)):
            return self._delete_view(request, object_id, extra_context)


**All Department Section**
--------------------------

All Department Page:
~~~~~~~~~~~~~~~~~~~~~

.. image:: /Images/all_department.png
   :alt: All Department Page

Coding Process:
~~~~~~~~~~~~~~

.. code-block:: python

    @csrf_protect_m
    def changelist_view(self, request, extra_context=None):
        """
       The 'change list' admin view for this model.
        Args:
            request: The HTTP request object.
            extra_context: Additional context data (optional).
        Returns:
            The rendered template response for the change list view.
        """
        from django.contrib.admin.views.main import ERROR_FLAG

        app_label = self.opts.app_label
        if not self.has_view_or_change_permission(request):
            raise PermissionDenied

        try:
            cl = self.get_changelist_instance(request)
        except IncorrectLookupParameters:
            # Wacky lookup parameters were given, so redirect to the main
            # changelist page, without parameters, and pass an 'invalid=1'
            # parameter via the query string. If wacky parameters were given
            # and the 'invalid=1' parameter was already in the query string,
            # something is screwed up with the database, so display an error
            # page.
            if ERROR_FLAG in request.GET:
                return SimpleTemplateResponse(
                    "admin/invalid_setup.html",
                    {
                        "title": _("Database error"),
                    },
                )
            return HttpResponseRedirect(request.path + "?" + ERROR_FLAG + "=1")

        # Rest of the code...


**CREATE NEW DEPARTMENT**
~~~~~~~~~~~~~~~~~~~~~~~~~~

Create New Department Page:
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /Images/create_department.png
   :alt: Create New Department Page

Coding Process:
~~~~~~~~~~~~~~

.. code-block:: python

    @sensitive_post_parameters_m
    @csrf_protect_m
    def add_view(self, request, form_url="", extra_context=None):
        """
        View for displaying the add form for a new model instance.
        Args:
            request: The HTTP request object.
            form_url: The URL to submit the form to (optional).
            extra_context: Additional context data (optional).

        Returns:
            The rendered template response for the add view.
        """
        with transaction.atomic(using=router.db_for_write(self.model)):
            return self._add_view(request, form_url, extra_context)


**UPDATE AN EXISTING DEPARTMENT**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Update Department Page:
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /Images/update_department.png
   :alt: Update Department Page

Coding Process:
~~~~~~~~~~~~~~

.. code-block:: python

    def change_view(self, request, object_id, form_url="", extra_context=None):
        """
        View for displaying the change form for an existing model instance.
        Args:
            request: The HTTP request object.
            object_id: The ID of the model instance to be changed.
            form_url: The URL to submit the form to (optional).
            extra_context: Additional context data (optional).
        Returns:
        The rendered template response for the change view.
        """
        return self.changeform_view(request, object_id, form_url, extra_context)

**Delete Any Department**
-------------------------

Delete Department Page:
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /Images/delete_department.png
   :alt: Delete Department Page

Coding Process:
~~~~~~~~~~~~~~

.. code-block:: python

    @csrf_protect_m
    def delete_view(self, request, object_id, extra_context=None):
       """
      View for displaying the delete confirmation page for a model instance.
       Args:
            request: The HTTP request object.
            object_id: The ID of the model instance to be deleted.
            extra_context: Additional context data (optional).

        Returns:
            The rendered template response for the delete view.
       """
        with transaction.atomic(using=router.db_for_write(self.model)):
            return self._delete_view(request, object_id, extra_context)

