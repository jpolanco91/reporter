FROM ubuntu:latest
MAINTAINER Juan Polanco

# Updating repos and installing software-properties-common to ensure
# we have the latest PPA repos.
RUN apt-get update && apt-get -y install software-properties-common
RUN apt-get -y install python3-pip
RUN pip3 install Flask
RUN pip3 install mongoengine
RUN pip3 install flask-restful
CMD ["mkdir","/home/models"]
COPY models /home/models
COPY selenium-reporter.py /home
WORKDIR /home
ENTRYPOINT ["python3" ]
CMD ["selenium-reporter.py"]
EXPOSE 5000
