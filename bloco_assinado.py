from hashlib import sha3_256
from rsa import KeyRsa
import math_util    

class BlocoAssinado:
    def __init__(self, bytes_bloco: bytes, valor_modulo_rsa: int, assinatura: int):
        self._bytes_bloco = bytes_bloco
        self._valor_modulo_rsa = valor_modulo_rsa
        self._assinatura = assinatura

    @classmethod
    def a_partir_assinatura_precalculada(cls, bytes_bloco: bytes, valor_modulo_rsa: int, assinatura: int):
        return cls(bytes_bloco, valor_modulo_rsa, assinatura)

    
    @classmethod
    def gerado_com_chave_rsa(cls, bytes_bloco: bytes, chave_rsa: KeyRsa, hash_function=sha3_256): 
        hash_calculado = hash_function(bytes_bloco).digest()
        assinatura = chave_rsa.cifra(int.from_bytes(hash_calculado))

        return cls(bytes_bloco, chave_rsa.valor_modulo, assinatura)


    def possui_assinatura_valida(self, chave_verificacao: int) -> bool:
        valor_decifrado = KeyRsa(self._valor_modulo_rsa, chave_verificacao).decifra(self._assinatura)
        hash_obtido = math_util.converte_int_para_bytes(valor_decifrado)

        return sha3_256(self._bytes_bloco).digest() == hash_obtido

    @property
    def bytes_bloco(self):
        return self._bytes_bloco

    @property
    def valor_modulo_rsa(self):
        return self._valor_modulo_rsa

    @property
    def assinatura(self):
        return self._assinatura
    