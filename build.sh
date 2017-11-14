#!/usr/bin/env bash

# Use -O to set __debug__ to False
rm -rf build dist && python -O -m PyInstaller scripts/build.spec
