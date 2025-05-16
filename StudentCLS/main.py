from student import Student
from management import StudentManagement

def main():
    system = StudentManagement()

    while True:
        print("\n___ Student Management System ___")
        print("1. Add Student \n2. View all students \n3. Update student data \n4. Delete student data \n5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            roll = input("Enter Roll No: ")
            name = input("Enter Name: ")
            course = input("Enter Course: ")
            Grade = input("Enter Grade: ")
            student = Student(roll, name, course, Grade)
            system.add_student(student)

        elif choice == '2':
            system.view_all()

        elif choice == '3':
            roll = input("Enter Roll No: ")
            name = input("Enter new name (or press enter to skip): ")
            course = input("Enter new course (or press enter to skip): ")
            Grade = input("Enter new grade (or press enter to skip): ")
            system.update_student(roll, name or None, course or None, Grade or None)

        elif choice == '4':
            roll = input("Enter Roll No to delete: ")
            system.delete_student(roll)

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("!!! Invalid option !!!")


if __name__ == "__main__":
    main()
