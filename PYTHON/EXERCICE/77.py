vogais = ('a','e','i','o','u')
palavras = ('aprender','programar','linguagem','python','curso','estudar','praticar')

for p in palavras:
    print(f'Na palavra {p.upper()} temos: ', end='')
    for letras in p:
        if letras in vogais:
            print (letras, end='')
    print('')


