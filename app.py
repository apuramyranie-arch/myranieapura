
from flask import Flask, jsonify, request, send_from_directory
import os

app = Flask(__name__)


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/student")
def student():
    return jsonify({
        "student_id": "YOUR_STUDENT_ID",
        "name": "Myranie Apura",
        "program": "BSIT",
        "year": 3,
        "section": "A"
    })


@app.route("/hello")
def hello():
    name = request.args.get("name", "Student").strip()

    if not name:
        name = "Student"

    return jsonify({
        "message": f"Hello, {name}! Welcome to the Student API."
    })


@app.route("/course")
def course():
    return jsonify({
        "course_code": "BSIT",
        "course_name": (
            "Bachelor of Science in Information Technology"
        ),
        "department": "Information Technology"
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
