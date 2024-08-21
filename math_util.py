
def algoritmo_extendido_euclides(valor_anterior, valor_atual):
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