import numpy as np
from PIL import Image

def converter_para_matriz(caminho):
  """ Primeiro abro a imagem, seguido pela transformação
  para uma matriz e por fim a copnversão para o formato RGB """
  imagem = Image.open(caminho)
  imagem_matriz = np.array(imagem)
  imagem_matriz_rgb = imagem_matriz[:, :, :3]
  return imagem_matriz_rgb

def imprimir_dados_matriz(matriz):
  """" Primeiro permito a impressão completa da matriz, uma vez que o python 
  trunca matrizes muito grandes (que é o caso), e faço a impressão em seguida"""
  np.set_printoptions(threshold=np.inf) 
  print(matriz) 
  
  """ Impresssão de algumas informações da matriz, apenas para verificação"""
  num_linhas, num_colunas, num_canais = matriz.shape 
  print(f'Número de linhas: {num_linhas}')
  print(f'Número de colunas: {num_colunas}')
  print(f'Número de canais de cor: {num_canais}')
  
def contar_cores_especificas(matriz, cor):
  """ Conta a quantidade de vezes que uma determinada cor RGB aparece """
  return np.sum(np.all(matriz == cor, axis=-1))

def contar_meteoros_na_agua(imagem_matriz, cor_meteoro, cor_agua):
  """ Conta o número de meteoros que caem na água verificando se há um pixel de água na mesma coluna """
  num_meteoros_na_agua = 0
  for x in range(imagem_matriz.shape[1]):
    coluna = imagem_matriz[:, x]
    if np.any(np.all(coluna == cor_meteoro, axis=1)) and np.any(np.all(coluna == cor_agua, axis=1)):
      num_meteoros_na_agua += 1
  return num_meteoros_na_agua


def main():
  """ Em primeiro momento eu estou transformando a imagem 
  em uma matriz e analisando se foi feito corretamente """
  caminho_imagem = 'meteor_img.png'
  imagem_matriz_rgb = converter_para_matriz(caminho_imagem)
  # imprimir_dados_matriz(imagem_matriz_rgb)
  
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
