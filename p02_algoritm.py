d = int(input("Zadej číslo větší nebo rovno 0:"))

# binary = ""
#
# while d > 0:
#     r = d % 2
#
#     if r == 1:
#         binary = "1" + binary
#     else:
#         binary = "0" + binary
#     d = d // 2
#     if d == 0:
#         print(binary)

def dec2bin(d):
    binary = ""
    # while True: ... můžeme d>0 nahradit jako nekonečný cyklus
    while d > 0:
        r = d % 2

        if r == 1:
            binary = "1" + binary
        else:
            binary = "0" + binary
        d = d // 2
        if d == 0:
            return (binary)

print(dec2bin(d))

for i in range(1,20):
    print(f"{i}:{dec2bin(i)}")
