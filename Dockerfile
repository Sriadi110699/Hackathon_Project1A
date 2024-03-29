# Use an official Python runtime as a parent image
FROM python:3.9.2-slim-buster
 
# Set the working directory in the container to /app
WORKDIR /app
 
# Add the current directory contents into the container at /app
ADD . /app
 
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
 
# Make port 8501 available to the world outside this container
EXPOSE 8017
 
# Define environment variable
ENV GOOGLE_APPLICATION_CREDENTIALS /app/key.json
 
# Run app.py when the container launches
CMD ["streamlit", "run", "app.py"]
