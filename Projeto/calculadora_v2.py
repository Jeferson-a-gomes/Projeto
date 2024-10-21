#Trabalho Prático: calculadora utilizando os conceidos de condição, repetição e funções
#função para armazenar a expressão
def digValores():
    global valor1
    global expressao
    global valor2
    valor1 = int(input("digite o primeiro valor:"))
    expressao = input("Digite a expressão matemática entre (+ - / *):")
    valor2 = int(input("Digite o segundo valor que será utilizado no cálculo:"))
    print("você quer saber o resultado da expressão:", valor1, " ", expressao, " ", valor2)
#função para validar as informaçoes
def validaNum ():
    global valor1
    global expressao
    global valor2
    if expressao not in['+','-','*','/','x','X']:
        print("Você não digitou uma expressão matemática válida, refaça os cálculos.")
        digValores()
    else:
        print ("Expressão válida!")
#função para calcular a expressão
def calcular ():
    global valor1
    global expressao
    global valor2
    if expressao in ['+']:
        resultado = (valor1 + valor2)
    elif expressao in '-':
        resultado = (valor1 - valor2)
    elif expressao in ['/']:
        resultado = (valor1 / valor2)
    elif expressao in ['*','x','X']:
        resultado = (valor1 * valor2)
    return resultado
#Iniciando o programa da calculadora
valor1=0
valor2=0
expressao=''
valorFinal=0
refazer=''
input("Olá, dê um enter para iniciar a calculadora:")
while refazer != "sair":
    #função para digitar a expressão
    digValores()
    input("valores armazenados, dê um enter para validar se digitou algo errado: ")
    #função para validar a expressão
    validaNum()
    #função para calcular a expressão
    valorFinal=calcular()
    print("fim das contas, o resultado de",valor1,expressao,valor2,"=",valorFinal)
    refazer= input("Digite 'sair' para encerrar a calculadora")
print("Calculadora desligada")


