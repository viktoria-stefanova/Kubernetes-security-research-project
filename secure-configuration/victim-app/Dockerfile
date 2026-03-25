# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install curl and Flask
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir flask

# Copy application code
COPY victim-app.py /app/

# Expose port 8080
EXPOSE 8080

# Run the Flask application
CMD ["python", "victim-app.py"]
