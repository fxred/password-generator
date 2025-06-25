import main
import pytest

def test_size():
    size = main.gerador_de_senha(12, True, False, False, False)
    assert len(size) == 12

def test_all_false():
    with pytest.raises(ValueError, match="Os valores não podem ser todos falsos"):
        main.gerador_de_senha(10, False, False, False, False)

def test_minusculo():
    password = main.gerador_de_senha(8, True, False, False, False)
    contador = 0
    verificador = 0
    while contador < len(password):
        if (password[contador].islower()):
            verificador = 1
            break
        contador += 1
    assert verificador == 1

def test_numero():
    password = main.gerador_de_senha(8, False, False, True, False)
    contador = 0
    verificador = 0
    while contador < len(password):
        if (password[contador].isnumeric()):
            verificador = 1
            break
        contador += 1
    assert verificador == 1

def test_maiusculo():
    password = main.gerador_de_senha(8, False, True, False, False)
    contador = 0
    verificador = 0
    while contador < len(password):
        if (password[contador].isupper()):
            verificador = 1
            break
        contador += 1
    assert verificador == 1

def test_simbolo():
    password = main.gerador_de_senha(8, False, False, False, True)
    contador = 0
    verificador = 0
    while contador < len(password):
        if (33 < ord(password[contador]) < 47):
            verificador = 1
            break
        contador += 1
    assert verificador == 1

def test_todas_condicoes():
    password = main.gerador_de_senha(8, True, True, True, True)
    contador_minusculo = 0
    verificador_minusculo = 0
    while contador_minusculo < len(password):
        if (password[contador_minusculo].islower()):
            verificador_minusculo = 1
            break
        contador_minusculo += 1

    contador_numero = 0
    verificador_numero = 0
    while contador_numero < len(password):
        if (password[contador_numero].isnumeric()):
            verificador_numero = 1
            break
        contador_numero += 1

    contador_maiusculo = 0
    verificador_maiusculo = 0
    while contador_maiusculo < len(password):
        if (password[contador_maiusculo].isupper()):
            verificador_maiusculo = 1
            break
        contador_maiusculo += 1

    contador_simbolo = 0
    verificador_simbolo = 0
    while contador_simbolo < len(password):
        if (33 < ord(password[contador_simbolo]) < 47):
            verificador_simbolo = 1
            break
        contador_simbolo += 1
        
    assert verificador_minusculo & verificador_numero & verificador_maiusculo & verificador_simbolo