#!/usr/bin/env bash
python3 -m venv .venv &&
source .venv/bin/activate &&
pip install -r requirements.txt

cd vandelay_project &&
pip install -r requirements.txt &&
python3 manage.py tailwind install &&
python3 manage.py tailwind start &&
python3 manage.py runserver &&

# open the demo :)
open -a Chrome http://127.0.0.1:8000/vandelay_demo