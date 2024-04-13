import numpy as np
from PIL import Image

def carregar_imagem(caminho):
  return Image.open(caminho) # carregando a imagem e retorna ela

def converter_para_matriz(imagem):
  return np.array(imagem)

def imprimir_dados_matriz(matriz):
  np.set_printoptions(threshold=np.inf) # realizar impressão completa da matriz
  print(matriz) # impressão da matriz 
  
  num_linhas, num_colunas, num_canais = matriz.shape # detalhes da matriz
  print(f'Número de linhas: {num_linhas}')
  print(f'Número de colunas: {num_colunas}')
  print(f'Número de canais de cor: {num_canais}')

def main():
  """ Em primeiro momento eu estou transformando a imagem 
  em uma matriz e analisando se foi feito corretamente """
  caminho_imagem = 'meteor_img.png'
  imagem = carregar_imagem(caminho_imagem)
  imagem_matriz = converter_para_matriz(imagem)
  imprimir_dados_matriz(imagem_matriz)

if __name__ == "__main__":
  main()

