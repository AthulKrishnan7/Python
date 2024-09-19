Working_hours_lst = []

for i in range(0, 2):
    print("Enter Salary of " + str(i+1) + "Day =")
    hours = int(input())
    Working_hours_lst.append(hours)

print(Working_hours_lst)

EachDaySalary = int(input("Enter the day salary"))
total_hours_week = sum(Working_hours_lst)

Total_salary = total_hours_week* EachDaySalary
print("Total day salay is "+ str(Total_salary))

