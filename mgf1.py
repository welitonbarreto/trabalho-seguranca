def mgf1(seed, tamanho_desejado, hash_function):
    resultado = b''

    contador = 0
    while(len(resultado) < tamanho_desejado):
        resultado += hash_function(seed + contador.to_bytes(4)).digest()
        contador += 1


    return resultado[:tamanho_desejado]