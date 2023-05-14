class Student:
 def __init__(self, student_id, student_name):
  self.student_id = student_id
  self.student_name = student_name

 def add_class(self, student_class):
  self.student_class = student_class

 def display_attributes(self):
  attributes = vars(self)
  print("Attributes and their values:")
  for attr, value in attributes.items():
   print(attr, ":", value)

 def remove_name(self):
  del self.student_name

student = Student("80008", "Anjali")
student.add_class("4th Sem")
student.display_attributes()
print("After removing student_name attribute:")
student.remove_name()
student.display_attributes()