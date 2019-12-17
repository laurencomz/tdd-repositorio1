def troca_vogais(texto):
    texto1 = list(texto)
    texto2 = []

    for letra in texto1:
        print(letra)
        if letra == 'a':
            texto2.append('@')
        elif letra == 'e':
            texto2.append('&')
        elif letra == 'i':
            texto2.append('!')
        elif letra == 'o':
            texto2.append('#')
        elif letra == 'u':
            texto2.append('*')

        else:
            texto2.append(letra)
        return ''.join(map(str,texto2))


print(troca_vogais('maneiro'))