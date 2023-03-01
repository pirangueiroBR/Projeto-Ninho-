'''''''''
num = int(input('Digite um número para ver sua tabuada: '))
print('{} x {} = {}'.format(num,1,num*1))
print('{} x {} = {}'.format(num,2,num*2))    
print('{} x {} = {}'.format(num,3,num*3))
print('{} x {} = {}'.format(num,4,num*4))
print('{} x {} = {}'.format(num,5,num*5))
print('{} x {} = {}'.format(num,6,num*6))
print('{} x {} = {}'.format(num,7,num*7))
print('{} x {} = {}'.format(num,8,num*8))
print('{} x {} = {}'.format(num,9,num*9))
print('{} x {} = {}'.format(num,10,num*10))
'''''''''
'''''''''
listanum = []
mai = 0
men = 0
for c in range (0,5):
    listanum.append(int(input(f'Digite um valor para a posção {c}: ')))
if c == 0:
    mai = men = listanum[c]
else:
    if listanum[c] > mai:
        mai = listanum[c]
    if listanum[c] < men:
        men = listanum 

print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end= '')
print(f'O menor  valor digitado foi {men} nas posições', end= '')
for i,v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='' )

print()
'''''''''
'''''''''
n=int(input("Digite um número positivo e inteiro: "))
soma = 0
if n > 0:
  for i in range(n+1):
    soma = soma + i
    print("para n = ",i," a soma é: ", soma)
  print("Pronto! A soma dos ",n," primeiros números naturais é: ",soma)
elif n < 0:
  print("Somente para números positivos!")
'''''''''

