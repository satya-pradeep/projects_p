def banking():
    while True:
        print('========= BANK =========')
        print()
        print('1. Create Account')
        print('2. Deposit Money')
        print('3. Withdraw Money')
        print('4. Check Balance')
        print('5. Display All Accounts')
        print('6. Exit')

        choose = input("enter your choice: ")

        if choose == '1':
            print("=====Create Account=====")
            account_number = input("Enter Account Number: ")
            customer_name = input("Enter Customer Name: ")
            initial_deposit = int(input("Enter Initial Deposit: "))
        
            if initial_deposit <= 0:
                print("Enter valid amount")
            else:

                with open("pradeep", "a") as p:
                    p.write(f'{account_number},{customer_name},{initial_deposit}\n')

                print("Account created successfully.")

        elif choose == '2':
            print("=====Deposit Money=====")
            account_number = input("Enter Account Number: ")
            deposit_amount = int(input("Enter Deposit Amount: "))
            if deposit_amount <= 0:
                print("Enter valid amount")
            else:

                updated_data = []
                found = False

                with open("pradeep", "r") as p:
                    for line in p:
                        line = line.strip()
                        acc_no, name, balance = line.split(",")

                        if acc_no == account_number:
                            balance = int(balance)
                            balance = balance + deposit_amount
                            found = True

                        updated_data.append(f"{acc_no},{name},{balance}\n")

                if found:
                    with open("pradeep", "w") as p:
                        p.writelines(updated_data)

                    print("Deposit successful.")
                    
                else:
                    print("Account Not Found.")

        elif choose == '3':
            print("=====Withdraw Money=====")
            account_number = input("Enter Account Number: ")
            withdraw_amount = int(input("Enter Withdrawal Amount: "))
            if withdraw_amount <= 0:
                print("Enter valid amount")
            else:

                update_data = []
                found = False
                success = False

                with open("pradeep", "r") as p:
                    for line in p:
                        line = line.strip()
                        acc_no, name, balance = line.split(",")

                        if acc_no == account_number:
                            found = True
                            balance = int(balance)

                            if balance >= withdraw_amount:
                                balance = balance - withdraw_amount
                                success = True
                            else:
                                print("Insufficient Balance")

                        update_data.append(f"{acc_no},{name},{balance}\n")

                if found and success:
                    with open("pradeep", "w") as p:
                        p.writelines(update_data)

                    print("Withdraw successful.")
                    

                elif not found:
                    print("Account Not Found.")

        elif choose == '4':
            print("=====Check Balance=====")
            account_number = input("Enter Account Number: ")

            found = False

            with open("pradeep", "r") as p:
                for line in p:
                    line = line.strip()
                    acc_no, name, balance = line.split(",")

                    if acc_no == account_number:
                        print("Name   :", name)
                        print("Balance:", balance)
                        found = True
                        break

            if not found:
                print("Account Not Found.")

        elif choose == "5":
            print("=====Display All Accounts=====")
            print()

            with open("pradeep", "r") as p:
                print(p.read())

        elif choose == "6":
            print("Thank you for using our Bank System.")
            break

        else:
            print("Invalid Choice.")

open("pradeep", "a").close()
banking()
