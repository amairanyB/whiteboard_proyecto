# Imagen base con Python 3.12
FROM python:3.12-slim

# Instalar herramientas básicas y Node.js
RUN apt-get update && apt-get install -y nodejs npm

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto al contenedor
COPY . .

# Instalar pipenv y dependencias de Python
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy

# Instalar dependencias de Node.js
RUN npm install

# Exponer el puerto que usa Django (8000 por defecto)
EXPOSE 8000

# Comando para ejecutar el servidor
CMD ["python", "whiteboardmanager/manage.py", "runserver", "0.0.0.0:8000"]
