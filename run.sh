#!/usr/bin/env bash

cd scripts; python ./setup.py build_ui; cd ..; python ./app/app.py
