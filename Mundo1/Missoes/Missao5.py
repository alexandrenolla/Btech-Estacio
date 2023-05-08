'''
Implementar um programa para manipular dados de um arquivo texto e visualizá-los em um
histograma e nuvem de palavras.

1• objetivo: Gerar dados de testes
2• objetivo: Gravar e recuperar dados de arquivos de textos
3• objetivo: Manipular os dados para visualizá-los em um histograma
4• objetivo: Manipular os dados para visualizá-los em uma nuvem de palavras
5• objetivo: Implementar um programa para gerar dados com nomes de pessoas e respectrivas pontuações,
gravar em um arquivo, recuperar os dados do arquivo, visualizar os dados das pontuações das pessoas
em um histograma e em uma nuvem de palavras
'''

# Importação de bibliotecas:
import wordcloud
import num2words
import matplotlib.pyplot as plt
from faker import Faker

# Geração dos dados:
# Declarando a varíavel para utilização dos métodos faker
fake = Faker('pt_BR')

# Declarando o dicionário que conterá os elementos
dicionario = {}

# Iterando uma criação de 10 nomes e 10 numéros de 1 a 10
for i in range(10):
  nome = fake.name()
  pontuacao = fake.random_int(1, 10)
# Retornando essa iteração no dicionario como as keys sendo o nome
# e os values sendo a pontuacao
  dicionario[nome] = pontuacao

# Gravaçao dos dados em arquivo de texto:
# Abrindo e escrevendo o arquivo
with open('teste1.txt', 'w') as arquivo:
# Iterando o par chave-valor com um loop for e o método items()
  for key, value in dicionario.items():
# Escrevendo o resultado da iteração dentro do arquivo
# com os pares convertidos em string para o método write funcionar
    arquivo.write('%s -> %s\n' % (key, value))

# Recuperação dos dados em arquivo de texto:
# Declarando a string que receberá o conteúdo do arquivo
texto = ''
# Abrindo e lendo o arquivo
with open('teste1.txt', 'r') as arquivo:
# Iterando o arquivo
  for line in arquivo.readlines():
# Recuperando o conteúdo na string
    texto += line + '\n'
print(texto)
# Declarando a lista que receberá os valore numéricos da string
numeros = []
# Iterando a string
for word in texto:
# Verificando a existência de dígitos
  if word.isdigit():
# Adicionando os dígitos na lista e convertendo em inteiros
    numeros.append(int(word))
print(numeros)

# Imprimindo o histograma a partir dos dados da lista de inteiros
# Usando a biblioteca matplotlib.pylplot
num_bins = 25; plt.hist(numeros, num_bins, density=True, facecolor='blue', alpha=0.75)

plt.xlabel('Valores')
plt.ylabel('Probabilidade')
plt.title('Histograma dos valores')
plt.grid(True)
plt.show()

# Declarando a string que receberá a lista de inteiros convertidos para
# funcionar o metodo wordcloud
palavras = ''
# Iterando a conversão dos números em palavras com o método num2words
# e concatenando na string, separados por vírgula
for i in numeros:
  palavras += num2words.num2words(i, lang='pt') + ','
print(palavras)

# Imprimindo a nuvem de palavras usando a biblioteca wordcloud
nuvem_palavras = wordcloud.WordCloud(background_color='blue', width=1200,height=800).generate(palavras)
plt.imshow(nuvem_palavras, interpolation='bilinear')
plt.axis("off")
nuvem_palavras.to_file("Nuvem de palavras.png")