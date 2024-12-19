array = [2, 3, 4, 123, 56]
number = int(input("Wprowadź wartość: "))  
greater = [x for x in array if x > number]  
print(f"Elementy większe niż {number}:", greater)