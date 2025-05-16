from student import Student

class StudentManagement:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        roll_no = student.get_roll_no()
        self.students[roll_no] = student
        print("Student added successfully!")

    def view_all(self):
        if not self.students:
            print("No student available.")
        for student in self.students.values():
            print(student)

    def update_student(self, roll_no, name=None, course=None, Grade=None):
        if roll_no in self.students:
            if name:
                self.students[roll_no].name = name
            if course:
                self.students[roll_no].course = course
            if Grade:
                self.students[roll_no].Grade = Grade
            print("Student updated.")
        else:
            print("Student not found.")

    def delete_student(self, roll_no):
        if roll_no in self.students:
            del self.students[roll_no]
            print("Record deleted.")
        else:
            print("Student data not found.")
