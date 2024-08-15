a = int(input("Zadej hodnotu a: "))
b = int(input("Zadej hodnotu b: "))

# def nsn(a, b):
#     i = max(a, b)
#     while True:
#         if i % a == 0 and i % b == 0:
#             return i
#         i += max(a, b)
#
#
# print(nsn(340, 730))


def nsn(a, b):
    maximum = max(a, b)

    while True:
        print(maximum)
        if maximum % a == 0 and maximum % b == 0:
            return maximum

        maximum += max(a, b)

print(nsn(23, 50))
