from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('greet.html', placeholder=name)
    return render_template('index.html')


# @app.route('/greet', methods=['POST'])
# def greet():
    # name = request.args.get('name', 'World')  # for GET requests
    # name = request.form.get('name', 'World')  # for POST requests
    # return render_template('greet.html', placeholder=name)
