from assinatura import AssinaturaRsa

def calcula_tamanho_numero_em_bytes(numero):
    num_bits = bin(numero)[2:]
    return len(num_bits) // 8 + (1 if len(num_bits) % 8 > 0 else 0)



def assinatura_para_arquivo(nome_arquivo, assinatura: AssinaturaRsa):
    bytes_header = len(assinatura.mensagem).to_bytes(8)
    bytes_header += calcula_tamanho_numero_em_bytes(assinatura.valor_modulo).to_bytes(8)
    bytes_header += len(assinatura.cifracao_hash).to_bytes(8)

    bytes_body = assinatura.mensagem
    bytes_body += assinatura.valor_modulo.to_bytes(calcula_tamanho_numero_em_bytes(assinatura.valor_modulo)) 
    bytes_body += calcula_tamanho_numero_em_bytes(assinatura.cifracao_hash)
    return bytes_header + bytes_body

'''
print(calcula_tamanho_numero_em_bytes(4194305))
'''