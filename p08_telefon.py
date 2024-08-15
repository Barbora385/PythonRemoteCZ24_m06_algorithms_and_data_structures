# Napište funkci, která přijme seznam 12 celých čísel a vrátí řetězec ve formátu telefonního čísla.#
# Struktura funkce by měla vypadat takto:

from typing import List


def create_phone_number(n: List[int]) -> str:
    return f"(+{n[0]}{n[1]}) {n[2]}{n[3]}{n[4]}-{n[5]}{n[6]}{n[7]}-{n[8]}{n[9]}{n[10]}"


    pass



# Algoritmus by měl fungovat následovně:

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]))
## => returns "(+12) 345-678-901"###