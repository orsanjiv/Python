class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def set_class(self, student_class):
        self.student_class = student_class

    def display_attributes(self):
        print("Student ID:", self.student_id)
        if hasattr(self, 'student_name'):
            print("Student Name:", self.student_name)
        print("Student Class:", self.student_class)

    def remove_name(self):
        del self.student_name

# Create a new Student object
student1 = Student("S001", "John Doe")

# Set the student_class attribute
student1.set_class("A")

# Display all the attributes
student1.display_attributes()

# Remove the student_name attribute
student1.remove_name()

# Display all the attributes again
student1.display_attributes()
