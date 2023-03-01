'''''''''
l=int(input("Digite a largura: "))
a=int(input("Digite a altura: "))

linha=0
coluna=0

while linha<a:
    while coluna<l:
        print("#", end=" ")
        coluna=coluna+1
    print()    
    linha=linha+1
    coluna= 0 
'''''''''

núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[31m', end= '')
        tot += 1
else:
    print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n\033[m0 número {} foi divisível {} vezes'. format(núm,tot))
if tot == 2:
    print('E por isso ele é PRIMO! ')
else:
    print('E por isso ele NÃO É PRIMO !')
