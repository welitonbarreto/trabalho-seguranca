from bloco_assinado import BlocoAssinado
import math_util

def bloco_assinado_para_bytes(bloco_assinado: BlocoAssinado):
    bytes_header = len(bloco_assinado.bytes_bloco).to_bytes(8)
    bytes_header += math_util.calcula_tamanho_em_bytes(bloco_assinado.valor_modulo_rsa).to_bytes(8)
    bytes_header += math_util.calcula_tamanho_em_bytes(bloco_assinado.assinatura).to_bytes(8)

    bytes_body = bloco_assinado.bytes_bloco
    bytes_body += math_util.converte_int_para_bytes(bloco_assinado.valor_modulo_rsa)
    bytes_body += math_util.converte_int_para_bytes(bloco_assinado.assinatura)

    return bytes_header + bytes_body


def sub_bytes(bytes_entrada: bytes, posicao: int, quantidade: int):
    if posicao >= len(bytes_entrada) or (posicao+quantidade > len(bytes_entrada)):
        raise Exception("A posicão e a quantidade desejada transborda os limites dos bytes de entrada")

    return bytes_entrada[posicao: posicao+quantidade]



def bytes_para_assinatura(bytes_entrada: bytes):
    tamanho_bloco = int.from_bytes(sub_bytes(bytes_entrada, 0, 8))
    tamanho_valor_modulo_rsa = int.from_bytes(sub_bytes(bytes_entrada, 8, 8))
    tamanho_assinatura = int.from_bytes(sub_bytes(bytes_entrada, 16, 8))

    bytes_bloco = sub_bytes(bytes_entrada, 24, tamanho_bloco)
    valor_modulo_rsa = int.from_bytes(sub_bytes(bytes_entrada, 24 + tamanho_bloco, tamanho_valor_modulo_rsa))
    assinatura = int.from_bytes(sub_bytes(bytes_entrada, 24 + tamanho_bloco + tamanho_valor_modulo_rsa, tamanho_assinatura))

    if len(bytes_entrada) > (tamanho_bloco + tamanho_valor_modulo_rsa + tamanho_assinatura + 24):
        raise Exception("Sintaxe incorreta!!!")

    return BlocoAssinado.a_partir_assinatura_precalculada(bytes_bloco, valor_modulo_rsa, assinatura)
