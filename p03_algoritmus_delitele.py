a = int(input("Zadej hodnotu a: "))
b = int(input("Zadej hodnotu b: "))
def gcd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print(f"Největší společný dělitel je: {a} a {b} je {gcd(a,b)}")

def gcd2(a,b):
    n = min(a,b)
    for i in range(n,0,-1):
        if a % i == 0 and b % i == 0:
            return i

print(f"Největší společný dělitel je: {a} a {b} je {gcd(a,b)}")


def gcd3(a,b):
    while b!=0:
        a,b = b, a % b
    return a

print(f"Největší společný dělitel je: {a} a {b} je {gcd(a,b)}")

# rekurzivní
def nsd(a, b):
    return a if b == 0 else nsd(b, a % b)
print(f"Největší společný dělitel je: {a} a {b} je {gcd(a,b)}")




