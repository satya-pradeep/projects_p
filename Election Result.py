voters = int(input("Enter how many voters: "))
A = 0
B = 0
C = 0
for i in range(voters):
    choice =input("A/B/C: ")
    if choice == "A":
        A += 1
    elif choice == "B":
        B += 1
    elif choice == "C":
        C += 1
print("========= Election Result =========")
print()
print('candidate A: ',A)
print('candidate B: ',B)
print('candidate c: ',C)

if A>B and A>C:
    print("winner = A")
elif B>A and B>C:
    print("winner = B")
elif C>A and C>B:
    print("winner = c")
else:
    print("No clear winner")
