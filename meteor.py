import numpy as np
from PIL import Image

def carregar_imagem(caminho):
  """ Recebe o caminho do arquivo da imagem e retorna a imagem """ 
  return Image.open(caminho) 

def converter_para_matriz(imagem):
  return np.array(imagem)

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
  """ Conta a quantidade de vezes que um determinado array (cor) aparece """
  return np.sum(np.all(matriz == cor, axis=-1))

def main():
  """ Em primeiro momento eu estou transformando a imagem 
  em uma matriz e analisando se foi feito corretamente """
  caminho_imagem = 'meteor_img.png'
  imagem = carregar_imagem(caminho_imagem)
  imagem_matriz = converter_para_matriz(imagem)
  
  """ Em segundo momento eu realizo a contagem de estrelas e meteoros, baseado no RGB de cada"""
  cor_estrelas = (255, 255, 255, 255)  # pure white
  cor_meteoros = (255, 0, 0, 255)  # pure red
  num_estrelas = contar_cores_especificas(imagem_matriz, cor_estrelas)
  num_meteoros = contar_cores_especificas(imagem_matriz, cor_meteoros)
  print(f'Estrelas: {num_estrelas}')
  print(f'Meteoros: {num_meteoros}')

 
if __name__ == "__main__":
  main()
