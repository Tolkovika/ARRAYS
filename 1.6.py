def weekday(n):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    if n >= 1 and n <= 7:
        return days[n - 1]
    else:
        return "Invalid day number"
print(weekday(1))  #  Monday
print(weekday(7))  #  Sunday
print(weekday(4))  #  Thursday