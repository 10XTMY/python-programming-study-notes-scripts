from flask import Flask, render_template, request, redirect


app = Flask(__name__)

# WARNING: below should be stored in a database
REGISTRANTS = {}
SPORTS = ['baseball', 'basketball', 'football', 'hockey']


@app.route('/')
def index():
    return render_template('index.html', sports=SPORTS)


@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    sport = request.form.get('sport')

    if not name:
        return render_template('failure.html', message='Name is required')

    if not sport:
        return render_template('failure.html', message='Sport is required')
    if sport not in SPORTS:
        return render_template('failure.html', message='Invalid sport')

    REGISTRANTS[name] = sport

    return redirect('/registrants')


@app.route('/registrants')
def registrants():
    return render_template('registrants.html', registrants=REGISTRANTS)
