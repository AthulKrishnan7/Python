item = str(input("Enter the item = "))
price = str(input("Enter the price = "))

newstr = item+price
print(newstr)

diff = 25 - (len(item) + len(price))
print(diff)

final_str = item.ljust(diff,'.')
f_str = final_str+price
print(f_str)



