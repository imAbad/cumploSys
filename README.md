Instrucciones para ejecutar la APP.

1. Crear un entorno virtual con el comando "virtualenv -p python3 nEntorno"
    nEntorno es el nombre que tendrá el entorno virtual, ejemplo "env"
2. Activar el entorno virtual 
    2.1 Entra a la ruta 'nEntorno\Scripts\' y una vez dentro ejecutar 'activate'
    Esto activara el entorno y aparecerá el nombre del entorno virtual creado en la linea de comandos entre parentesis, eje. "(env)".
3. Instalar las librerías a usar, para instalar se debe pocisionar en la raiz del proyecto "cumploSys" mediante el comando "cd..", repitalo hasta que llegue a la raiz del proyecto.
    3.1 Instalar las librerias del archivo requirements con el comando 'pip install -r requirements.txt'
4. Una vez instaladas todas las librerías, se deberá ejecutar "python manage.py runserver", esto le mostrará el puerto donde se debe abrír la web app, comunmente es http://127.0.0.1:8000/
5. Listo!, abrir el puerto y probar la app!                                                                                       