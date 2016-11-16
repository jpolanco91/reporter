
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from models.report_model import Report
from mongoengine import connect
from bson.json_util import dumps
import json
import os

# Creating our webservice (app)
app = Flask(__name__)
service_hostname = os.environ.get('REPORTER_SERVICE_HOSTNAME')
connect('selenium-reports', host=service_hostname, port=27017)
api = Api(app)

class ReportGeneratorHandler(Resource):

    def get(self, report_id):
        report = Report.objects(report_id=report_id)
        return report.to_json()

    def put(self, report_id):
        report_data = request.get_json()

        #Get all keys from the report dictionary.
        report_keys = report_data.keys()

        #Creating report object with initial data.
        report = Report(report_id=report_id, title=report_data['title'], start_time=report_data['start_time'],
        	           duration=float(report_data['duration']), status=report_data['status'])

        #Creating new list for tests type keys.
        tests_keys = []

        #Add keys for every group of tests that were performed.
        for key in report_keys:
            if key.find("_tests"):
                report.__setattr__(key, report_data[key])

        # Saving report to db.
        report.save()
        return jsonify(report_data)


# Endpoint to generate/showing report.
api.add_resource(ReportGeneratorHandler, '/reporter/api/generate-report/<int:report_id>')

# This is to run via Docker container.
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
