



FROM python:3.12-slim

# Evita que Python escriba archivos .pyc y almacene en búfer de salida
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Crear el usuario y grupo 'melodify'
RUN groupadd -r melodify && useradd -r -g melodify melodify

WORKDIR /src/melodify

# Instalar dependencias como root
COPY requirements.txt /src/melodify/

# Instalar ffmpeg
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /src/melodify/requirements.txt

# Crear estructura necesaria
RUN mkdir -p \
    /library \
    /static/melodify

# Copiar proyecto directamente con ownership correcto
COPY --chown=melodify:melodify . /src/melodify

# Ajustar permisos SOLO donde hace falta
#RUN chown -R melodify:melodify \
#    /library \
#    /media/melodify \
#    /static/melodify \
#    /src/melodify && \
#    chmod -R 775 /src/melodify/media

# Cambiar a usuario no-root
#USER melodify

# Ejecutar migraciones, recopilar estáticos y arrancar Gunicorn
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py makemigrations main && python manage.py migrate && python manage.py migrate main && python manage.py importfonts && python manage.py importschemes && python manage.py collectstatic --noinput && gunicorn backend.wsgi:application --bind 0.0.0.0:8000"]
#CMD ["sh", "-c", "python manage.py migrate --fake && python manage.py migrate main --fake && gunicorn backend.wsgi:application --bind 0.0.0.0:8000"]
