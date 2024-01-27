#!/bin/sh
set -e

cd -- "$(dirname -- "$0")"

pip-sync ../requirements-dev.txt
pip install -r ../requirements-dev.txt