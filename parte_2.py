import geracao_chave_rsa
import rsa_oaep_services
import assinatura_services
import sys

def imprime_opcoes_de_servicos():
    print('Serviços disponíveis:')
    print('1. Gerar chaves RSA')
    print('2. Cifrar mensagem com RSA/OAEP')
    print('3. Decifrar criptograma com RSA/OAEP')
    print('4. Assinar arquivo com RSA')
    print('5. Verificar assinatura de arquivo com RSA')
    print('6. Finalizar')



def chama_servico_desejado(opcao_selecionada: int):
    match opcao_selecionada:
        case 1:
            geracao_chave_rsa.gera_chaves()
        case 2:
            rsa_oaep_services.cifra_mensagem_usuario()
        case 3:
            rsa_oaep_services.decifra_criptograma_usuario()
        case 4:
            assinatura_services.assina_arquivo()
        case 5:
            assinatura_services.verifica_assinatura_em_arquivo()
        case 6:
            sys.exit()

def main():
    if __name__ == '__main__':        
        finaliza_programa = False

        while(not finaliza_programa):
            imprime_opcoes_de_servicos()
            opcao_selecionada = int(input("Qual opção deseja selecionar? "))
            chama_servico_desejado(opcao_selecionada)
            input("Digite qualquer coisa para continuar ")

main()
