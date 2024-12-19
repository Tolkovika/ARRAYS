# funkcja porównująca dwie tablice
def porownaj(tab1, tab2):
    if len(tab1) != len(tab2):  # sprawdzamy długość tablic
        return False
    for i in range(len(tab1)):  # sprawdzamy każdy element
        if tab1[i] != tab2[i]:
            return False
    return True

tablica1 = ["woda", "ksiazka", "niebo"]
tablica2 = ["woda", "ksiazka", "niebo"]

print(tablica1)
print(tablica2)
print("Porównanie:", "Tablice są takie same" if porownaj(tablica1, tablica2) else "Tablice są różne")