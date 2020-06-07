#!/bin/bash
cd api
export FLASK_APP=app.py
if test $# -eq 1
then
	flask db migrate -m "$1"
else
	flask db migrate
fi
