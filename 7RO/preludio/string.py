texto = "En el reino de Hyrule la leyenda del heroe del tiempo perdurara por siempre"
print(texto)

print(f"\nEl texto tiene {len(texto)} caracteres")

print(f"\nEl texto sin espacios tiene {len(texto.replace(" ", ""))} caracteres\n")

print(texto.lower())

print(f"\nEl texto cuenta con {texto.count('a')} letras 'a', {texto.count('e')} letras 'e', {texto.count('i')} letras 'i', {texto.count('o')} letras o y {texto.count('u')} letras u")

print(f"\nEl texto cuenta con {texto.split()} palabras\n")

print(texto[3:])

print()

print(texto.replace(" ", "-").swapcase())