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
    