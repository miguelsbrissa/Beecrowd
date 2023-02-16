frase = input()
while frase != '*':
    palavras = frase.split(' ')
    inicial = frase[0]
    count = 0
    for palavra in palavras:
        if(palavra[0] == inicial.lower() or palavra[0] == inicial.upper()):
            count += 1

    if count == len(palavras):
        print('Y')
    else:
        print('N')
    frase = input()