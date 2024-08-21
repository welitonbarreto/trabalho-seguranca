from hashlib import sha256
from assinatura import AssinaturaRsa
from rsa import KeyRsa

def assina_bytes(bytes_mensagem, chave_rsa: KeyRsa, hash_function=sha256):
    hash_mensagem = hash(bytes_mensagem).digest()
    AssinaturaRsa(bytes_mensagem, chave_rsa.valor_modulo, chave_rsa.cifra(hash_mensagem))

    return AssinaturaRsa
