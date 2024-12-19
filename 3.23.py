import mytext_3_23  

text = "An apple a day keeps the doctor away" 

num_words = mytext_3_23.word_count(text)  # Liczy słowa
print(f"Text: {text}")
print(f"Number of words: {num_words}")

longest_first = mytext_3_23.words_longest_first(text)  # Sortuje od najdłuższego
print(f"Words sorted from longest: {', '.join(longest_first)}")

alphabetical = mytext_3_23.words_alphabetically(text)  # Sortuje alfabetycznie
print(f"Words sorted alphabetically: {', '.join(alphabetical)}")