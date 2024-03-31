FROM python:3.9

# Install any dependencies required for your service
# For example, if you need additional Python packages:
# RUN pip install package1 package2 ...

# Set up a directory for your application code
WORKDIR /app
COPY /requirements.txt /app

# Copy your application code into the container
COPY /app /app
#COPY /pip-cache/ /root/.cache/pip/

# Run your service
CMD ["tail", "-f", "/dev/null"]

# Alternatively, if your service doesn't run continuously, you can use a simple command
# to keep the container running, for example:
# CMD ["tail", "-f", "/dev/null"]
