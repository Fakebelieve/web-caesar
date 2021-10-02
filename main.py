from flask import Flask, request
from caesar import rotate_string
app = Flask('app')

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            .error {
                color: red;
            }
        </style>
    </head>
    <body>
      <form action="/" method="POST">
        <label for="rot">Rotate by:
        <input type="text" name="rot" value="0" />
        <p class="error"></p>
        </label>
        <textarea name="text"></textarea>
        <input type="submit" value="Encrypt Text" />
      </form>
    </body>
</html>"""


@app.route('/')
def index():
    return form


@app.route('/')
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    encrypted_string = "<h1>" + rotate_string(text, rot) + "</h1>"
    return encrypted_string


app.run(host='0.0.0.0', port=8080)
