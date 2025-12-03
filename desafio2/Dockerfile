FROM python:3.9-slim

WORKDIR /app

COPY logger_app.py .

# Create the data directory where the volume will be mounted
RUN mkdir -p /app/data

CMD ["python", "logger_app.py"]
