imiona = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

# inicjalizujemy zmienną dla najdłuższego imienia
najdluzsze_imie = ""

for imie in imiona:
    if len(imie) > len(najdluzsze_imie):  # jesli aktualne imie jest dluzsze
        najdluzsze_imie = imie  

print(imiona)
print(f"Najdłuższe imię: {najdluzsze_imie}")
