# Use an official Python runtime as a base image
FROM python:3.9-slim

# Install necessary system dependencies and fonts
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port that the Flask app will run on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
