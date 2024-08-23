import rsa_oaep
from rsa import KeyRsa
  
def imprime_bytes(bytes_entrada):
    print(''.join(format(x, '02x') for x in bytes_entrada))

def cifra_mensagem_usuario():
    mensagem = input("Digite a mensagem desejada: ")
    bytes_mensagem = mensagem.encode()

    n = int(input("Digite o valor de n: "))
    e = int(input("Digite o valor de e: "))

    bytes_mensagem_cifrada = rsa_oaep.cifra(bytes_mensagem, KeyRsa(n, e))
    print("Esses é o criptograma (hexadecimal)")
    imprime_bytes(bytes_mensagem_cifrada)

def decifra_criptograma_usuario():
    hex_string = input("Digite o criptograma (hexadecimal): ")
    bytes_criptograma = bytes.fromhex(hex_string)
   
    n = int(input("Digite o valor de n: "))
    d = int(input("Digite o valor de d: "))

    mensagem_original = rsa_oaep.decifra(bytes_criptograma, KeyRsa(n, d)).decode()
    print(f'Essa é sua mensagem original: {mensagem_original}')