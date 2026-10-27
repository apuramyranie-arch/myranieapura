
import sqlite3
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return render_template("index.html")


# Existing student information
@app.route("/student")
def get_student():
    return jsonify({
        "student_id": "23-0006",
        "name": "Francine Escultura",
        "program": "BSIT",
        "year": 3,
        "section": "3B"
    })


@app.route("/hello")
def say_hello():
    name = request.args.get("name", "Student")
    return jsonify({"message": f"Hello, {name}!"})


@app.route("/hobbies")
def get_hobbies():
    hobbies = [
        "Listening to music",
        "Watching movies",
        "Learning programming"
    ]
    return jsonify({
        "hobbies": hobbies,
        "total_hobbies": len(hobbies)
    })


# Return all students from SQLite
@app.route("/students")
def get_students():
    conn = get_db_connection()
    students = conn.execute(
        "SELECT * FROM students ORDER BY id"
    ).fetchall()
    conn.close()

    return jsonify([dict(student) for student in students])


# Return one student using the database ID
@app.route("/students/<int:id>")
def get_student_by_id(id):
    conn = get_db_connection()
    student = conn.execute(
        "SELECT * FROM students WHERE id = ?", (id,)
    ).fetchone()
    conn.close()

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(dict(student))


# Additional endpoint: filter students by program
@app.route("/students/program/<program>")
def get_students_by_program(program):
    conn = get_db_connection()
    students = conn.execute(
        "SELECT * FROM students WHERE program = ? ORDER BY id",
        (program,)
    ).fetchall()
    conn.close()

    return jsonify([dict(student) for student in students])


if __name__ == "__main__":
    app.run(debug=True)
