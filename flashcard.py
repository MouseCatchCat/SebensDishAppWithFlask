from flask import Flask, render_template, abort, jsonify, redirect, url_for, request
from datetime import datetime
from model import db, save_db


app = Flask(__name__)

count = 0


@app.route('/welcome')
def welcome():
    global count
    count += 1
    now = str(datetime.now())
    dishes = db
    return render_template("welcome.html", count=count, now=now, dishes=dishes)


@app.route('/dishes/<int:index>')
def dishes(index):
    try:
        dish = db[index]
        return render_template('dishes.html', dish=dish, index=index, max_index=len(db) - 1)
    except IndexError:
        abort(404)


# REST api, no need to serve html but show data directly, the url must be added api by the urls that already exist
@app.route('/api/welcome')
def show_dish_list():
    return jsonify(db)


@app.route('/api/dishes/<int:index>')
def show_dish_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)


@app.route('/add_dish', methods=["GET", "POST"])  # if you want to do the validation for user input, can use library
# call: Flask WTF
def add_card():
    if request.method == "POST":
        dish = {
            "name_en": request.form['name_en'],
            "name_nl": request.form['name_nl']
        }
        db.append(dish)
        save_db()
        return redirect(url_for('dishes', index=len(db) - 1))
    else:
        return render_template('add_dish.html')


@app.route('/remove_dish/<int:index>', methods=["GET", "POST"])
def remove_dish(index):
    try:
        if request.method == "POST":
            del db[index]
            save_db()
            return redirect(url_for('welcome'))
        else:
            return render_template('remove_dish.html', card=db[index])
    except IndexError:
        abort(404)
