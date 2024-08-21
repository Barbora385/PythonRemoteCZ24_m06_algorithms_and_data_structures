"""
Uspořádáme seznam celých čísel tak,
že nejprve budou všechna lichá čísla (uspořádaná podle velikosti)
a následně všechna sudá čísla (uspořádaná podle velikosti).
[5, 3, 4, 2, -6, 7, -7, 8, 1, 2] -> [-7, 1, 3, 5, 7, -6, 2, 2, 4, 8]
"""

def odd_even_bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def sort_odd_even(arr):
    odd_numbers = [x for x in arr if x % 2 != 0]
    even_numbers = [x for x in arr if x % 2 == 0]

    print(odd_numbers)
    print(even_numbers)

    # Seřadím lichá a sudá čísla pomocí bublin
    sorted_odd_numbers = odd_even_bubblesort(odd_numbers)
    sorted_even_numbers = odd_even_bubblesort(even_numbers)

    print(odd_numbers)
    print(even_numbers)

    # Spojím seřazené liché a sudé seznamy
    return sorted_odd_numbers + sorted_even_numbers

numbers = [5, 3, 4, 2, -6, 7, -7, 8, 1, 2]
sorted_numbers = sort_odd_even(numbers)
print(sorted_numbers)

