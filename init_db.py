
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Francine Escultura - My API</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6fb;
            margin: 0;
            padding: 30px;
            color: #263238;
        }

        .container {
            max-width: 900px;
            margin: auto;
        }

        h1, h2 {
            color: #4f46a5;
        }

        .card {
            background: white;
            padding: 22px;
            margin: 18px 0;
            border-radius: 12px;
            box-shadow: 0 3px 12px #00000012;
        }

        button, input {
            padding: 10px 14px;
            margin: 5px 4px 5px 0;
            border-radius: 6px;
            border: 1px solid #ccc;
        }

        button {
            background: #5b50bd;
            color: white;
            cursor: pointer;
            border: none;
        }

        button:hover {
            background: #40368e;
        }

        .student {
            background: #f7f7ff;
            border-left: 4px solid #5b50bd;
            padding: 12px;
            margin: 10px 0;
            border-radius: 5px;
        }

        .error {
            color: #b91c1c;
        }
    </style>
</head>

<body>
<div class="container">

    <h1>Welcome to Francine Escultura's API!</h1>
    <p>BSIT - 3rd Year - Section 3B</p>

    <div class="card">
        <h2>Students from Database</h2>
        <button onclick="loadStudents()">Load All Students</button>
        <div id="studentList"></div>
    </div>

    <div class="card">
        <h2>Find Student by Database ID</h2>
        <input type="number" id="studentId" min="1"
               placeholder="Enter ID, e.g. 1">
        <button onclick="findStudent()">Find Student</button>
        <div id="singleStudent"></div>
    </div>

    <div class="card">
        <h2>Filter Students by Program</h2>
        <input type="text" id="program"
               placeholder="Enter BSIT or BSCS">
        <button onclick="filterProgram()">Search Program</button>
        <div id="programList"></div>
    </div>

</div>

<script>
    function displayStudents(data, elementId) {
        const container = document.getElementById(elementId);
        container.replaceChildren();

        if (!Array.isArray(data) || data.length === 0) {
            container.textContent = "No student records found.";
            return;
        }

        data.forEach(student => {
            const card = document.createElement("div");
            card.className = "student";

            const title = document.createElement("strong");
            title.textContent =
                student.student_id + " - " + student.name;

            const details = document.createElement("p");
            details.textContent =
                student.program + " | Year " + student.year +
                " | Section " + student.section;

            card.append(title, details);
            container.appendChild(card);
        });
    }

    async function loadStudents() {
        try {
            const response = await fetch("/students");
            if (!response.ok) throw new Error("Request failed");

            const data = await response.json();
            displayStudents(data, "studentList");
        } catch (error) {
            document.getElementById("studentList").textContent =
                "Unable to retrieve student records.";
        }
    }

    async function findStudent() {
        const id = document.getElementById("studentId").value;
        const output = document.getElementById("singleStudent");

        if (!id || Number(id) < 1) {
            output.textContent = "Please enter a valid database ID.";
            return;
        }

        try {
            const response = await fetch("/students/" + Number(id));
            const data = await response.json();

            if (!response.ok) {
                output.textContent = data.error || "Student not found.";
                return;
            }

            displayStudents([data], "singleStudent");
        } catch (error) {
            output.textContent = "Unable to retrieve student.";
        }
    }

    async function filterProgram() {
        const program = document.getElementById("program").value.trim();
        const output = document.getElementById("programList");

        if (!program) {
            output.textContent = "Please enter a program.";
            return;
        }

        try {
            const response = await fetch(
                "/students/program/" + encodeURIComponent(program)
            );

            if (!response.ok) throw new Error("Request failed");

            const data = await response.json();
            displayStudents(data, "programList");
        } catch (error) {
            output.textContent = "Unable to retrieve student records.";
        }
    }
</script>
</body>
</html>
