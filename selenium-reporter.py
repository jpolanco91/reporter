# Using bitnami/mongodb:latest image for MongoDB https://hub.docker.com/r/bitnami/mongodb/

from datetime import datetime
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from mongoengine import *
from bson.json_util import dumps
import json

# Creating our webservice (app)
app = Flask(__name__)

# We need to configure an IP since docker run on its separate network, so we need the static IP from host machine.
connect('selenium-reports', host='10.0.0.18', port=27017)

# App/Webservice config.
api = Api(app)

class Report(Document):
    report_id = IntField(db_field='id', unique=True)
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
        report = Report.objects(id=report_id)
        return dumps(report)
    def put(self, report_id):
        report_data = json.loads(request.get_json())
        report = Report(id=report_id, title=report_data['title'], start_time=report_data['start_time'],duration=float(report_data['duration']), status=report_data['status'])
        report.save()
        return jsonify(report_data)

class TestAggregatorHandler(Resource):
    def put(self, report_id):
        pass


# Endpoint to generate/showing report.
api.add_resource(ReportGeneratorHandler, '/reporter/api/generate-report/<int:report_id>')
# Endpoint to add tests results (e.g. articles, galleries ... )
api.add_resource(TestAggregatorHandler, '/reporter/api/add-test/<int:report_id>')
# report = {
#     'id': 1,
#     'title': 'Test report for Cosmopolitan SE',
#     'date': '2016-08-29',
#     'start_time':'20:41:47',
#     'duration':'0:02:51',
#     'status': 'Pass: 14, Failure: 2',
#     'article_tests': [
#         {'test_title':'ARTICLE - Checking if share buttons inside Article lead image works fine', 'status': 'Pass', 'error_msg':'', 'test_type':'article'},
#         {'test_title':'ARTICLE - Checking if the article is showing up published date', 'status': 'Pass', 'error_msg':'', 'test_type':'article'},
#         {'test_title':'ARTICLE - Checking if is showing up tags on top of an article', 'status':'Pass', 'error_msg':'', 'test_type':'article'},
#         {'test_title':'ARTICLE - Checking if sticky social buttons works fine', 'status':'Fail', 'error_msg':'', 'test_type':'article'}
#     ],
#     'gallery_tests': [],
#     'homepage_tests': [],
#     'mediaos-article_tests':[],
#     'mediaos-collection_tests':[],
#     'mediaos-login_tests':[],
#     'mediaos-search-content_tests':[],
#     'mediaos-search-img_tests':[],
#     'mediaos-section_tests':[],
#     'mediaos-subsection_tests':[],
#     'mediaos-sponsor_tests':[],
#     'mediaos-upload-img_test':[]
# }



# This is to run via Docker container.
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
