import math_util
import oaep
from rsa import KeyRsa

def cifra(bytes_mensagem, chave: KeyRsa):
    tamanho_modulo_em_bytes = math_util.calcula_tamanho_em_bytes(chave.valor_modulo)
    resultado_oaep = oaep.encoding(bytes_mensagem, tamanho_modulo_em_bytes)
    valor_cifrado = chave.cifra(int.from_bytes(resultado_oaep))
    return valor_cifrado.to_bytes(tamanho_modulo_em_bytes)

def decifra(bytes_cifrados, chave: KeyRsa):
    tamanho_modulo_em_bytes = math_util.calcula_tamanho_em_bytes(chave.valor_modulo)
    valor_decifrado = chave.decifra(int.from_bytes(bytes_cifrados))
    bytes_valor_decifrado = valor_decifrado.to_bytes(tamanho_modulo_em_bytes)
    return oaep.decoding(bytes_valor_decifrado)
