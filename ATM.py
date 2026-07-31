balance=1000
while True:
    print("========= ATM =========")
    print(" 1. Check Balance")
    print(" 2. Deposit Money")
    print(" 3. Withdraw Money")
    print(" 4. Exit")

    choice = input("choose: ")


    if choice =="1":
         print("balance = $",balance)

    elif choice == "2":
        print(f"Your current balance is ${balance}")

        deposit=int(input("Enter amount to deposit:"))

        if deposit<=0:
            print("Invalid Deposit Amount")
        else:
            balance=deposit+balance
            print("Amount deposited successfully")
            print('current balance = $',balance)

    elif choice == "3":
        print(f"Your current balance is ${balance}")

        withdraw=int(input("Enter amount to withdraw: "))

        if withdraw<=0:
            print("Invalid Withdrawal Amount")

        elif withdraw>balance:
            print("Insufficient Balance")

        else:
            balance=balance-withdraw
            print("Please collect your cash.")
            print("Remaining Balance = $",balance)
    elif choice == "4":
        print("Thank you for using our ATM.")
        break
    else:
        print("invalid choice")
        
