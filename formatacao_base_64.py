import math_util
base_64_table = [
    b'A', b'B', b'C', b'D', b'E', b'F', b'G', b'H', b'I', b'J', b'K', b'L', b'M', b'N', b'O', b'P', b'Q', b'R', b'S', b'T', b'U', b'V', b'W', b'X', b'Y', b'Z',
    b'a', b'b', b'c', b'd', b'e', b'f', b'g', b'h', b'i', b'j', b'k', b'l', b'm', b'n', b'o', b'p', b'q', b'r', b's', b't', b'u', b'v', b'w', b'x', b'y', b'z',
    b'0', b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8', b'9', b'+', b'/'
]


def obtem_bits_from_byte(byte_entrada, posicao, quantidade):
    string_binaria = bin(byte_entrada)[2:]
    string_binaria_formatada = (8 - len(string_binaria)) * '0' + string_binaria

    return string_binaria_formatada[posicao:posicao+quantidade]

def extrai_caracter_base_64(a_byte, residual_anterior):
    bits_capturados = obtem_bits_from_byte(a_byte, 0, 6 - len(residual_anterior))
    caracter_resultante = base_64_table[int(residual_anterior + bits_capturados, 2)]
    novo_residual = obtem_bits_from_byte(a_byte, len(bits_capturados), 8 - len(bits_capturados))

    return caracter_resultante, novo_residual


def codifica_base_64(bytes_entrada):
    resultado = []
    residual = ''

    for a_byte in bytes_entrada:
        caracter_resultante, residual = extrai_caracter_base_64(a_byte, residual)
        resultado.append(caracter_resultante)

        if len(residual) == 6:
            resultado.append(base_64_table[int(residual,2)])
            residual = ''

    if residual != '':
        resultado.append(base_64_table[int(residual + '0'*(6 - len(residual)), 2)])

    while len(resultado) % 4 != 0:
        resultado.append(b'=')

    return b''.join(resultado)


def conta_quantidade_padding(bytes_codificados):
    contador = 0

    for a_byte in reversed(bytes_codificados[-2:]):
        if a_byte != ord(b'='):
            return contador    

        contador += 1

    return contador

def calcula_tamanho_decodificacao(bytes_codificados):
    if len(bytes_codificados) % 4 != 0:
        raise Exception("Entrada possui tamanho incorreto!!!")

    quantidade_bytes_padding = conta_quantidade_padding(bytes_codificados)
        
    return ((len(bytes_codificados) - quantidade_bytes_padding) * 6 - quantidade_bytes_padding*2) // 8


def decodifica_base_64(bytes_codificados):
    tamanho_esperado = calcula_tamanho_decodificacao(bytes_codificados)
    bytes_decodificados = b''
    residual_bits = ''
    index = 0

    while len(bytes_decodificados) < tamanho_esperado:
        byte_atual = bytes_codificados[index].to_bytes(1)
        residual_bits += format(base_64_table.index(byte_atual), '008b')[2:]
        index += 1

        if len(residual_bits) >= 8:
            bytes_decodificados += math_util.bytes_from_bit_string(residual_bits[:8])
            residual_bits = residual_bits[8:]


    return bytes_decodificados