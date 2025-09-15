FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && playwright install chromium

# Copy code
COPY whitepages_mcp.py .

CMD ["python", "whitepages_mcp.py"]
