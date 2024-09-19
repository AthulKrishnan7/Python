string = 'ABBcckdhsD'
lower = ''
upper= ''
for x in string:
    if x.islower():
        lower = lower+x
    else:
        upper = upper+x

print("Rearrageed case is "+lower+upper)