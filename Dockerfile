FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Set port
ENV PORT=8000
EXPOSE 8000

# Run gunicorn
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 120 app:app



