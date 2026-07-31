# Restaurant Ordering System
pizza = 12
burger = 6
fries = 4
coke = 2
t = 0
c_p = 0
c_b = 0
c_f = 0
c_c = 0
while True:
        
    print("========= MENU =========")
    print()
    print("1. Pizza   - $12")
    print("2. Burger  - $6")
    print("3. Fries   - $4")
    print("4. Coke    - $2")
    print("5. Exit / Finish Order")
    choice = input("enter your order: ")
    if choice == "1":
        t += 12
        print("pizza add to your order")
        c_p += 1
    elif choice == "2":
        t += 6
        print("burger add to your order")
        c_b += 1
    elif choice == "3":
        t += 4
        print("fries add to your order")
        c_f += 1
    elif choice == "4":
        t += 2
        print("coke add to your order")
        c_c += 1
    elif choice == "5":
        print("Exit / Finish Order")
        break
    else:
        print("Invalid Choice")

print("========= BILL =========")
print()
print("Pizza: ",c_p)
print("Burger: ",c_b)
print("Fries: ",c_f)
print("Coke: ",c_c)
print("Total: ",t)
