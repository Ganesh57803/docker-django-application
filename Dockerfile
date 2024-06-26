# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code
COPY Pipfile /code/
RUN pip install pipenv && pipenv install --skip-lock --system
# Install dependencies


# Copy project
COPY . /code/

# Run the application
CMD ["gunicorn", "your_project_name.wsgi:application", "--bind", "0.0.0.0:$PORT"]
