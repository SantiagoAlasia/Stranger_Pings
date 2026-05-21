FROM python:3.12

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos del proyecto
COPY . .

# Puerto que usa el servidor
EXPOSE 5000

# Comando para ejecutar el servidor
CMD ["python", "src/server.py"]