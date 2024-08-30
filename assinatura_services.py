from rsa import KeyRsa
import parsing_assinatura
import formatacao_base_64
from bloco_assinado import BlocoAssinado

def le_conteudo_arquivo(nome_arquivo: str):
    with open(nome_arquivo, "rb") as arquivo:
        conteudo_arquivo = arquivo.read()

    return conteudo_arquivo


def grava_arquivo(nome_arquivo: str, conteudo: bytes):
    with open(nome_arquivo, "wb") as arquivo:
        arquivo.write(conteudo)

def assina_conteudo_arquivo():
    nome_arquivo = input("Informe o nome do arquivo que deseja assinar: ")
    nome_arquivo_destino = input("Informe o nome do arquivo de destino: ")
    n = int(input("Digite o valor de n: "))
    e = int(input("Digite o valor de e: "))

    conteudo_arquivo = le_conteudo_arquivo(nome_arquivo)
    bloco_assinado = BlocoAssinado.gerado_do_zero(conteudo_arquivo, KeyRsa(n,e))
    conteudo_arquivo_destino = formatacao_base_64.codifica_base_64(parsing_assinatura.bloco_assinado_para_bytes(bloco_assinado))

    grava_arquivo(nome_arquivo_destino, conteudo_arquivo_destino)

def verifica_assinatura_em_arquivo():
    nome_arquivo = input("Informe o nome do arquivo com a assinatura: ")
    chave_verificacao = int(input("Digite o valor da chave de verificação: "))

    try:
        conteudo = formatacao_base_64.decodifica_base_64(le_conteudo_arquivo(nome_arquivo))
        bloco_assinado = parsing_assinatura.bytes_para_assinatura(conteudo)
        if not bloco_assinado.possui_assinatura_valida(chave_verificacao):
            raise Exception("Assinatura Inválida")

        print("Assinatura Válida")
    except:
        print("Assinatura Inválida")
        

