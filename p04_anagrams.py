from typing import List
from collections import Counter


def anagrams(word: str, lst_of_words: List[str]) -> List[str]:
    counts = Counter(word)
    return [w for w in lst_of_words if Counter(w) == counts]

# word: řetězec, pro který hledáme anagramy.
    # lst_of_words: seznam řetězců, ve kterém hledáme anagramy.
    # Funkce vrací seznam řetězců, které jsou anagramy slova word.
#     Counter z modulu collections se používá k počítání výskytů jednotlivých znaků v řetězci.
    # List z modulu typing se používá pro typovou anotaci seznamu.
    # Počítání znaků:
    # counts = Counter(word) vytvoří slovník, kde klíče jsou znaky ze slova word a hodnoty jsou počty jejich výskytů.
    # Porovnání s ostatními slovy:
    # return [w for w in lst_of_words if Counter(w) == counts] prochází každý řetězec w v seznamu lst_of_words a porovnává jeho Counter s counts.
    # Pokud se počty znaků shodují, znamená to, že w je anagram slova word, a proto je přidán do výsledného seznamu.

# dopiš od Pavla Mrázka přes sorted
    def  anagrams(word: str, lst_of_words: List[str]) -> List[str]:
    sorted_word

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
# = > ['aabb', 'bbaa']

print(anagrams('kotel', ['lenoch', 'loket', 'vokel', 'akol', 'a']))
# = > ['loket']

print(anagrams('laser', ['lazing', 'lazy', 'lacer']))
# = > []

