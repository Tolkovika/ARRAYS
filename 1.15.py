# Ceny produktów w sklepie komputerowym (w jednostkach waluty)
car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]

# Procedura sortowania bąbelkowego
def bubble_sort(arr):
    n = len(arr)  # ustalamy długość listy
    for i in range(n-1):  # zewnętrzna pętla iterująca po liście
        for j in range(n-i-1):  # wewnętrzna pętla porównująca sąsiednie elementy
            if arr[j] > arr[j+1]:  # jeśli  arr[j] > arr[j+1] zamiana miejsc
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# sortowanie bąbelkowe dla zużycia paliwa
print("Oryginalne zużycie paliwa:", car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)
print("Posortowane zużycie paliwa:", sorted_car_fuel_consumption)

# dla transakcjii bankowych
print("Oryginalne transakcje bankowe:", bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions)
print("Posortowane transakcje bankowe:", sorted_bank_transactions)
