''' Student Management System 
Create a Student Management System.
Requirements:
* Create a Student class.
* Attributes: student_id, name, age, course, marks.
* Create methods to:
    * Add student
    * Display student details
    * Calculate percentage
    * Check pass/fail
* Create multiple student objects.
* Store student details in a text file.
* Read and display all students from the file.
'''

class Student:
    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def add(self):
        file_exist=False
        with open("info.txt","r") as f:
            if f.read().strip() != "":
                file_exist=True
        with open("info.txt","a") as f:
            if not file_exist:
                f.write(f"{'SId':<10}{'Name':<15}{'Age':<10}{'Course':<15}{'Marks':<5}\n")
                f.write("-"*55+"\n")    
            f.write(f"{self.student_id:<10}{self.name:<15}{self.age:<10}{self.course:<15}{self.marks:<5}\n")
        print("\nStudent added successfully\n")

    def display(self):
        print("\nStudents Details:")
        with open("info.txt","r") as f:
            data=f.read()
            print(data)

    def percentage(self):
        print("\nCalculate Percentage")
        search_id=input("Enter student to calculate perecenatge: ")
        with open("info.txt","r") as f:
            data=f.readlines()
            for line in data[2:]:
                student_id,name,age,course,marks=line.split()
                if student_id==search_id:
                    perc=(int(marks))
                    print(f"\nStudent {name} has a percentage of {perc:.2f}%\n")
                    return
            print("\nStudent not found.\n")

    def status(self):
        print("\nCheck Pass/Fail Status")
        search_id=input("Enter student to check status: ")
        with open("info.txt","r") as f:
            data=f.readlines()
            for line in data[2:]:
                student_id,name,age,course,marks=line.split()
                if student_id==search_id:
                    if int(marks)>40:
                        print(f"\nStudent {name} has passed.\n")
                    else:
                        print(f"\nStudent {name} has failed.\n")
                    return
            print("\nStudent not found.\n")

open("info.txt", "a").close()
choice=1
while choice!=0:
    print("Student Management System")
    print("1. Add Student")
    print("2. Display Student Details")
    print("3. Calculate Percentage")
    print("4. Check Pass/Fail Status")
    print("0. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        student_id=input("Enter student id: ")
        name=input("Enter student name: ")
        age=int(input("Enter studnet age: "))
        course=input("Enter student course: ")
        marks=input("Enter student marks: ")
        student=Student(student_id,name,age,course,marks)
        student.add()
    elif choice==2:
        student=Student(None, None, None, None, None)
        student.display()
    elif choice==3:
        student=Student(None, None, None, None, None)
        student.percentage()
    elif choice==4:
        student=Student(None, None, None, None, None)
        student.status()
    elif choice==0:
        print("Exit")
        break
