"""
Jak bys naprogramovala funkci - do které zadáš číslo -
a vrátí se seznam rozkladů onoho čísla na prvočísla.  3*5
"""

def prv(n):
    p = []
    delitel = 2
    while n > 1:
    # while n % delitel == 0:
        if n % delitel == 0:
            p.append(delitel)
            n //= delitel
        else:
            delitel +=1
    return p

n = int(input("zadej číslo: "))
print(prv(n))

