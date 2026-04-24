import json
import os

FILE_NAME = "students.json"

# Load existing data
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save data
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

students = load_students()

while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # ADD
    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter age: ")
        course = input("Enter course: ")

        student = {
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)
        save_students(students)
        print("✅ Student added successfully!")

    # VIEW
    elif choice == "2":
        if not students:
            print("❌ No students found.")
        else:
            print("\n📋 Student List:")
            for i, s in enumerate(students):
                print(f"{i+1}. Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")

    # DELETE
    elif choice == "3":
        if not students:
            print("❌ No students to delete.")
        else:
            for i, s in enumerate(students):
                print(f"{i+1}. {s['name']}")

            try:
                num = int(input("Enter number to delete: "))
                if 0 < num <= len(students):
                    removed = students.pop(num - 1)
                    save_students(students)
                    print(f"🗑️ Deleted: {removed['name']}")
                else:
                    print("❌ Invalid number")
            except:
                print("❌ Enter a valid number")

    # EXIT
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("❌ Invalid choice, try again.")