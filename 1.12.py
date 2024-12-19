categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

max_expenses = max(expenses)

# znajdujemy indeks maksymalnej kwoty w liście expenses
max_expense_index = expenses.index(max_expenses)

# uzyskujemy kategorie odpowiadającą maksymalnej kwocie
max_ex_category = categories[max_expense_index]

print(f"Najdroższa kategoria to '{max_ex_category}'!")