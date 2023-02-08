from flask import Flask
import random
app = Flask(__name__)

random_num = random.randint(0, 9)
print(random_num)

@app.route('/')
def hello_World():
    return  '<h1>Guess a number between 0 and 9</h1>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<num>')
def guess(num):
    if int(num) > random_num:
        return '<h1>Too high, try again</h1>'
    elif int(num) < random_num:
        return '<h1> Too low, try again</h1>'
    else:
        return '<h1>You guessed correctly</h1>'

if __name__ == '__main__':
    app.run(debug=True)