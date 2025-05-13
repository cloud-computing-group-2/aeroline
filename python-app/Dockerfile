# Usar una imagen base oficial de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requerimientos e instalarlos
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código fuente
COPY . .

# Exponer el puerto 8082
EXPOSE 8082

# Comando para iniciar la aplicación FastAPI usando Uvicorn en el puerto 8082
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8082"]
