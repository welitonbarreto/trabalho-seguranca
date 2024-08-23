class AssinaturaRsa:
    def __init__(self, mensagem_bytes: bytes, valor_modulo: int, cifracao_hash: int):
        self._mensagem_bytes = mensagem_bytes
        self._valor_modulo = valor_modulo
        self._cifracao_hash = cifracao_hash

    
    @property
    def mensagem_bytes(self):
        return self._mensagem_bytes

    @property
    def valor_modulo(self):
        return self._valor_modulo

    @property
    def cifracao_hash(self):
        return self._cifracao_hash
    