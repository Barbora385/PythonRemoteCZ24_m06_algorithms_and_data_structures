def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Posuneme prvky arr[0..i-1], které jsou větší než key, o jednu pozici doprava
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Testovací pole
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Seřazené pole je:", arr)