import math_util
import geracao_primos
import secrets

def gera_chaves_cifracao(totiente_euler):
    derivou_chaves = False        
            
    while(not derivou_chaves):
        e = secrets.randbelow(totiente_euler)
        mdc, _, d =  math_util.algoritmo_extendido_euclides(totiente_euler, e)
        derivou_chaves = mdc == 1

    return e, d % totiente_euler
        


def gera_chaves():
    p = geracao_primos.gera_primo_aleatorio_com_nbytes(128)
    q = geracao_primos.gera_primo_aleatorio_com_nbytes(128)
    n = p*q
    totiente_euler = (p-1)*(q-1)
    e, d = gera_chaves_cifracao(totiente_euler)

    print(f'Valor de n: {n}')
    print(f'Valor de e: {e}')
    print(f'Valor de d: {d}')