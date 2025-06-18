FROM python:3.12

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y iputils-ping

COPY . /app/

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "aircraft_production.wsgi:application", "--bind", "0.0.0.0:8000"]
