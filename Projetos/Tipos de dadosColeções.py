'''''''''
Dado o nome de uma pessoa, retorne o número de letras do nome e a primeira
letra do nome.
n = str(input('Digite seu completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
'''''''''
'''''''''
Dada uma palavra, retorna a palavra invertida
frase = input('Digite uma frase: ')
print(' Você digitou: {}'.format(frase))
invertida = ' '.join(palavra[::-1] for palavra in frase.split())
print('A frase que você digitou invertida fica: {}'.format(invertida))
'''''''''

palavra = list('trevas')

palavra.reverse()

print(''.join(palavra))