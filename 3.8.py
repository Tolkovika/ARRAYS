# funkcja zwracająca ciąg gwiazdek
def gwiazdki(n):
    return "*" * n  # zwraca ciąg złożony z n gwiazdek

array = [2, 6, 4, 9, 7]

# wyświetlamy każdą wartość graficznie
for num in array:
    print(f"{num}: {gwiazdki(num)}")