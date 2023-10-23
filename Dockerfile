# Usa una imagen de Python como base
FROM python:3.10-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY requirements.txt .
COPY app.py .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que tu aplicación Flask estará escuchando
EXPOSE 5001

# Comando para ejecutar tu aplicación
CMD ["python", "app.py"]
