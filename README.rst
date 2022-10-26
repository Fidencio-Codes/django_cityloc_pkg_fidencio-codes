Django Packaging Exercise 

Will be creating a package in order to install it into an existing Django project

STEPS
1. Setup the project directory 
- python -m venv venv
- . venv/Scripts/activate
- pip install wheel setuptools twine
- citylocations.zip

2. Create package configuration files
- README.rst
- setup.cfg
- setup.py
- MANIFEST.in
- LICENSE.txt

3. Build package 
- (bash terminal) python setup.py sdist

4. Install packaged app (on week4 folder)
- hello_django.zip
- pip install -r requirements.txt
- ls ../django_cityloc_pkg/dist
- pip install ../django_cityloc_pkg/dist/django_cityloc_pkg-0.0.1.tar.gz
- pip list (to double check pkg installed)

5. Connect new app to project
- python manage.py runserver 8000
- Open a browser, and type: http://127.0.0.1:8000 (should see "Hello World")
- update message and restart app to see new message


==============
City Locations
==============

City Locations is a Django app that can be installed in an existing Django project
Documentation: https://toddpy-django-cityloc-pkg.readthedocs.io/en/latest/

------------
Installation
------------

1. Add "citylocations" to your INSTALLED_APPS setting in settings.py:
    
    INSTALLED_APPS = [
        ...
        'citylocations',
    ]

2. Include the citylocations URLconf in your project urls.py like this::
    path('', include('citylocations.urls')),

3. Start the development server and visit http://127.0.0.1:8000/