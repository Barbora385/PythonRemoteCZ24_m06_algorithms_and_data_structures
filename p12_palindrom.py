"""Palindrom
Napište funkci, který zjistí, zda je daný řetězec palindrom.
Palindrom je řetězec, který se čte stejně zleva i zprava,
například 'madam' nebo 'racecar'.

is_palindrom("madam") -> True
is_palindrom("kobylamamalybok") -> True
is_palindrom("kokos") -> False
"""

def is_palindrom(text):
    return text == text[::-1]
    



    # if text == text[::-1]:
    #     return True
    # else:
    #     return False

print(is_palindrom("madam"))
print(is_palindrom("kobylamamalybok"))
print(is_palindrom("kokos"))