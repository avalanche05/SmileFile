from peewee import *

database = SqliteDatabase('main.sqlite')


class Patient(Model):
    id = AutoField(primary_key=True)
    name = CharField()
    contactDetails = CharField()
    lastAppointment = DateTimeField()

    class Meta:
        database = database


class Visit(Model):
    id = AutoField(primary_key=True)
    patient = ForeignKeyField(Patient, backref='visits')
    date = DateTimeField()
    diagnosis = CharField()
    treatment = CharField()

    class Meta:
        database = database
