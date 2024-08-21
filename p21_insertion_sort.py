from typing import List


def insertion_sort(unsorted: List[int]) -> List[int]:
    sorted_list = []
    for i in range(len(unsorted)):
        j = 0
        while j < len(sorted_list) and sorted_list[j] < unsorted[i]:
            j += 1
        sorted_list.insert(j, unsorted[i])
    return sorted_list


if __name__ == '__main__':
    my_numbers = [8, 4, 2, 5, 3, 1, 7, 2, 9, 14, 4, 2]
    print(insertion_sort(my_numbers))

    
# Jasně, pojďme si tento kód podrobně vysvětlit!
#
# ### Importování modulu
# ```python
# from typing import List
# ```
# Tento řádek importuje `List` z modulu `typing`, což nám umožňuje specifikovat typy seznamů v anotacích funkcí.
#
# ### Definice funkce `insertion_sort`
# ```python
# def insertion_sort(unsorted: List[int]) -> List[int]:
# ```
# Tato funkce přijímá seznam celých čísel (`unsorted`) a vrací seřazený seznam celých čísel (`List[int]`).
#
# ### Inicializace prázdného seznamu
# ```python
#     sorted_list = []
# ```
# Vytvoříme prázdný seznam `sorted_list`, do kterého budeme postupně vkládat prvky ze seznamu `unsorted` na správné místo.
#
# ### Hlavní cyklus
# ```python
#     for i in range(len(unsorted)):
# ```
# Tento cyklus prochází všechny prvky v seznamu `unsorted`.
#
# ### Vnitřní cyklus pro nalezení správné pozice
# ```python
#         j = 0
#         while j < len(sorted_list) and sorted_list[j] < unsorted[i]:
#             j += 1
# ```
# Tento cyklus hledá správnou pozici pro aktuální prvek `unsorted[i]` v již seřazeném seznamu `sorted_list`. `j` se zvyšuje, dokud nenajde prvek v `sorted_list`, který je větší nebo rovný `unsorted[i]`.
#
# ### Vložení prvku na správné místo
# ```python
#         sorted_list.insert(j, unsorted[i])
# ```
# Jakmile je nalezena správná pozice `j`, prvek `unsorted[i]` je vložen do `sorted_list` na tuto pozici.
#
# ### Vrácení seřazeného seznamu
# ```python
#     return sorted_list
# ```
# Po dokončení všech iterací hlavního cyklu je vrácen seřazený seznam `sorted_list`.
#
# ### Hlavní část programu
# ```python
# if __name__ == '__main__':
#     my_numbers = [8, 4, 2, 5, 3, 1, 7, 2, 9, 14, 4, 2]
#     print(insertion_sort(my_numbers))
# ```
# Tato část kódu se spustí pouze tehdy, když je skript spuštěn přímo. Vytvoří seznam `my_numbers` a vytiskne jeho seřazenou verzi pomocí funkce `insertion_sort`.
#
# Máš k tomu nějaké další otázky nebo potřebuješ něco upřesnit? 😊