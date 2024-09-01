import geracao_chave_rsa
import rsa_oaep_services
import assinatura_services
import sys
import os

def limpa_tela():
    os.system('cls' if os.name=='nt' else 'clear')


def imprime_opcoes_de_servicos():
    print('Serviços disponíveis:')
    print('1. Gerar chaves RSA')
    print('2. Cifrar mensagem com RSA/OAEP')
    print('3. Decifrar criptograma com RSA/OAEP')
    print('4. Assinar arquivo com RSA')
    print('5. Verificação assinatura RSA em arquivo e gravação do conteúdo original')
    print('6. Finalizar')

def main():
    servicos = {
        '1': geracao_chave_rsa.gera_chaves,
        '2': rsa_oaep_services.cifra_mensagem_usuario,
        '3': rsa_oaep_services.decifra_criptograma_usuario,
        '4': assinatura_services.assina_conteudo_arquivo,
        '5': assinatura_services.verificacao_e_gravacao_assinatura_em_arquivo,
        '6': sys.exit,
    }

    if __name__ == '__main__':        
        while(True):
            limpa_tela()
            imprime_opcoes_de_servicos()
            opcao_selecionada = input("Qual opção deseja selecionar? ")
            if opcao_selecionada in servicos:
                servicos[opcao_selecionada]()
                input("Digite qualquer coisa para continuar ")

main()
