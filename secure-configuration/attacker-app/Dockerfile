# Dockerfile for Internal Dashboard (Attacker Pod)
FROM python:3.9-slim

WORKDIR /app

# Install Flask and curl
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir flask

# Copy application
COPY attacker-app.py /app/

EXPOSE 5000

CMD ["python", "attacker-app.py"]
