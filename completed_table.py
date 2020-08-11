from flask import Flask, render_template
import sqlite3
from typing import Dict

DB_FILE: str = 'Homework11_DB'

app: Flask = Flask(__name__)

@app.route('/completed')
def completed_courses() -> str:
    query = """select s.cwid s.name, s.major, count(*) as Complete from students as s join grades as g on s.cwid=g.studentcwid group by s.name order by s.name"""

    db: sqlite3.Connection = sqlite3.connect(DB_FILE)

    #this converts the results from the query in line#11 to a list of dictionaries to pass to the template
    data: Dict[str, str] = [{"cwid": cwid, "name": name, "major": major, "complete": complete}
        for cwid, name, major, complete in db.execute(query)]
    db.close() #closes the connection

    return render_template('student_grade_table.html',
                            title="My Stevens Repository",
                            table_title="Number of Completed Courses By Student Name")
app.run(debug=True)
