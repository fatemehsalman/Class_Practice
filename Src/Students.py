from Src.Human import Human

class Students(Human):
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id
        self.selected_course = None
        self.grades = {}

    def select_course(self, course):
        if self.selected_course is None:
            self.selected_course = course
        else:
            raise ValueError("Student can only select one course")
        

    def calculate_grade(self):
        if not self.grades:
            raise ValueError("No grades available")

        average = sum(self.grades.values()) / len(self.grades)

        if average >= 12:
            return "Pass"
        else:
            return "Fail"    
    





        


    