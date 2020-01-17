"""
In real website, should not put the data in a json file since it won't work for multiple uses. Instead,
Use a real database layer like:
https://flask-sqlalchemy.palletsprojects.com/
"""

import json


def load_db():
    with open("dishes_db.json") as f:
        return json.load(f)


def save_db():
    with open('dishes_db.json', 'w') as f:
        return json.dump(db, f)


db = load_db()
