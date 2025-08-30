FROM python:3.9-slim

# image name: wottreng/object-detection

# Set working directory
WORKDIR /app

# Install system dependencies
# dockerfile
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    git \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libgomp1 \
    nano \
 && rm -rf /var/lib/apt/lists/*


# Copy requirements first for better layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the port
EXPOSE 1300

# Run the application
CMD ["python", "main.py", "--port", "1300"]
