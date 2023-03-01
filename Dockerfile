FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# # Copy the requirements file to the container
COPY ./requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip install -r /app/requirements.txt
COPY . .

# Expose port 80 for the API
EXPOSE 8000

# Run the app
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port" ,"8000", "--reload" ]