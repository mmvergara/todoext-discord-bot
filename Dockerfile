FROM python:3.11.7-alpine3.19
# Copy all files from current directory to /app inside the container

COPY . /app
# Set the working directory to /app

WORKDIR /app

# Install the dependencies from requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "bot.py"]


