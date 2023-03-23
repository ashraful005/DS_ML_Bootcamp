number = float(input("Enter a number:"))
count = 0
digits = len(str(number))
if str(number)[-1] == '0':
    digits = digits-1

print("Number of digits are: ",digits-1)
