# kit-respuesta-rapida
Landing page del kit de respuesta rápida para catástrofe

Repositorio Chile Ayuda

Collaborator

#############################
Software:
   >Python 3.4
   >Django 1.7.7
#############################


1.- Download last version of the code

2.- Create database
   > python manage.py syncdb

3.- Migrate changes in the database (this step may not be needed in all systems)
   > python manage.py makemigrations maps
   > python manage.py migrate

4.- Load initial data to the database
   > python manage.py loaddata data.json (now is category.json)

5.- Run the server
   > python manage.py runserver (any port)

6.- Now the following URL will take you to the index page
   > 127.0.0.1:8000/
