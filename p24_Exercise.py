"""
Zadání: Chceme neuspořádaný seznam čísel uspořádat podle
absolutní hodnoty:
[2, -5, 3, -2, 2, 1, -1, -9, -7, 8] -> [-1, 1, -2, 2, 2, 3, -5, -7, 8, -9]
"""

# def abs_sort1(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if abs(arr[j]) > abs(arr[j + 1]):
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             return arr
#
#         numbers = [2, -5, 3, -2, 2, 1, -1, -9, -7, 8]
#         sorted_numbers = abs_sort1(numbers)
#         print(sorted_numbers)

def abs_sort(arr):
    return arr

if __name__ == "__main__":
    numbers = [2, -5, 3, -2, 2, 1, -1, -9, -7, 8]
    print(abs(numbers))
