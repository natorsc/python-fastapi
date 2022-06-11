#!/bin/bash

poetry run uvicorn v1.main:app \
--host='127.0.0.1' \
--port='8000' \
--reload