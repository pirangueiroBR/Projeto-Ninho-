'''''
1. Escreva um programa Python para clonar ou copiar uma lista
original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
print(original_list)
print(new_list)
'''''''''
'''''''''
2.Escreva um programa Python para encontrar a lista de palavras com mais de n em uma determinada lista de palavras
def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
print(long_words(3, "Micael é uma pessoa de coração de pedra"))
'''''''''
'''''''''
3.Escreva uma função Python que receba duas listas e retorne True se elas tiverem pelo menos um membro comum
def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))
'''''''''

'''''''''
4.Escreva um programa em Python para imprimir os números de uma lista especificada depois de remover dela os números pares.
num = [7,8, 120, 25, 44, 20, 27]
num = [x for x in num if x%2!=0]
print(num)
'''''''''
'''''''''
5.Escreva um script Python para concatenar os seguintes dicionários para criar um novo.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)
'''''''''
'''''''''
6.Escreva um script Python para verificar se uma determinada chave já existe em um dicionário.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)
'''''''''
'''''''''
7.Escreva um script Python para verificar se uma determinada chave já existe em um dicionário.
n=int(input(" Digite o número: "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d) 
'''''''''
'''''''''
8.Escreva um programa Python para criar uma tupla de números e imprimir um item.
#Cria uma tupla com números
tuplex = 5, 10, 15, 20, 25
print(tuplex)
#Cria uma tupla de um item
tuplex = 5,
print(tuplex)
'''''''''
'''''''''
9.Escreva um programa Python para obter o quarto elemento do último elemento de uma tupla
#Obter um item da tupla
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print(tuplex)
#Pega o item (4º elemento) da tupla pelo índice
item = tuplex[3]
print(item)
#Obter item (4º elemento do último) por índice negativo
item1 = tuplex[-4]
print(item1)
'''''''''
'''''''''
Escreva um programa Python para encontrar o comprimento de uma tupla.
#cria uma tupla
tuplex = tuple("w3resource")
print(tuplex)
#use a função len() para saber o comprimento da tupla
print(len(tuplex))
'''''''''