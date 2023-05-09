# 1.	Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class and display the entire attribute and their values of the said class. Now remove the student_name attribute and display the entire attribute with values

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def set_class(self, student_class):
        self.student_class = student_class

    def display_attributes(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.student_name)
        print("Student Class:", self.student_class)

    def remove_name(self):
        del self.student_name

student1 = Student("S001", "John Doe")
student1.set_class("A")
student1.display_attributes()

# student1.remove_name()
# student1.display_attributes()