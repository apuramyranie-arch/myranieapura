
import sqlite3
from pathlib import Path
from flask import Flask, jsonify, render_template, send_file

app = Flask(__name__)

# Database connection
BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / 'students.db'


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Home page
@app.route('/')
def home():
    template_file = BASE_DIR / 'templates' / 'index.html'

    if template_file.exists():
        return render_template('index.html')

    return send_file(BASE_DIR / 'index.html')


# API: Get all students
@app.route('/students')
def get_students():
    conn = get_db_connection()

    students = conn.execute(
        'SELECT * FROM students'
    ).fetchall()

    conn.close()

    return jsonify([dict(student) for student in students])


# API: Get one student by ID
@app.route('/students/<int:id>')
def get_student_by_id(id):
    conn = get_db_connection()

    student = conn.execute(
        'SELECT * FROM students WHERE id = ?',
        (id,)
    ).fetchone()

    conn.close()

    if student is None:
        return jsonify({
            "error": "Student not found"
        }), 404

    return jsonify(dict(student))


# Additional API: Get students by program
@app.route('/students/program/<program>')
def get_students_by_program(program):
    conn = get_db_connection()

    students = conn.execute(
        'SELECT * FROM students WHERE LOWER(program) = LOWER(?)',
        (program,)
    ).fetchall()

    conn.close()

    return jsonify([dict(student) for student in students])


# Run Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
