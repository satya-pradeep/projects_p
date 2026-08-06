#Student Marks Management System
students = int(input("Enter number of students: "))
f = 0
p = 0
t = 0
h_m = 0
l_m = 100
for i in range(students):
    name = input("Enter student name: ")
    marks = int(input("Marks out of 100: "))
    t += marks

    if h_m < marks:
        h_m = marks
    if l_m > marks:
        l_m = marks

    if marks < 35:
        f += 1
    elif marks >= 35 and marks <= 100:
        p += 1
avg = t/students

print("=====Student Marks=====")
print()
print("Pass students: ",p)
print("Fail students: ",f)
print("Highest Marks: ",h_m)
print("Lowest Marks : ",l_m)
print("Average",avg)
