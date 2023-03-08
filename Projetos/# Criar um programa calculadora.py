# Criar um programa calculadora
    # Recebe dois números e uma operação (+,-,/,*)
    # Dependendo da opreção escolhida, passa os números 
    # Para uma dsas funções
    # No final impreme o resultado e a função escolhiada

# Criar função para soma 
# Criar função para subtração 
# Criar função para multiplicação 
# Criar função para divisão

valor1 = int(input("Informe o primero número: "))
valor2 = int(input("Informe o segundo número: "))
print("-> Soma : +")
print("-> subtração: -")
print("-> Multiplicação: *")
print("-> divisão: /")
operacao = input("Informe a Operação com os sinais a cima: ")
resultado = 0

if(operacao == '+'):
  resultado = valor1 + valor2
elif(operacao == '-'):
  resultado = valor1 - valor2
elif(operacao == '*'):
  resultado = valor1 * valor2
elif(operacao == '/'):
  resultado = valor1 / valor2
else:
  print(":( Houve algum ERRO!!! Reinicie o programa.")
  
print(valor1,operacao,valor2,'=',resultado)