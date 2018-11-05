FROM node:11.1.0-slim

ADD . /app

COPY . /app

# Install dependencies
WORKDIR /app

RUN npm install

RUN npm i -g serve

# Build the app
RUN npm build

# Start the app
CMD serve -s build
