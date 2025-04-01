FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .
# Install the required packages
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

CMD ["python", "main.py"]
