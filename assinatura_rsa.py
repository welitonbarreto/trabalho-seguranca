from hashlib import sha256
from rsa import KeyRsa
import math_util

class AssinaturaRsa:
    def __init__(self, mensagem_bytes: bytes, valor_modulo: int, cifracao_hash: int):
        self._mensagem_bytes = mensagem_bytes
        self._valor_modulo = valor_modulo
        self._cifracao_hash = cifracao_hash

    @classmethod
    def assina_bytes(cls, mensagem_bytes: bytes, chave_rsa: KeyRsa, hash_function=sha256): 
        hash_mensagem = hash_function(mensagem_bytes).digest()

        return cls(mensagem_bytes, chave_rsa.valor_modulo, chave_rsa.cifra(int.from_bytes(hash_mensagem)))


    def eh_valida(self, chave_verificacao: int) -> bool:
        valor_decifrado_hash = KeyRsa(self._valor_modulo, chave_verificacao).decifra(self.cifracao_hash)
        hash_obtido = math_util.converte_int_para_bytes(valor_decifrado_hash)

        return sha256(self._mensagem_bytes).digest() == hash_obtido

    @property
    def mensagem_bytes(self):
        return self._mensagem_bytes

    @property
    def valor_modulo(self):
        return self._valor_modulo

    @property
    def cifracao_hash(self):
        return self._cifracao_hash
    