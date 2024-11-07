# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt /app/requirements.txt

# Copy the entire backend source code into the container
COPY . /app/

# Install any needed dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 to the outside world
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app when the container launches
CMD ["python", "main.py"]
