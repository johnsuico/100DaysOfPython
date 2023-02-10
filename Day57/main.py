from flask import Flask, render_template
import random, requests as req
from datetime import date as dt

app = Flask(__name__)

rand_num = random.randint(1, 10)

year = dt.today().year

# Ex 1
@app.route('/')
def home():
    return render_template('index.html', num=rand_num, year=year)

# Ex 2
@app.route('/guess/<name>')
def guess(name):
    gender_req = req.get(url=f"https://api.genderize.io/?name={name}")
    gender = gender_req.json()['gender']

    age_req = req.get(url=f"https://api.agify.io?name={name}")
    age = age_req.json()['age']

    return render_template('guess.html', name=name, gender=gender, age=age)


if __name__ == '__main__':
    app.run(debug=True)