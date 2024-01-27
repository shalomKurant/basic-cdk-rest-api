#!/bin/sh

set -e

cd -- "$(dirname -- "$0")"

export CUSTOM_COMPILE_COMMAND="$(basename $0)"
pip-compile --no-emit-index-url --no-header --allow-unsafe ../pyproject.toml -o ../requirements.txt "$@"
pip-compile --no-emit-index-url --no-header --allow-unsafe --extra=dev ../pyproject.toml -o ../requirements-dev.txt "$@"
