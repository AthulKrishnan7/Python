num = int(input("Enter the number :"))
number = num
count = 0
plus =0
while num > 0:
    rem = num % 10
    num = num // 10
    print(rem, num)
    count = count + 1
    plus = (plus * 10) + rem
print("Number of digits in ", number, " is ", plus)
