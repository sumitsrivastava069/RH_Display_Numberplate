FROM python:3.10

WORKDIR /app

# Copy the source code to the working directory
COPY . .
RUN mkdir -p /app/static/yoloimages  && mkdir -p /app/static/numberplateimages && chmod -R 777 /app
#python -m pip install --upgrade pip
# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y libsm6 libxext6 ffmpeg


# Expose port 5000 for
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
