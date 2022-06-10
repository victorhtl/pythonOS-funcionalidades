import os


def formata_byte(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'bytes'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'Kb'
    elif tamanho < giga:
        tamanho /= giga
        texto = 'Mb'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'Gb'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'Tb'

    return f'{round(tamanho, 2)} {texto}'


def encontra_arquivo(caminho, termo=''):
    """
    caminho = insere o caminho da pasta
    termo = opcional, uma palavra chave para encontrar um arquivo dentro
    da pasta
    """
    conta = 0
    for raiz, diretorios, arquivos in os.walk(caminho):
        for arquivo in arquivos:
            conta += 1
            if termo in arquivo:
                try:
                    caminho_completo = os.path.join(raiz, arquivo)
                    nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                    tamanho = os.path.getsize(caminho_completo)
                    print()
                    print('Encontrei o arquivo:', arquivo)
                    print('Caminho:', caminho_completo)
                    print('Nome:', nome_arquivo)
                    print('Extensão:', ext_arquivo)
                    print('Tamanho:', formata_byte(tamanho))
                except Exception:
                    print('Erro desconhecido')
    print(f'{conta} arquivos encontrados')


encontra_arquivo('caminho', 'key_word')
