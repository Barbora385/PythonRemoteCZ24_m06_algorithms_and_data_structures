def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        print(arr)
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            return arr
    return arr

arr = [8, 4, 3, 9, 2, 1]
bubble_sort(arr)
print("setříděný seznam buuble technikou je: ", arr)


# takže porovná index 0 a index 0+1, tzn. 1
# potom porovná 1 s 2 ... potom 5 s 6 ... ok, keď jasné :)
# Tomáš Jaško
# 20:17
# Pavel, môžeš nakopírovať:
#
# if __name__ == "__main__":
#     arr = [8, 4, 2, 5, 3, 1, 7, 2, 9]
#     print(buble_sort(arr))
