"""Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
Napište program, který vygeneruje všechna prvočísla menší než N
pomocí algoritmu Eratosthenovo síto.

Eratosthenovo síto funguje tak, že postupně "odškrtáváte" násobky každého čísla počínaje 2,
které jsou tím pádem složená čísla. Čísla, která zůstanou neodškrtnutá, jsou prvočísla.
"""


def print_n_prime_number(n):
    for i in range(n+1):
        if is_prime(i):
            print(i,end=" ")
        print()

def sieve_of_eratoshenes(n):
    sieve = [True]



