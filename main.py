import random

def gerador_de_senha(tamanho, minusculas, maiusculas, numeros, simbolos):
    if not any([minusculas, maiusculas, numeros, simbolos]):
        raise ValueError("Os valores não podem ser todos falsos")

    divisor = 0

    if minusculas:
        divisor += 1
    if maiusculas:
        divisor += 1
    if numeros:
        divisor += 1
    if simbolos:
        divisor += 1

    indexes = random.sample(range(0,tamanho),tamanho)

    caracteres_restantes = tamanho - ((tamanho // divisor)*divisor)


    if minusculas:
        arr_minusculas = []
        for i in range(0, (tamanho // divisor) + caracteres_restantes):
            arr_minusculas.append(chr(random.randint(97, 122)))
    if maiusculas:
        arr_maiusculas = []
        for i in range(0, (tamanho // divisor)):
            arr_maiusculas.append(chr(random.randint(65, 90)))
    if numeros:
        arr_numeros = []
        for i in range(0, (tamanho // divisor)):
            arr_numeros.append(str(random.randint(0, 9)))
    if simbolos:
        arr_simbolos = []
        for i in range(0, (tamanho // divisor)):
            arr_simbolos.append(chr(random.randint(33, 47)))

    senha = [0] * tamanho

    fator = len(indexes) // divisor

    if minusculas:
        for i in range(fator):
            senha[indexes[i]] = arr_minusculas.pop(0)
        for i in range(fator):
            indexes.pop(0)

    if maiusculas:
        for i in range(fator):
            senha[indexes[i]] = arr_maiusculas.pop(0)
        for i in range(fator):
            indexes.pop(0)

    if numeros:
        for i in range(fator):
            senha[indexes[i]] = arr_numeros.pop(0)
        for i in range(fator):
            indexes.pop(0)

    if simbolos:
        for i in range(fator):
            senha[indexes[i]] = arr_simbolos.pop(0)
        for i in range(fator):
            indexes.pop(0)
    

    if caracteres_restantes > 0:
        for i in range(caracteres_restantes):
            senha[indexes[i]] = arr_minusculas.pop(0)
        for i in range(caracteres_restantes):
            indexes.pop(0)
    

    senha = ''.join(senha)
    return senha