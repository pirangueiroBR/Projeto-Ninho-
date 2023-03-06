'''''''''
def num_cascate1(n):
    for x in range(1,n+1):
        print(end ='\n')
        for y in range(1,n+1):
            if x >= y:
                print(x, end ='')
num_cascate1(5)
'''''''''
'''''''''
def num_cascate2(n):
    for x in range(1,n+1):
        print(x , end ='\n')
        if x == n:
            break
        else:
            for y in range(1,n+1):
                if x >= y:
                    print(y, end='')
num_cascate2(9)
'''''''''
'''''''''
def sum_mult(a,b,c):
    return a+b+c,a*b*c
sum_, mult = sum_mult(10,20,30)
print(sum_)
print(mult)
'''''''''
'''''''''
def sequencia_4(numero):
    if numero >0:
    print(char)

     else:
     char = 'N'
     print(char)
#numero = int(input("Digite um número qualquer: "))
#sequencia_4(numero)
'''''''''
'''''''''
def somaImposto(taxaImposto, custo):
    #cálculo do imposto.
    resultado_imposto = custo + (custo * taxaImposto / 100)
    #retorno do resultado do imposto
    return resultado_imposto
'''''''''
def valor_por_omissao(valor):
    if valor=='':
        return int(1)
    else:
        return faixa_minima_maxima(int(valor))

def faixa_minima_maxima(valor):
    if valor<1:
        return 1
    elif valor>20:
        return 20
    else:
        return valor

def cria_linha(linha):
    l='+'
    for x in range(linha):
        l+='-'
    l+='+'
    print (l)

def cria_coluna(linha, coluna):
    for y in range(coluna):
        c='|'
        c+= ' '*linha
        c+='|'
        print (c)

def desenha_moldura(linha, coluna):
    cria_linha(linha)
    cria_coluna(linha, coluna)
    cria_linha(linha)

linha=input('Diga quantos +----+, entre 1 e 20: ')
coluna=input('Diga quantos |    |, entre 1 e 20: ')
desenha_moldura(valor_por_omissao(linha), valor_por_omissao(coluna))

