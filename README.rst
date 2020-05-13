===============================
Example Application for manage employee leave date
===============================

Assuming you use virtualenv, follow these steps to download and run the
django-allauth example application in this directory:

::

    $ git clone git://github.com/pennersr/django-allauth.git
    $ cd django_leave_online_system
    $ virtualenv venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt


Now we need to create the database tables and an admin user.
Run the following and when prompted to create a superuser choose yes and
follow the instructions:

::

    $ python manage.py migrate
    $ python manage.py createsuperuser
    
set up there following:

::

    $ setting.py config database


Now you need to run the Django development server:

::

    $ python manage.py runserver


You should then be able to open your browser on http://127.0.0.1:8000 and see a page with links to login and signup.

echo "# django_leave_online_system" >> README.rst


