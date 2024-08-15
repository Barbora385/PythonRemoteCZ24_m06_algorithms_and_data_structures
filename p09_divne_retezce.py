# Napište funkci to_weird_case, která přijme řetězec a vrátí jej se všemi znaky na sudých pozicích převedenými
# na velké znaky a všemi znaky na lichých pozicích převedenými na malé znaky. Uvažujte,
# že každé slovo by mělo být považováno za samostatný řetězec tak, aby první znak každého slova měl vždy index 0,
# viz příklady níže. Nulu považujte za sudé číslo.#
# Struktura funkce by měla vypadat takto:
# dopsat dle tomáše
def to_weird_case(string: str) -> str:
    new_str = string.split()
    result = ""
    for slovo in new_str:
        for i,
        if i % 2 == 0:
            new_str += str.upper(slovo)
            i+= 1
    return(new_string)

def to_weird_case1(string: str) -> str:
	words = string.split()
	new_words = []

	for word in words:
		new_word = ''
		for i in range(len(word)):
			if i % 2 == 0:
                # 0=false, 1=true,... když napíši %2: je to vždy true
				new_word += word[i].upper()
			else:
				new_word += word[i].lower()
		new_words.append(new_word)

	return ' '.join(new_words)

# result.strip() ukrojí mezeru vzadu
## => return 'StRiNg'
print(to_weird_case('Algorithms and data structures'))
print(to_weird_case1('Algorithms and data structures'))
## => return 'AlGoRiThMs AnD DaTa StRuCtUrEs