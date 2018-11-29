# Historical News Search

# Usage
## Bringing up the application

Start the application using ```docker-compose```:
```
$ docker-compose up [-d] [--build]
```

You can run all services in the background (detached mode) by adding the ```-d``` flag to the above command.
Furthermore you can build everything by adding the ```--build``` but this is no necessity. 

Start the Frontend using the following commands from the root directory:
```
$ cd hs-frontend
$ docker build -t hs-frontend .
$ docker run -it \
  -v ${PWD}:/usr/src/app \
  -v /usr/src/app/node_modules \
  -p 4200:4200 \
  --rm \
  hs-frontend
```
This command changes into the frontend folder, builds and tags the Docker image and spins up the container afterwards.

**You are now able to see the App visiting ```http://localhost:4200``` in your browser.**

## Bindings
By default, the application exposes the following ports:
* 5000: Flask API
* 9200: Elasticsearch HTTP
* 9300: Elasticsearch TCP Transport
* 5601: Kibana 
* 5044: Logstash TCP Input
