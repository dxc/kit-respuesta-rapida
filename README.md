# kit-respuesta-rapida
Landing page del kit de respuesta rápida para catástrofe

Repositorio Chile Ayuda

Collaborator

#############################
Software:
   >Python 3.4
   >Django 1.7.7
#############################


1.- Download the latest version of the code

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



######
Tutorial para subir el proyecto a https://www.pythonanywhere.com

1.- Crear un usuario

2.- Crear una "web app", en este caso "kit_rr", dándole como parámetros Django y Python3.4. No tomar en cuenta la versión de Django por ahora.

3.- Abrir una consola bash (Dashboard/Consoles) de las que nos entrega la página, en ella crearemos un virtualenv y le instalaremos Django 1.7.7:
    >virtualenv -p /usr/bin/python3.4 venv
    >cd venv
    >source bin/activate
    >pip install django==1.7.7
    >deactivate

4.- En Dashboard/WEB/Virtualenv agregamos el PATH en donde se creó el virtualenv, de este estilo mas o menos: /home/user/venv. Luego en Dashboard/WEB/Code modificamos el archivo: /var/www/user_pythonanywhere_com_wsgi.py
Con las instruccciones para django 1.7 que salen en los comentarios, reemplazar 2 líneas de código.

5.- En Menu/Files borramos la carpeta que nos crea por defecto pythonanywhere "kit_rr"

6.- Entramos nuevamente a la consola para clonar el código en el servidor
    >git clone https://github.com/dxc/kit-respuesta-rapida.git
    >mv kit-respuesta-rapida kit_rr

7.- En Menu/WEB/StatiFiles modificar /static/ por /home/user/kit_rr/static/static

8.- En Menu/WEB/Actions clickear el botón RELOAD user.pythonanywhere.com

9.- Todo está listo, ahora solo dirigirse a user.pythonanywhere.com



# Comandos WSGI

wsgi -x django.xml
ctrl+z
bg
exit
