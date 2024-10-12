# Spark Standalone Mode to a Cluster with Docker

## Spark Docker Image
- bitnami/spark:3.5.2

## Spark cluster
- spark master
- spark worker 1
- spark worker 2
- jupyter notebook (optional)

## Make Directories
- apps : Spark Applications
- jars : .jar files

## Docker Setting
- `Dockerfile`: build image for spark
- `docker-compose.yaml`: Spark Standalone cluster containers