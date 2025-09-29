# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
EXPOSE 5000
# use a production server:
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
