# Use a Python base image
FROM python:3.11

# Set environment variables
ENV FLASK_APP=app.py \
    FLASK_ENV=production \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=5000

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the port that the Flask application will run on
EXPOSE $PORT

# Start the Flask application
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "$PORT"]
