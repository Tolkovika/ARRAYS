def word_count(text):
    words = text.split()  # Dzieli tekst na słowa
    return len(words)  # Zwraca liczbę słów

def words_longest_first(text):
    words = text.split()  # Dzieli tekst na słowa
    return sorted(words, key=len, reverse=True)  # Sortuje od najdłuższego do najkrótszego

def words_alphabetically(text):
    words = text.split()  # Dzieli tekst na słowa
    return sorted(words)  # Sortuje alfabetycznie
