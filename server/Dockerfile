# Base image
FROM python:3.9

# Set the working directory
WORKDIR ./server

# Copy the socket server file to the container
COPY server.py .

# Run the socket server
CMD ["python","server.py"]


RUN pip3 install kafka-python