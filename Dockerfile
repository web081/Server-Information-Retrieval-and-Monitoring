# Use the appropriate base image
FROM ubuntu:20.04

# Update package lists and install net-tools
RUN apt-get update && apt-get install -y net-tools

# Set the working directory
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Set the entrypoint or command to run your script
CMD ["python3", "devopsfetch.py"]
