students = int(input("How many students: "))
print(students)
present = 0
absent = 0
for i in range(students):
    name = input("Enter student name: ")
    attendance = input("present/absent: ")
    if attendance == "present":
        present += 1
    else:
        absent += 1
        
attendance_percentage = (present / students)*100
print("========= Attendance Report =========")
print()
print("Total students       :",students)
print("present              :",present)
print("absent               :",absent)
print("attendance percentage:",attendance_percentage,"%")

    
