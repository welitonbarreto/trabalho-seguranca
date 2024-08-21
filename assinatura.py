from hashlib import sha256
from rsa import KeyRsa


class AssinaturaRsa:
    def __init__(self, mensagem, valor_modulo, cifracao_hash):
        self._mensagem = mensagem
        self._valor_modulo = valor_modulo
        self._cifracao_hash = cifracao_hash

    @property
    def mensagem(self):
        return self._mensagem

    @property
    def valor_modulo(self):
        return self._valor_modulo

    @property
    def cifracao_hash(self):
        return self._cifracao_hash
    

class TrechoAssinatura:
    def __init__(self, bytes_tamanho, bytes_conteudo):
        self._bytes_tamanho = bytes_tamanho
        self._bytes_conteudo = bytes_conteudo

    def total_bytes(self):
        return len(self._bytes_tamanho) + len(self._bytes_conteudo)

    def bytes_conteudo(self):
        return self._bytes_conteudo

    def tamanho_conteudo(self):
        return self._bytes_tamanho.from_bytes(8)


def assina_bytes(bytes_entrada, valor_modulo, tamanho_modulo, chave):
    hash_entrada = sha256(bytes_entrada).digest()
    info_dados = len(bytes_entrada).to_bytes(8) + bytes_entrada
    info_modulo = tamanho_modulo.to_bytes(8) + valor_modulo.to_bytes(tamanho_modulo)
    info_cifrado = tamanho_modulo.to_bytes(8) + KeyRsa(valor_modulo, chave).cifra(int.from_bytes(hash_entrada)).to_bytes(tamanho_modulo)

    return info_dados + info_modulo + info_cifrado

def obtem_trecho(assinatura, posicao_inicial):
    bytes_tamanho = assinatura[posicao_inicial:posicao_inicial+ 8]
    return TrechoAssinatura(bytes_tamanho, assinatura[posicao_inicial + 8: posicao_inicial + 8 + int.from_bytes(bytes_tamanho)])


def verifica_assinatura(assinatura, chave_verificacao):
    trecho_dados = obtem_trecho(assinatura, 0)
    trecho_modulo = obtem_trecho(assinatura, trecho_dados.total_bytes())
    trecho_cifrado = obtem_trecho(assinatura, trecho_dados.total_bytes() + trecho_modulo.total_bytes())

    key = KeyRsa(int.from_bytes(trecho_modulo.bytes_conteudo()), chave_verificacao)
    hash = key.decifra(int.from_bytes(trecho_cifrado.bytes_conteudo())).to_bytes(sha256().digest_size)

    return hash == sha256(trecho_dados.bytes_conteudo()).digest()


'''

valor_modulo = 19326380405036253862681608031092994602185697818719592772945235758298069977965299896988152374442988641764853391637306069399147439633885783578978568393344427735254738046086647556208240258945287138875428084745484274566013302803637609267339069867591949019946155202759127731463927473487668089840492946578211274536489193886710014870365878617046078391031441376693175762139167078919820094371911355386365332427878091225256533642612551546967035374142118033549324431159667328636230643841976263487661791956379686898690866006579727646743349001636970607819043540898140281292429365449598455573225785771234447894478902409031754134003
chave_cifracao = 65537
chave_decifracao = 3232908256105901263356248666323946775466710487001585296394382098939862080480241432636237766162907738829486972740891197931288484073214975439466897253402428571060587045474280439426750354133042142659739049591295666601571689864294659663973606099736187758146843759828010395960129955473172486823036211198817922741969459824216873457626280757090522720374020344456137160445544874858846129132216439182928265835827016953491282829433069206426768595804209547921375001432642341642393570165860753641831195127230656638362088319914045817723199421033699874154162174023830559366013235663987754755811703994737345950011672832276460434513
assinatura = assina_bytes(b'\x00\x01', valor_modulo, 256, chave_cifracao)

print(verifica_assinatura(assinatura, chave_decifracao))
'''