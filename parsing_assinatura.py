from assinatura_rsa import AssinaturaRsa
import math_util

def assinatura_para_bytes(assinatura: AssinaturaRsa):
    bytes_header = len(assinatura.mensagem_bytes).to_bytes(8)
    bytes_header += math_util.calcula_tamanho_em_bytes(assinatura.valor_modulo).to_bytes(8)
    bytes_header += math_util.calcula_tamanho_em_bytes(assinatura.cifracao_hash).to_bytes(8)

    bytes_body = assinatura.mensagem_bytes
    bytes_body += math_util.converte_int_para_bytes(assinatura.valor_modulo)
    bytes_body += math_util.converte_int_para_bytes(assinatura.cifracao_hash)

    return bytes_header + bytes_body


def sub_bytes(bytes_entrada: bytes, posicao: int, quantidade: int):
    if posicao >= len(bytes_entrada) or (posicao+quantidade > len(bytes_entrada)):
        raise Exception("A posicão e a quantidade desejada transborda os limites dos bytes de entrada")

    return bytes_entrada[posicao: posicao+quantidade]



def bytes_para_assinatura(conteudo: bytes):
    tamanho_mensagem = int.from_bytes(sub_bytes(conteudo, 0, 8))
    tamanho_valor_modulo = int.from_bytes(sub_bytes(conteudo, 8, 8))
    tamanho_cifracao_hash = int.from_bytes(sub_bytes(conteudo, 16, 8))


    mensagem_bytes = sub_bytes(conteudo, 24, tamanho_mensagem)
    valor_modulo = int.from_bytes(sub_bytes(conteudo, 24 + tamanho_mensagem, tamanho_valor_modulo))
    cifracao_hash = int.from_bytes(sub_bytes(conteudo, 24 + tamanho_mensagem + tamanho_valor_modulo, tamanho_cifracao_hash))

    if len(conteudo) > (tamanho_mensagem + tamanho_valor_modulo + tamanho_cifracao_hash + 24):
        raise Exception("Sobraram bytes")


    return AssinaturaRsa(mensagem_bytes, valor_modulo, cifracao_hash)
