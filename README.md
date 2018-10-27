# HistoricalNewsSearch

# Build

Bauen mit:

`docker build . -t app`

Dann starten mit:

`docker run app`

oder einfacher mit docker-compose:

`docker-compose up [--build]`

Elasticsearch muss entweder selbst auf dem Rechner laufen oder mit `./start-elasticsearch-server.sh` mit docker gestartet werden.
