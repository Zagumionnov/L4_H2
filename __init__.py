from flask import Flask
from flask import request
from flask import render_template
from cryptography.fernet import Fernet

app = Flask(__name__)


@app.route('/encrypt/', methods=('GET', 'POST'))
def encrypt_page():

    if request.method == 'GET':
        return '<form method="POST"> <input name="string"> <input type="submit"></form>'

    string = request.form['string']
    return render_template('index.html', crypt='Enrypted', string=string)


if __name__ == "__main__":
    app.run(debug=True)
