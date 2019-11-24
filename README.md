# ImproveProject

ImproveProject is a Django project that simulated numerous issues requiring debugging. ImproveProject was initially provided with a rough outline of views and templates including a significant database. Line by line, the objective was to bring this project not only into a working state, but an optimized and streamlined condition. 

Some of the Changes Included:
1. Namespacing the urls
2. Extending the menu app's url patterns list
3. Cleaning up and adding more view logic
4. Optimizing database queries in each view to be under 5 database hits, and in all taking less than 60ms 
5. Splitting up common components and features in the tempaltes - taking advatage of inheritance and template tags
6. Correcting models by first adding fields of correct data type, writing a custom data-migration to convert and move the existing data, then a deletion of the old field  
7. Adding validation to forms
8. Cleaning up messy code as per PEP 8
9. Writing from scratch tests for the views, models, and forms - pushing coverage from below 50% to 95%


<br/>

# installation

1. cd into your directory of projects (or wherever you prefer to keep your clones)
2. git clone ```https://github.com/Marksparkyryan/ImproveProject.git``` to clone the app
3. ```virtualenv .venv``` to create your virtual environment
4. ```source .venv/bin/activate``` to activate the virtual environment
5. ```pip install -r ImproveProject/requirements.txt``` to install app requirements
6. cd into the ImproveProject/improveproject directory
7. ```python manage.py migrate``` to apply the existing data and model migrations
8. ```python manage.py runserver``` to serve the site to your local host (in DEBUG mode)
9. visit ```http://127.0.0.1:8000/``` to see some menus! 


<br/>

# usage

Note: this has been pushed with the latest database

By default, there is a django-debug-toolbar app installed for continued testing. Remove from installed apps in settings if required.

<br/>

# credits

Treehouse TechDegree project 9
