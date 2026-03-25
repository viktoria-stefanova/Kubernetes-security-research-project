# Dockerfile for Internal Dashboard (Attacker Pod)
FROM python:3.9-slim

WORKDIR /app

# Install Flask
RUN pip install --no-cache-dir flask

# Copy application
COPY attacker-app.py /app/

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "attacker-app.py"]