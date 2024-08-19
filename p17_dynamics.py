def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


# vypsat všechna prvočísla menší než n (10000)
def print_n_prime_numbers(n: int):
    # pro každé i v tomto rozsahu
    for i in range(n+1):
        if is_prime(i):
            print(i, end=" ")
    print()

    if __name__ == "__main__":
        