from Src.Human import Human


class Professors(Human):
    def __init__(self, first_name, last_name, age, professor_id):
        super().__init__(first_name, last_name, age)
        self.professor_id = professor_id
        self.course_taught = []



    def select_course_to_teach(self, course):
        if len(self.courses_taught) < 3:
            self.courses_taught.append(course)

        else:
            raise ValueError("Professor can only teach up to 3 courses")
        


    def give_grade_to_student(self, student, grade):
        if not (0 <= grade <= 20):
            raise ValueError("Grade between 0 and 20")
        student.grades[self.selected_course] = grade
        