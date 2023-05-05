class Student:
    def stu_detail(self,name,uid,section):
        self.name = name
        self.uid = uid
        self.section = section

    def disply_detail(self):
         print(self.name)
         print(self.uid)
         print(self.section)
class Student1:
    def stu_multi(self,branch):
        self.branch = branch
    def display_multi(self):
        print(self.branch)


class Student2(Student):
    def stu_group(self,group):
        self.group = group;
    def display_group(self):
        print(self.group)

class Student3(Student2):
    def stu_group(self,cgpa):
        self.cgpa = cgpa;
    def display_group(self):
        print(self.cgpa)

# multiple inheritence
# class Student5(Student,Student1):
#     print("multiple inheritance")


# consturctor (intitialize using init keyword)

class Student7():
    def __init__(self):
        self.student = "Abhi"
    def print_abhi(self):
        print(self.student)    
                 


# obj1 = Student()
# obj1.stu_detail("sanjiv","21BCS3478",611)
# obj1.disply_detail()  
      
# obj2 = Student2()
# obj2.stu_detail("sanjiv","21bcs3478",611);
# obj2.disply_detail()

# obj3 = Student3()
# obj3.stu_group("A")
# obj3.display_group()

obj = Student7()
obj.print_abhi()


