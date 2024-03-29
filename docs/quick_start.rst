Quick Start Guide
=================

Download EmployeeManagement Django Project Boilerplate
------------------------------------------------------

First, you need to download the BoilerPlate from GitHub. 

.. Secret Django Key
.. -----------------

.. This boilerplate has the **DJANGO_KEY** setting variable hidden. 

.. You can generate your DJANGO_KEY |django_key|.

.. .. |django_key| raw:: html
    
..     <a href="http://www.miniwebtool.com/django-secret-key-generator"
..     target="_blank">here</a>

Project Name
------------

This project is named *EmpDashboard*, so if you are using this 
Boilerplate to create your own project, you'll have to change 
the name in a few places:

 - *EmpDashboard* **folder** (your top project container)
 - *EmpDashboard/EmpDashboard* **folder** (your project name)
 - virtual environment names: **tb_dev** and **tb_test** (name them whatever you want)


Virtual environments and Settings Files
---------------------------------------
 
First, you must know your Python 3 path::

    where python3

which is something similar to C:\Users\Guest302\AppData\Local\Programs\Python\Python312\python.exe.
 
Next, create a Development virtual environment with Python 3 installed::
 
    $ python -m venv virtual_env_name
 

.. where you might need to change it with your python path.

.. Go to the virtual enviornment folder with::
 
..     $ cd $virtual_env_name/bin

.. and edit the postactivate file.:
 
..     $ vi postactivate
 
.. You must add the lines: ::
..     export DJANGO_SETTINGS_MODULE="EmployeeManagement.settings.development"
..     export SECRET_KEY="your_secret_django_key"


.. with your project name and your own secret key.
 
.. Next, edit the **predeactivate** file and add the line::
 
..     unset SECRET_KEY


.. Repeat the last steps for your testing environment::
 
..     $ mkvirtualenv --python=/usr/local/bin/python3 tb_test
..     $ cd $VIRTUAL_ENV/bin
..     $ vi postactivate

.. where you have to add the lines::
..     export DJANGO_SETTINGS_MODULE="taskbuster.settings.testing"
..     export SECRET_KEY="your_secret_django_key"

.. and in the predeactivate file::
..      unset SECRET_KEY

Next, install the packages in each environment::
    $ workon tb_dev
    $ pip install -r requirements/development.txt
    $ workon tb_test
    $ pip install -r requirements/testing.txt

Internationalization and Localization
-------------------------------------

Settings
********

.. The default language for this Project is **English**, and we use internatinalization to translate the text into Any Language.
 
.. If you want to change the translation language, or include a new one, you just need to modify the **LANGUAGE_CODE** variable in the file *settings.py*. The language codes that define each language can be found |codes_link|.
 
.. .. |codes_link| raw:: html
 
..     <a href="http://msdn.microsoft.com/en-us/library/ms533052(v=vs.85).aspx" target="_blank">here</a>
 
.. For example, if you want to use French, Spanish with English you should include::
..      from django.utils.translation import gettext_lazy as _
..      LANGUAGES = (
..         ...
..         ('en', _('English')),
..         ('fr', _('French')),
..         ('es', _('Spanish')),
..         ...
..     )

.. You can also specify a dialect, like Luxembourg's German with::
..     from django.utils.translation import gettext_lazy as _
..     LANGUAGES = (
..         ...
..         'de-lu', _("Luxemburg's German"),
..         ...
..     )

.. For the LANGUAGE_CODE to take effect, USE_I18N must be True, which enables Django's translation system.
..      TIME_ZONE = 'UTC'
     
..      USE_L10N = True
     
..      USE_TZ = True


.. Note: the name inside the translation function _("") is the language name in the default language (English).
 
.. More information on the |internationalization_post|. 
 
.. .. |internationalization_post| raw:: html
 
..     <a href="https://marinamele.com/taskbuster-django-tutorial/internationalization-localization-languages-time-zones" target="_blank">TaskBuster post</a>
 
 
.. Translation
.. ***********
 
.. Go to the terminal, inside the taskbuster_project folder and create the files to translate with::
 
..     $ python manage.py makemessages -l ca
 
.. change the language "ca" for your selected language.
 
.. Next, go to the locale folder of your language::
 
..     $ cd taskbuster/locale/ca/LC_MESSAGES
 
.. where taskbuster is your project folder. You have to edit the file *django.po* and translate the strings. You can find more information about how to translate the strings |translation_strings_post|.
 
.. .. |translation_strings_post| raw:: html
 
..     <a href="https://marinamele.com/taskbuster-django-tutorial/internationalization-localization-languages-time-zones#inter-translation" target="_blank">here</a>
 
.. Once the translation is done, compile your messages with::

..     $ python manage.py compilemessages -l ca
 
 
 
.. Tests
.. *****
 
.. We need to update the languages in our Tests to make sure the translation works correclty. Open the file *functional_tests/test_all_users.py*:
 
.. - in **test_internationalization**, update your languages with the translation of title text, here "Welcome to TaskBuster!"
.. - in **test_localization**, update your languages.
 
 
 
.. Useful commands
.. ---------------
 
.. A list of all the commands used to run this template::
 
..     $ workon tb_dev
..     $ workon tb_test
 
..     $ python manage.py makemessages -l ca
..     $ python manage.py compilemessages -l ca

