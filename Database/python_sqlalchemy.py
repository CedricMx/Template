# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 soovii
# Cedric, cedric_mx@163.com

''' Use sqlalchemy package to access to database '''

from sqlalchemy import MetaData, create_engine, Table
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy.sql import func
from sqlalchemy import and_, or_


# Database connection (Read-only access)
address = '192.168.8.119'
port = 3306
user = 'jwroot'
password = 'Soovii.jw123'
database = 'ftrack'

engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
	user, password, address, port, database), encoding='utf8', poolclass=NullPool, echo=False)

metadata = MetaData(engine)

class Db(object):

	def __init__(self):
		self.Session = sessionmaker()
		self.Session.configure(bind=engine)

	@property
	def session(self):
		return self.Session()

class ApiKey(object): pass
class Appointment(object): pass
class Asset(object): pass

api_key_table = Table('api_key', metadata, autoload=True)
appointment_table = Table('appointment', metadata, autoload=True)
asset_table = Table('asset', metadata, autoload=True)

mapper(ApiKey, api_key_table)
mapper(Appointment, appointment_table)
mapper(Asset, asset_table)


session = Db().Session()

keyid = session.query(ApiKey).filter_by(name='fauzi keys').first().keyid

session.flush()
session.close()

print(keyid)
