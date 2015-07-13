#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  App settings
#  copy to "config.py"

DEBUG = True
ONLY_BASIC_REVIEW = True
IGNORE_REVIEW_CONCLUSION_ERRORS = True		# if true ignores status == 400 (not all 400) raised when sending concluded meds

SESSION_SECRET = "use-your-own"
API_SERVER_BASE = "http://127.0.0.1:18000"

FHIR_TEMPLATE_NAME = 'FHIR-medicationstatement-0.5.0.5149-contained.json'

PILLBOX_API_KEY = None
