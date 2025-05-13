# Aimz API Scripts
This repo contains scripts to integrate with Aimz:
- https://app.aimz.no/graphql

## Getting Started

Requirements:
- python: https://www.python.org/downloads/

```shell
cd ./src

# Activate poetry environment
pip install poetry
poetry config virtualenvs.in-project true
# Set path to python if necessary with:
poetry env use /full/path/to/python
poetry install
poetry shell

# Set environment variables by copying .env -> private.env
# Then edit private.env, with f.ex TENANT=<my-organization>

# Get projects
python aimz/GetProjects.py
```
