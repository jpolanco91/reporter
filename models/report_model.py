from datetime import datetime
from mongoengine import DynamicDocument
from mongoengine.fields import IntField, StringField, DateTimeField, FloatField


class Report(DynamicDocument):

    report_id = IntField(unique=True)
    title = StringField()
    date = DateTimeField(default=datetime.now)
    start_time = StringField()
    duration = FloatField()
    status = StringField()
