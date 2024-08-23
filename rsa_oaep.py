import math_util
import oaep
from rsa import KeyRsa

def cifra(bytes_mensagem, chave: KeyRsa):
    tamanho_modulo_em_bytes = math_util.calcula_tamanho_em_bytes(chave.valor_modulo)
    resultado_oaep = oaep.encoding(bytes_mensagem, tamanho_modulo_em_bytes)
    valor_cifrado = chave.cifra(int.from_bytes(resultado_oaep))
    return valor_cifrado.to_bytes(tamanho_modulo_em_bytes)

def decifra(bytes_cifrados, chave: KeyRsa):
    valor_cifrado = chave.decifra(int.from_bytes(bytes_cifrados))
    bytes_valor_cifrado = valor_cifrado.to_bytes(len(bytes_cifrados))
    return oaep.decoding(bytes_valor_cifrado, len(bytes_cifrados))
