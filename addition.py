num = 1
sum = 0
print("Enter number for sum, enter 0 to exit")
while num != 0:
    num = int(input("Enter Number: "))
    sum = sum + num
    print("Current Sum: ", sum)
else:
    print("You have exited out from the operation.")