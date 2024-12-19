def occurs(number, array): #occurs sprawdza czy dana liczba znajduje się w array
    return number in array

array = [15, 38, 7, 23, 14]
number = int(input("Wprowadź liczbę: "))
print(f"Liczba {number} występuje w tablicy" if occurs(number, array) else "Liczba nie występuje.")