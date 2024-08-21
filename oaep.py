from hashlib import sha256
from mgf1 import mgf1
import secrets

def xor(bytearray1, bytearray2):
    if(len(bytearray1) != len(bytearray2)):
        raise Exception('Bytearrays com tamanhos diferentes')

    return bytes([x ^ y for x, y in zip(bytearray1, bytearray2)])


def gera_bloco_dados(mensagem, tamanho_maximo, hash_function):
    padding = b'\x00'*(tamanho_maximo - len(mensagem) - 2*hash_function().digest_size - 2)
    return hash_function().digest() + padding  + b'\x01' + mensagem
  

def encoding_oaep(mensagem, tamanho_maximo=512, hash_function=sha256):    
    if len(mensagem) > tamanho_maximo - 2*hash_function().digest_size - 2:
        raise Exception("Mensagem muito grande!!!")
  
    seed = secrets.token_bytes(hash_function().digest_size)
    bloco_dados = gera_bloco_dados(mensagem, tamanho_maximo, hash_function)

    masked_bloco_dados = xor(mgf1(seed, len(bloco_dados), hash_function), bloco_dados)
    masked_seed =  xor(mgf1(masked_bloco_dados, len(seed), hash_function), seed)

    return b'\x00' + masked_seed + masked_bloco_dados

def separa_texto_cifrado(mensagem_cifrada, tamanho_seed):
    return mensagem_cifrada[:1], mensagem_cifrada[1:tamanho_seed+1], mensagem_cifrada[tamanho_seed+1:] 


def obtem_mensagem_de_bloco_dados(bloco_dados, hash_function):
    if bloco_dados[:hash_function().digest_size] != hash_function().digest():
        raise Exception("Hash inválido")
    
    for i in range(hash_function().digest_size, len(bloco_dados)):
        if bloco_dados[i] == 1:
            return bloco_dados[i+1:]

        if bloco_dados[i] != 0:
            raise Exception("Padding incorreto")
        
    raise Exception("Padding incorreto")



def decoding_oaep(mensagem_cifrada, tamanho_maximo=512, hash_function=sha256):
    hash_digest_size =  hash_function().digest_size
    primeiro_byte, masked_seed, masked_bloco_dados = separa_texto_cifrado(mensagem_cifrada, hash_digest_size)

    if(primeiro_byte != b'\x00'):
        raise Exception("Entrada inválida: primeiro byte deve ser b'\x00'")

    seed = xor(masked_seed, mgf1(masked_bloco_dados, len(masked_seed), hash_function))
    bloco_dados = xor(masked_bloco_dados, mgf1(seed, tamanho_maximo - hash_digest_size - 1, hash_function))

    return obtem_mensagem_de_bloco_dados(bloco_dados, hash_function)


'''

mensagem_cifrada1 = encoding_oaep(b'\x02\xba')
mensagem_cifrada2 = encoding_oaep(b'\x02\xba')

print(f'Mensagem cifrada 1:{mensagem_cifrada1.hex()}')
print(f'Mensagem cifrada 2:{mensagem_cifrada2.hex()}')

print(f'Mensagem cifrada 2:{decoding_oaep(mensagem_cifrada2).hex()}')

#print(mensagem_cifrada.hex())
#mensagem_decifrada = decoding_oaep(mensagem_cifrada)
#print(mensagem_decifrada)'''