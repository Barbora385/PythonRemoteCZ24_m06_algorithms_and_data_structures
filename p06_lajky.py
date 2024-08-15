from typing import List


def likes(names: List[str]) -> str:
    if len(names) == 0:
        return "nikdo to nelajkoval"
    if len(names) == 1:
        return f"{names[0]} to olajkoval"
    if len(names) == 2:
        return f"{names[0]} a {names[1]} to lajkovali"
    if len(names) == 3:
        return f"{names[0]} a {names[1]} a {names[2]} to lajkovali"
    if len(names) >= 4 :
        return f"{names[0]}, {names[1]}, {names[2]} a další to lajkovali"


if __name__ == "__main__":
    list_of_likes = [[],["Petr"], ["petr","Anna"] , ["Petr", "Ana", "Marek"], ["Petr", "Ana", "Marek", "Ola"]]


