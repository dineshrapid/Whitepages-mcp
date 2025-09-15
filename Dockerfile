FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && playwright install chromium

# Copy code
COPY whitepages-mcp.py .

CMD ["python", "whitepages-mcp.py"]
