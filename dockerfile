FROM python:3.11-slim

# Set environment variables for Ubuntu compatibility
ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Etc/UTC

# Install essential Ubuntu packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    tzdata \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Expose three ports (HTTP, HTTPS, and alternative HTTP)
EXPOSE 80    
EXPOSE 443   
EXPOSE 8080  

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY .env .env

COPY . .

CMD ["python", "main.py"]