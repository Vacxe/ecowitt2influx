FROM python:3.12-slim

WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install fastapi uvicorn influxdb-client

# Copy application code
COPY src/ .

# Expose the port FastAPI will run on
EXPOSE 80

# Start the FastAPI application using uvicorn
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]