#!/usr/bin/env bash

cd scripts; ./setup.py build_ui; cd ..;

if [ "$1" = "debug" ]; then
    python app/app.py
else
    # Use -O to set __debug__ to False
    python -O app/app.py
fi
