# Historical News Search

This Search Engine for Historical News is based on the dataset of the *Berliner Volkszeitung* published by the *Staatsbibliothek zu Berlin – Preußischer Kulturbesitz*. 

![Test](https://codingdavinci.de/img/daten/F_SBB_00009_19140802_062_361_0_001_cropped_1000px-wide_upper-half.png)

# Usage
## Bringing up the application

Start the application using ```docker-compose```:
```
$ docker-compose up [-d] [--build]
```

You can run all services in the background (detached mode) by adding the ```-d``` flag to the above command.
Furthermore you can build everything by adding the ```--build``` but this is no necessity. 

**You are now able to see the App visiting ```http://localhost:80``` in your browser.**

## Bindings
By default, the application exposes the following ports:
* 80:   NGINX Webserver
* 5000: Flask API
* 9200: Elasticsearch HTTP
