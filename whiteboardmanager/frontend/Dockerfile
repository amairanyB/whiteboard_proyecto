# Usa una imagen base de Node.js
FROM node:16

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del frontend al contenedor
COPY . /app/

# Instala las dependencias de React
RUN npm install

# Construye la aplicación de React para producción
RUN npm run build

# Exponer el puerto 3000 para React
EXPOSE 3000

# Comando para iniciar la aplicación de React
CMD ["npm", "start"]

