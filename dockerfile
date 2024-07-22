FROM python:3.9-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Setup container directories
RUN mkdir /app

# Copy local code to the container
COPY . .

WORKDIR /app


VOLUME ["/files"]

VOLUME ["/uploads"]

CMD ["python", "main.py"]
