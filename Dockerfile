# Use an official Python runtime as a base image
FROM python:3.9-slim

# Install MySQL development libraries and build tools, which include mysql_config
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port that the app runs on
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "localhost:8000"]
