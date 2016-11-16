# Reporter



Reporter is an API for creating selenium tests reports. It takes a report in JSON format and saves it into a MongoDB database. Reporter is a Report as a Service API, so we use flask_restful to design it as a RESTful API. We use MongoEngine as a ODM (Object Document Mapper) to handle the Report as Models; and Docker to containerize the service and use it as a microservice.

## How to run the API.

We just need to edit the docker-compose.yml file and substitute the `REPORTER_SERVICE_HOSTNAME` value `'your_ip_address_or_hostname'` for the IP address or domain/hostname of the server where the container is being run. Example `REPORTER_SERVICE_HOSTNAME=10.0.0.1` or `REPORTER_SERVICE_HOSTNAME=mydnsname.net`.

Then we replace in the volumes section, the value `'your_volume_here'` for the volume mapping of the MongoDB container with the path where you will persist MongoDB data. For example, `/Users/myuser/reporter/db_data:/bitnami/mongodb`, where db_data is any folder you create to save MongoDB data in the host system disk.

After doing this we just need to run:

`docker-compose up -d`

This will download and setup all required images, as well as build the API image using the `Dockerfile` which sets python 3 and all it's dependencies along with the API code.

To stop the API service we just run this command:

`docker-compose stop`

This will stop all containers.


Any feedbacks on the code or documentation are welcome.
