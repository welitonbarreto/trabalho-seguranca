from hashlib import sha256
from assinatura_rsa import AssinaturaRsa
from rsa import KeyRsa

def assina_bytes(bytes_mensagem, chave_rsa: KeyRsa, hash_function=sha256) -> AssinaturaRsa:
    hash_mensagem = hash_function(bytes_mensagem).digest()

    return AssinaturaRsa(bytes_mensagem, chave_rsa.valor_modulo, chave_rsa.cifra(int.from_bytes(hash_mensagem)))
