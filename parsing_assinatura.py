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


def obtem_sub_bytes(bytes_entrada: bytes, posicao: int, quantidade: int):
    return bytes_entrada[posicao: posicao+quantidade]

def bytes_para_assinatura(conteudo: bytes):
    tamanho_mensagem = int.from_bytes(conteudo[:8])
    tamanho_valor_modulo_n = int.from_bytes(conteudo[8:16])
    tamanho_cifracao_hash = int.from_bytes(conteudo[16:24])

    posicao_atual = 24

    mensagem_bytes = obtem_sub_bytes(conteudo, posicao_atual, tamanho_mensagem)
    posicao_atual += tamanho_mensagem

    valor_modulo_n = int.from_bytes(obtem_sub_bytes(conteudo, posicao_atual, tamanho_valor_modulo_n))
    posicao_atual += tamanho_valor_modulo_n

    cifracao_hash = int.from_bytes(obtem_sub_bytes(conteudo, posicao_atual, tamanho_cifracao_hash))

    return AssinaturaRsa(mensagem_bytes, valor_modulo_n, cifracao_hash)