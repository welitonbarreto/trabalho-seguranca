import geracao_primos
import math_util

class KeyRsa():
    def __init__(self, valor_modulo, chave):
        self._valor_modulo = valor_modulo
        self._chave = chave

    def cifra(self, mensagem) -> int:
        if(not(1 <= mensagem < self._valor_modulo)):
            raise Exception("Mensagem de tamanho incorreto!!!")
    
        return pow(mensagem, self._chave, self._valor_modulo)
    
    def decifra(self, criptograma) -> int:
        if(not(1 <= criptograma < self._valor_modulo)):
            raise Exception("Criptograma de tamanho incorreto!!!")
        return pow(criptograma, self._chave, self._valor_modulo)

    @property
    def valor_modulo(self) -> int:
        return self._valor_modulo
    
'''

p = geracao_primos.geraPrimoAleatorio(128)
q = geracao_primos.geraPrimoAleatorio(128)
totiente = (p-1) * (q-1)
e = 65537
d = math_util.algoritmo_extendido_euclides(totiente, e)[2] % totiente

print(f'Esse é o n {p*q}')
print(f'Esse é o d {d}')
print((d*e) % (totiente))
#print(len(bin(p)[2:]))
'''
