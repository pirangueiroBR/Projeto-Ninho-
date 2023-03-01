'''''''''''
idade = int(input('Digite sua idade: '))
if idade >= 10 and idade <20: 
    print('Você é adolescente')
elif idade >= 20 and idade < 30 :
    print('Você é jovem')
elif idade >= 30 and idade <= 100:
    print('Você é adulto')
else:
    print('Valor não encontrado!') 
'''''''''
'''''''''
a = int(input('Digite um número A: '))
b = int(input('Digite um número B: '))
c = int(input('Digite um número C: '))

if  a+b<c:
    print(f"{a} + {b} e menor que {c}")
else: 
    print(f"A soma não é igual a{c}")
'''''''''
'''''''''
numero = float(input('Digite um número para saber se é par ou impar'))
resto = numero %2

if resto == 0:
    print('Número é par')
else:
    print('Número é impar')
'''''''''''

'''''
a = int(input('Digite um número A: '))
b = int(input('Digite um número B: '))

if  a==b:
    soma = a + b
    print(f"Soma= {soma}")
else: 
    mult = a*b
    print(f"Multiplicação = {mult}")
'''''''''

'''''''''
a = float(input('Escreva um número: '))
b = float(input('Escreva um número: '))
c = float(input('Escreva um número: '))

if a >= b and a >= c and b >= c:
    print(f'A ordem decrescente é {a} , {b} e {c}')
elif a >= b and a >=c and c >= b:
    print(f'A ordem decrescente é {a} , {c} e {b}')
elif b >= a and b >= c and a >= c:
    print(f'A ordem decrescente é {b} , {a} e {c}')
elif b >= a and b >= c and c >= a:
    print(f'A ordem decrescente é {b} , {c} e {a}')
elif c >= a and c >= b and a >=b:
    print(f'A ordem decrescente é {c} , {a} e {b}')
elif c >= a and c >= b and b >= a:
    print(f'A ordem decrescente é {c} , {b} e {a}')
'''''

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))

média = (nota1 + nota2 + nota3) / 3
print('Tirando {:.1f} e {:.1f} e {:.1f} a média do aluno é {:.1f}' .format (nota1, nota2, nota3, média ))
if 7 >média >= 5:
    print('O aluno está em RECUPERAÇÃO. ')
elif média < 5:
    print('O aluno está REPROVADO. ')
elif média >= 7:
    print('O aluno está APROVADO')