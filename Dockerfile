# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set environment variables
ENV SUPABASE_URL=https://gzfutsqkdbdqzozfaoit.supabase.co \
    SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd6ZnV0c3FrZGJkcXpvemZhb2l0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0OTA4MDIsImV4cCI6MjA3NTA2NjgwMn0.Mn2snCBYqmbTlqaLlqUgQ35uPZLKIDx1FhN6j8yMK2g

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .



# Then your install commands
RUN apt-get update && apt-get install -y --no-install-recommends gcc g++ \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && python -m spacy download en_core_web_sm \
    && apt-get remove -y gcc g++ \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*


# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 7860

# Command to run the application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
