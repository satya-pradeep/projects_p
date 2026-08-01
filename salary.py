employees = int(input("enter no of employees: "))


for i in range(employees):
    name = input("Enter Employee name: ")
    salary = int(input("Enter Basic salary: "))
    HRA = salary*(20/100)
    DA = salary*(15/100)
    TAX = salary*(5/100)
    Net_Salary = salary+HRA+DA-TAX
    print("========= Employee Salary Report =========")
    print()
    print("name: ",name)
    print("salary",salary)

    print("HRA  :",HRA)
    print("DA   :",DA)
    print("Tax  :",TAX)
    print("Net_salary: ",Net_Salary)



    
