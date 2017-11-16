#!/usr/bin/env bash

rm -rf build dist &&

if [ "$1" = "debug" ]; then
    python -m PyInstaller scripts/build.spec
else
    # Use -O to set __debug__ to False
    python -O -m PyInstaller scripts/build.spec
fi  && iscc build.iss
