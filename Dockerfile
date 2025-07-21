# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY generate_qr.py .

# Create directory for QR codes
RUN mkdir qr_codes

# Run the app
CMD ["python", "generate_qr.py"]
