
import secrets
import random

def calcula_divisoes_sucessivas(dividendo, divisor):
    numero_divisoes = 0

    while(dividendo % divisor == 0):
        dividendo = dividendo // divisor
        numero_divisoes += 1

    return numero_divisoes, dividendo


def teste_miller(valor_teste, candidato_primo):
    numero_divisoes, resto_divisoes_sucessivas = calcula_divisoes_sucessivas(candidato_primo-1, 2)
    temp = pow(valor_teste, resto_divisoes_sucessivas, candidato_primo)

    if temp == 1:
        return 'INCONCLUSIVO'
    
    for _ in range(numero_divisoes):
        if (candidato_primo - 1) == temp:
            return 'INCONCLUSIVO'

        temp = pow(temp, 2, candidato_primo)

    return 'COMPOSTO'


def teste_miller_rabin(candidato_primo, numero_iteracoes=40):
    for i in range(numero_iteracoes):
        valor_aleatorio = random.randint(1,candidato_primo-1)
        if(teste_miller(valor_aleatorio, candidato_primo) == 'COMPOSTO'):
            return 'COMPOSTO'

    return "PROVAVELMENTE PRIMO"


def gera_numero_impar_aleatorio(tamanho_bytes):
    bytearray_gerado = bytearray(secrets.token_bytes(tamanho_bytes))
    bytearray_gerado[0] |= 128
    bytearray_gerado[-1] |= 1
    return  int.from_bytes(bytearray_gerado)

def geraPrimoAleatorio(tamanho_bytes):
    passou_teste = False
    while(not passou_teste):
        valor_aleatorio = gera_numero_impar_aleatorio(tamanho_bytes)
        passou_teste = teste_miller_rabin(valor_aleatorio) == "PROVAVELMENTE PRIMO"

    return valor_aleatorio