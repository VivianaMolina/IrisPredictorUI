# Uses python version 3.10 as our base image
FROM python:3.10

# Goes to the app directory 
WORKDIR /app

# Copy files
COPY server.py .
COPY requirements.txt .

# Copy the model file into the correct subdirectory
COPY models/model_iris.pkl models/model_iris.pkl

# Install app dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port so our computer can access it
EXPOSE 5000

#RUN the app
CMD [ "python", "server.py"]