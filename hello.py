from flask import Flask, render_template
app: Flask = Flask(__name__)

@app.route('/Hello')
def hello() -> str:
    return "Hello world! This is Flask!"

app.run(debug=True)