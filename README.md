#AVITO
## Run database(docker)



docker run --name djangoProject2_postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:13.0-alpine 


