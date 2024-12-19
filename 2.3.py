# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# total koszty na kategorie 
total_food = sum(week[0] for week in monthly_expenses)
total_transport = sum(week[1] for week in monthly_expenses)
total_utilities = sum(week[2] for week in monthly_expenses)

# total koszty weekly
total_week_1 = sum(monthly_expenses[0])
total_week_2 = sum(monthly_expenses[1])
total_week_3 = sum(monthly_expenses[2])
total_week_4 = sum(monthly_expenses[3])

# total koszty
total_month = total_food + total_transport + total_utilities

print('MONTHLY EXPENSES')
print('----------------')
print('Food:', total_food)
print('Transport:', total_transport)
print('Utilities:', total_utilities)
print('Week 1:', total_week_1)
print('Week 2:', total_week_2)
print('Week 3:', total_week_3)
print('Week 4:', total_week_4)
print('---------------')
print('TOTAL:', total_month)
