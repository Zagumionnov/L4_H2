from flask import Flask
from flask import request
from flask import render_template
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()
f = Fernet(key)


# Take data using the request form and encrypt

@app.route('/encrypt/', methods=('GET', 'POST'))
def encrypt_page():

    if request.method == 'GET':
        return '<form method="POST"> <input name="string"> <input type="submit"></form>'

    string = request.form.get('string', 'none')
    if not string:
        return "None"
    token = f.encrypt(bytes(string, 'utf-8'))
    return render_template('index.html', crypt='Enrypted', string=token)

# Take token using the request form and decrypt

@app.route('/decrypt/', methods=('GET', 'POST'))
def decrypt_page():

    if request.method == 'GET':
        return '<form method="POST"> <input name="string"> <input type="submit"></form>'

    string = request.form.get('string', 'none')
    if not string:
        return "None"
    token = f.decrypt(bytes(string, 'utf-8'))
    return render_template('index.html', crypt='Derypted', string=token)


if __name__ == "__main__":
    app.run(debug=True)
