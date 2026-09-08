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
status=[]
for i in range(len(marks)):
    if marks[i]>75:
        status.append("Pass")
    else:
        status.append("Fail")
print("Sr.no Name   Marks   Status")
for i,(name,mark,status1) in enumerate(zip(names,marks,status),start=1):
    print(f"{i}     {name}      {mark}      {status1}")