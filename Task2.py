''' Given the following two lists:
names = ["A", "B", "C", "D", "E"]
marks = [85, 72, 91, 64, 78]
* Write a Python program that displays each student's:
   * Serial number
   * Name
   * Marks
   * Pass/Fail status

* The program must demonstrate the use of:
    * range()
    * enumerate()
    * zip()
'''
names = ["A", "B", "C", "D", "E"]
marks = [85, 72, 91, 64, 78]
grade=[]
for i in range(len(marks)):
    if marks[i]>75:
        grade.append("Pass")
    else:
        grade.append("Fail")
print("Sr.no Name   Marks   Grades")
for i,(name,mark,grades) in enumerate(zip(names,marks,grade),start=1):
    print(f"{i}     {name}      {mark}      {grades}")