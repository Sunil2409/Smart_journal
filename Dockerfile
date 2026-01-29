FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Replace the old CMD with this:
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "journal_project.wsgi:application"]