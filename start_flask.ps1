# Navega hasta el directorio de tu entorno virtual
cd .\env

# Activa el entorno virtual
.\Scripts\activate

# Navega de vuelta al directorio de tu proyecto
cd ..

# Configura la variable de entorno FLASK_APP
$env:FLASK_APP = "main.py"
$env:USE_SAMPLE_DATA = "True"

# Inicia la aplicación Flask
flask run