from flask import Flask, render_template

app: Flask = Flask(__name__)

@app.route('/Hello')
def hello() -> str:
    return "Hello world! This is Flask!"

@app.route('/Goodbye')
def see_ya() -> str:
    return "See you later!"

@app.route("/student_grade_table")
def template_demo() -> str:
    return render_template('/student_grade_table.html',
                            my_header="My Stevens Repository",
                            my_param="My custom parameter")
app.run(debug=True)