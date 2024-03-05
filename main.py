from Src.Human import Human
from Src.Professors import Professors
from Src.Students import Students
from Src.write_file import save_data
from Src.read_file import load_data

def main():
    data = load_data()
    print("Menu:")
    print("1. Add student")
    print("2. Add professor")
    print("3. Select course for student")
    print("4. Select course to teach for professor")
    print("5. Give grade to student")
    print("6. Save data and exit")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
            age = int(input("Enter student's age: "))
            student_id = int(input("Enter student's ID: "))
            student = Students(first_name, last_name, age, student_id)
            data["students"].append(student.__dict__)
        elif choice == "2":
            first_name = input("Enter professor's first name: ")
            last_name = input("Enter professor's last name: ")
            age = int(input("Enter professor's age: "))
            professor_id = int(input("Enter professor's ID: "))
            professor = Professors(first_name, last_name, age, professor_id)
            data["professors"].append(professor.__dict__)
        elif choice == "3":
            student_id = int(input("Enter student's ID: "))
            course = input("Enter course name: ")
            for student in data["students"]:
                if student["student_id"] == student_id:
                    student_obj = Students(student["first_name"], student["last_name"], student["age"], student["student_id"])
                    student_obj.select_course(course)
                    break
        elif choice == "4":
            professor_id = int(input("Enter professor's ID: "))
            course = input("Enter course name: ")
            for professor in data["professors"]:
                if professor["professor_id"] == professor_id:
                    professor_obj = Professors(professor["first_name"], professor["last_name"], professor["age"], professor["professor_id"])
                    professor_obj.select_course_to_teach(course)
                    break
        elif choice == "5":
            student_id = int(input("Enter student's ID: "))
            grade = int(input("Enter grade: "))
            for student in data["students"]:
                if student["student_id"] == student_id:
                    student_obj = Students(student["first_name"], student["last_name"], student["age"], student["student_id"])
                    student_obj.give_grade_to_student(student_obj, grade)
                    break
        elif choice == "6":
            save_data(data)
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()