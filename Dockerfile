FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all other files (make sure app.py is in same folder)
COPY . .

# Expose port (for clarity — not required in Cloud Run)
EXPOSE 8080

# Run your app
CMD ["python", "app.py"]
