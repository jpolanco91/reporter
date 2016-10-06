# Using bitnami/mongodb:latest image for MongoDB https://hub.docker.com/r/bitnami/mongodb/

from datetime import datetime
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from mongoengine import *
from bson.json_util import dumps
import json
import os

# Creating our webservice (app)
app = Flask(__name__)
service_hostname = os.environ.get('REPORTER_SERVICE_HOSTNAME')
connect('selenium-reports', host=service_hostname, port=27017)
api = Api(app)

class Report(Document):
    report_id = IntField(unique=True)
    title = StringField()
    date = DateTimeField(default=datetime.now)
    start_time = StringField()
    duration = FloatField()
    status = StringField()
    article_tests = ListField()
    gallery_tests = ListField()
    homepage_tests = ListField()
    mediaos_article_tests = ListField()
    mediaos_collection_tests = ListField()
    mediaos_article_testslogin_tests = ListField()
    mediaos_search_content_tests = ListField()
    mediaos_search_img_tests = ListField()
    mediaos_section_tests = ListField()
    mediaos_subsection_tests = ListField()
    mediaos_sponsor_tests = ListField()
    mediaos_upload_img_test = ListField()

class ReportGeneratorHandler(Resource):
    def get(self, report_id):
        report = Report.objects(report_id=report_id)
        return report.to_json()
    def put(self, report_id):
        report_data = json.loads(request.get_json())
        report = Report(report_id=report_id, title=report_data['title'], start_time=report_data['start_time'],duration=float(report_data['duration']), status=report_data['status'])
        report.save()
        return jsonify(report_data)

class TestAggregatorHandler(Resource):
    def put(self, report_id):
        pass


# Endpoint to generate/showing report.
api.add_resource(ReportGeneratorHandler, '/reporter/api/generate-report/<int:report_id>')
# Endpoint to add tests results (e.g. articles, galleries ... )
api.add_resource(TestAggregatorHandler, '/reporter/api/add-test/<int:report_id>')

# This is to run via Docker container.
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
