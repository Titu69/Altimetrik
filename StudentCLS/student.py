class Student:
    def __init__(self, roll_no, name, course, Grade):
        self.__roll_no = roll_no
        self.name = name
        self.course = course
        self.Grade = Grade

    def get_roll_no(self):
        return self.__roll_no

    def __str__(self):
        return f"Roll no: {self.__roll_no}, Name: {self.name}, Course: {self.course}, Grade: {self.Grade}"
