# Welcome to Vivid AI Service

## Why?

Integrate best of AI frameworks available today. So that we can make use of such technologies within your application ecosystem.

## How?

A micro-service written in python flask to utilize one of the latest AI frameworks such as `langchain`.

## Setup

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
# to maintain latest requirements run:
pip install -U -r requirements.txt

```
Create a `.env` file for your local setup.

Run the application

```sh
python app.py

# alternatively
FLASK_CONFIG=config.DevelopmentConfig FLASK_APP=app.py flask run
```

## References

* [langchain github page](https://github.com/hwchase17/langchain)
* [flask github page](https://github.com/pallets/flask/)
