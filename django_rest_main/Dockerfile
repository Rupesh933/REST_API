FROM python:3.13-slim

# Prevent Python from writing .pyc files and buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app

EXPOSE 8000

# Run development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]