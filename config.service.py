#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  configuration
#  copy to "config.py"

MONGO_HOST = 'localhost'
MONGO_PORT = "27017"
MONGO_USER = None
MONGO_PASS = None
MONGO_DB = 'medhub'
MONGO_BUCKET = 'rxnorm'

USERDATA_SERVICEURI = 'http://localhost:18000/service.user'
USERDATA_SERVICEAUTH = ('basic', 'user:pass')
USERDATA_RETRIEVEPATH = 'demographics?token={token}'    # may contain "{token}" placeholder
USERDATA_RETRIEVEMETHOD = 'GET'

MEDSDATA_SERVICEURI = 'http://localhost:18000/service.meds'
MEDSDATA_SERVICEAUTH = ('basic', 'user:pass')
#MEDSDATA_SERVICEAUTH = ('token', 'saonxdosk')
MEDSDATA_RETRIEVEPATH = 'record/{token}'                # may contain "{token}" or "{record_id}" placeholder
MEDSDATA_RETRIEVEMETHOD = 'GET'
MEDSDATA_RETRIEVETYPE = 'pdo'
MEDSDATA_SENDPATH = 'record/{token}'                    # may contain "{token}" or "{record_id}" placeholder
MEDSDATA_SENDMETHOD = 'POST'
