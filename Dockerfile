# Use an official Python runtime image (slim version for a smaller image)
FROM python:3.11-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project files into the container
COPY . .

# Expose port 8000 for the FastAPI app
EXPOSE 8000

# Run the FastAPI application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]