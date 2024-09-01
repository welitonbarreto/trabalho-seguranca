import math

def algoritmo_euclides_estendido(valor_anterior, valor_atual):
    if valor_anterior < valor_atual:
        raise Exception("O primeiro parâmetro deve ser maior ou igual ao segundo")
    
    coeficiente_1_anterior, coeficiente_1_atual = 1, 0
    coeficiente_2_anterior, coeficiente_2_atual = 0, 1

    while(valor_atual != 0):
        q = valor_anterior // valor_atual
        valor_anterior, valor_atual = valor_atual, valor_anterior % valor_atual

        coeficiente_1_anterior, coeficiente_1_atual = coeficiente_1_atual, coeficiente_1_anterior - coeficiente_1_atual*q
        coeficiente_2_anterior, coeficiente_2_atual = coeficiente_2_atual, coeficiente_2_anterior - coeficiente_2_atual*q

    return (valor_anterior, coeficiente_1_anterior, coeficiente_2_anterior)


def bytes_from_bit_string(bit_string):
    return int(bit_string, 2).to_bytes((len(bit_string) + 7) // 8, 'big')


def calcula_tamanho_em_bytes(valor: int) -> int:
    return math.ceil(valor.bit_length() / 8)


def converte_int_para_bytes(valor: int):
    tamanho = calcula_tamanho_em_bytes(valor)
    return valor.to_bytes(tamanho)