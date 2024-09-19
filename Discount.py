amount = int(input("Enter the total ammount :"))
if amount <=1000 :
    discount = (amount* 10/100)
elif amount >1000 and amount <= 5000:
    discount = (amount * 20 / 100)

elif amount >5000 and amount <=10000 :
    discount = amount * 30/100

elif amount >10000 :
    discount = amount * 50 / 100


disamount = amount - discount
print(amount)
print(discount)
print("Total amount", disamount)