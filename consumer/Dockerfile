
# Base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the socket server file to the container
COPY consumer.py .


CMD ["python","consumer.py"]

RUN pip install pymongo[srv]  kafka-python python-dotenv==0.19.2
