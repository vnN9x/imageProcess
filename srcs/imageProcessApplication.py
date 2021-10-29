import os
import matplotlib.pyplot as plt
import matplotlib.image as im
import numpy as np


def imagem_para_matriz(nome_file: str) -> np.array:
    matriz_colorida = im.imread(nome_file)
    matriz_8bit = matriz_colorida.astype(np.uint16)

    return matriz_8bit


def colorida_para_cinza(matriz_colorida: np.array) -> np.array:
    linhas = matriz_colorida.shape[0]
    colunas = matriz_colorida.shape[1]

    mtrz_cinza = np.zeros((linhas, colunas))

    for i in range(linhas):
        for j in range(colunas):
            r, g, b = matriz_colorida[i, j]
            mtrz_cinza[i, j] = int((r + g + b) / int(matriz_colorida.shape[2]))

    return mtrz_cinza


def histograma(matriz_cinza: np.array) -> np.array:
    histo = np.zeros(256).astype(int)
    linhas = matriz_cinza.shape[0]
    colunas = matriz_cinza.shape[1]

    for i in range(linhas):
        for j in range(colunas):
            cor = int(matriz_cinza[i, j])
            histo[cor] = histo[cor] + 1

    return histo


def threshold(matriz_cinza: np.array) -> int:
    cor_predominante = 0
    indice_divisor = 0
    matriz_histograma = histograma(matriz_cinza)

    for i in range(256):
        if matriz_histograma[i] > cor_predominante:
            cor_predominante = matriz_histograma[i]
            indice_divisor = i

    return indice_divisor


def binarizador(mtrz_cnz: np.array) -> np.array:
    linhas = mtrz_cnz.shape[0]
    colunas = mtrz_cnz.shape[1]
    matriz_segmentada = np.zeros((linhas, colunas))
    place_holder = threshold(mtrz_cnz)

    for i in range(linhas):
        for j in range(colunas):
            color = mtrz_cnz[i, j]
            if color < place_holder:
                matriz_segmentada[i, j] = 0
            else:
                matriz_segmentada[i, j] = 255

    return matriz_segmentada


def main():
    nome_file = os.path.join('..', 'files', 'img01.jpg')
    matriz_colorida = imagem_para_matriz(nome_file)
    matriz_cinza = colorida_para_cinza(matriz_colorida)
    histo = histograma(matriz_cinza)
    matriz_binaria = binarizador(matriz_cinza)

    print('IMAGEM COLORIDA')
    plt.imshow(matriz_colorida)
    plt.title('IMAGEM COLORIDA')
    plt.show()

    print('IMAGEM CINZA')
    plt.imshow(matriz_cinza, cmap='gray')
    plt.title('IMAGEM CINZA')
    plt.show()

    print('HISTOGRAMA')
    print(histo)
    plt.plot(histo)
    plt.title('HISTOGRAMA')
    plt.show()

    print('IMAGEM BINARIZADA')
    plt.imshow(matriz_binaria, cmap='gray')
    plt.title('IMAGEM BINARIZADA')
    plt.show()


if __name__ == "__main__":
    main()
