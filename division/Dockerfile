# Use the python:3.8-alpine base image
FROM python:3.8-alpine

# Copy the contents of ./app/requirements.txt to /app/requirements.txt
COPY ./app/requirements.txt /app/requirements.txt

# Set the working directory to /app
WORKDIR /app

# Install dependencies and remove cache
RUN apk add --update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

# Copy the contents of ./app to /app folder
COPY ./app /app

# Run the command "python app.py"
CMD ["python", "app.py"]
