import numpy as np
from PIL import Image

def converter_para_matriz(caminho):
  """ Abertura de imagem e conversão para o formato RGB """
  imagem = Image.open(caminho)
  imagem_matriz = np.array(imagem)
  imagem_matriz_rgb = imagem_matriz[:, :, :3]
  return imagem_matriz_rgb

def imprimir_dados_matriz(matriz):
  """" Habilito impressão completa e assim imprimo """
  np.set_printoptions(threshold=np.inf) 
  print(matriz) 
  
  num_linhas, num_colunas, num_canais = matriz.shape 
  print(f'Número de linhas: {num_linhas}')
  print(f'Número de colunas: {num_colunas}')
  print(f'Número de canais de cor: {num_canais}')
  
def contar_cores_especificas(matriz, cor):
  return np.sum(np.all(matriz == cor, axis=-1))

def contar_meteoros_na_agua(imagem_matriz, cor_meteoro, cor_agua):
  """ Conta o número de meteoros perpendiculares à água  """
  num_meteoros_na_agua = 0
  for x in range(imagem_matriz.shape[1]):
    coluna = imagem_matriz[:, x]
    if np.any(np.all(coluna == cor_meteoro, axis=1)) and np.any(np.all(coluna == cor_agua, axis=1)):
      num_meteoros_na_agua += 1
  return num_meteoros_na_agua


def main():
  """ Transformando a imagem em uma matriz """
  caminho_imagem = 'meteor_img.png'
  imagem_matriz_rgb = converter_para_matriz(caminho_imagem)
  
  """ Definindo os valores RGB passados"""
  cor_estrela = [255, 255, 255] # pure white
  cor_meteoro = [255, 0, 0] # pure red
  cor_agua = [0, 0, 255] # pure blue
  
  """ Em segundo momento eu realizo a contagem de estrelas e meteoros, baseado no RGB de cada"""
  num_estrelas = contar_cores_especificas(imagem_matriz_rgb, cor_estrela)
  num_meteoros = contar_cores_especificas(imagem_matriz_rgb, cor_meteoro)
  print(f'Estrelas: {num_estrelas}')
  print(f'Meteoros: {num_meteoros}')
  
  """ Por fim, encontro os meteoros perpendiculares à água """
  num_meteoros_na_agua = contar_meteoros_na_agua(imagem_matriz_rgb, cor_meteoro, cor_agua)
  print(f'Número de meteoros na água: {num_meteoros_na_agua}')

if __name__ == "__main__":
  main()
