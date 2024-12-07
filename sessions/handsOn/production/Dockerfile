# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the code
COPY app.py /app

# Install Flask
RUN pip install Flask requests

# Run the application
CMD ["python", "app.py"]
