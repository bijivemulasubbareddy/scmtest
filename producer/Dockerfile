# Base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the socket server file to the container
COPY producer.py .

# Run the socket server
CMD ["python","producer.py"]


RUN pip3 install python-dotenv kafka-python