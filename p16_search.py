"""
Napište funkci, která má jako parametr hodnotu a uspořádaný seznam čísel.
Funkce vrátí první index ze seznamu, na kterém se nachází hledaná hodnota.

search(5, [1,1,1,2,2,3,5,6,8,9,10,12,15,20]) -> 6
search(7, [1,1,1,2,2,3,5,6,8,9,10,12,15,20]) -> -1
"""
from typing import List


def search(n: int, numbers: List[int]) -> int:
    for i in range(len(numbers)):
        if numbers[i] == n:
            return i
        if numbers[i] > n:
            return -1
    return -1


"""
Binary search:
[1, 1, 1, 2, 2, 3, 5, 6, 8, 9, 10, 12, 15, 20]
 D                 S                        H
                      D         S           H
                                     D  S   H
                                   

Hledám číslo 15:
Dolni = 12
Střed = 15
Horni = 20

Pokud je délka seznamu 1000000:
1. 1000000
2.  500000
3.  250000
4.  125000
5.   62500
6.   31250
7.   15625
8.    7813
9.    3907
10.   1954
11.    977
12.    489
13.    245
14.    123
15.     62
16.     31
17.     16
18.      8
19.      4
20.      2
21.      1
 
 0  1  2  3  4  5  6  7  8  9  10  11  12  13
[1, 1, 1, 2, 2, 3, 5, 6, 8, 9, 10, 12, 15, 20]
 S                 M                        E
                   S        M               E
                            S       M       E
                            S   M   E
                                S   E
n = 11
start = 10
end = 11
mid = 10
"""


def binary_search_iter(n: int, numbers: List[int]) -> int:
    start = 0
    end = len(numbers)-1

    while start < end - 1:
        mid = (start + end) // 2
        #print(f"start={start}, mid={mid}, end={end}, numbers[mid]={numbers[mid]}")

        if numbers[mid] == n:
            return mid

        if numbers[mid] > n:
            end = mid
        else:
            start = mid

    return -1


"""
           0  1  2  3  4  5  6  7  8  9  10  11  12  13
numbers = [1, 1, 1, 2, 2, 3, 5, 6, 8, 9, 10, 12, 15, 20]
           S                 M                        E
                             S        M               E
n = 9
S = 6
E = 13
M = 9
"""


def binary_search_rec(n: int, numbers: List[int], start: int = 0, end: int = None) -> int:
    if end is None:
        end = len(numbers) - 1

    if start >= end - 1:
        return -1

    mid = (start + end) // 2

    if numbers[mid] == n:
        return mid

    if numbers[mid] > n:
        return binary_search_rec(n, numbers, start=start, end=mid)

    return binary_search_rec(n, numbers, start=mid, end=end)


if __name__ == '__main__':
    print("search:")
    print(search(5, [1, 1, 1, 2, 2, 3, 5, 6, 8, 9, 10, 12, 15, 20]))
    print(search(7, [1, 1, 1, 2, 2, 3, 5, 6, 8, 9, 10, 12, 15, 20]))
    print("binary_search_iter:")
    print(binary_search_iter(5, [1, 1, 1, 2, 2, 3, 5, 6, 8, 9, 10, 12, 15, 20]))
    print(binary_search_iter(11, [1, 1, 1, 2, 2, 3, 5, 6, 8, 9, 10, 12, 15, 20]))
    print("binary_search_rec:")
    print(binary_search_rec(5, [1, 1, 1, 2, 2, 3, 5, 6, 8, 9, 10, 12, 15, 20]))
    print(binary_search_rec(11, [1, 1, 1, 2, 2, 3, 5, 6, 8, 9, 10, 12, 15, 20]))
