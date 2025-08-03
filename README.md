# studentscoremanagement_123
hello

📚 Student Score Management System
This is a menu-driven Python application designed to help school administrators manage student academic records. Each student is identified by a unique ID and has a name along with a list of test scores.

✅ Features:
Add New Student

Auto-generates a unique ID.

Adds a student with an empty score list.

Add Test Scores

Allows adding multiple scores to an existing student.

View Student Report

Displays name, all scores, highest, lowest, and average score.

Update Student Score

Update a specific score using its index.

Delete Student Record

Removes the student from the database by ID.

Exit

Ends the program.

🧠 Data Structure Used
Students are stored in a dictionary like this:

python
Copy
Edit
students = {
    "S1": {"name": "Alice", "scores": [85, 90, 78]},
    "S2": {"name": "Bob", "scores": [70, 88, 91]}
}
