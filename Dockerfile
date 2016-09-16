FROM ubuntu
MAINTAINER Juan Polanco
RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install Flask
RUN pip install mongoengine
RUN pip install flask-restful
COPY selenium-reporter.py /home
WORKDIR /home
ENTRYPOINT ["python" ]
CMD ["selenium-reporter.py"]
EXPOSE 5000
