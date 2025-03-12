def exercicio1():
    print("########## Exercício 1 ##########")
    print("Faça um programa que exiba seu nome na tela")
    print("Henrique Augusto Cruz")
    print(" ")

def exercicio2():
    print("########## Exercício 2 ##########")
    print("Escreva um programa que exiba o resultado de 2a x 3b, em que a vale 3 e b vale 5.")
    a = 2
    b = 3
    print((2 * a) * (3 * b))
    print(" ")

def exercicio3():
    print("########## Exercício 3 ##########")
    print("Escreva um programa que calcule a soma de três variáveis e imprima o resultado na tela.")
    c = 1
    d = 4
    e = 7
    print(c + d + e)
    print(" ")

def exercicio4():
    print("########## Exercício 4 ##########")
    print("Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.")
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    print(num1 + num2)
    print(" ")

def exercicio5():
    print("########## Exercício 5 ##########")
    print("Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.")
    valorEmMetros = float(input("Digite o valor em metros: "))
    print(f"{valorEmMetros} m -> {valorEmMetros * 1000} mm")
    print(" ")

def exercicio6():
    print("########## Exercício 6 ##########")
    print("Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.")
    dias = int(input("Digite a quantidade de dias: "))
    horas = int(input("Digite a quantidade de horas: "))
    minutos = int(input("Digite a quantidade de minutos: "))
    segundos = int(input("Digite a quantidade de segundos: "))
    total_segundos = dias * 86400 + horas * 3600 + minutos * 60 + segundos
    print(f"Total em segundos: {total_segundos}")
    print(" ")

def exercicio7():
    print("########## Exercício 7 ##########")
    print("Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.")
    salario = float(input("Digite o salário: "))
    aumento = float(input("Digite o percentual de aumento: "))
    valor_aumento = salario * aumento / 100
    novo_salario = salario + valor_aumento
    print(f"Valor de Aumento: R$ {valor_aumento:.2f}")
    print(f"Novo Salário: R$ {novo_salario:.2f}")
    print(" ")

def exercicio8():
    print("########## Exercício 8 ##########")
    print("Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.")
    precoMercadoria = float(input("Digite o preço da mercadoria: "))
    desconto = float(input("Digite o percentual de desconto: "))
    valor_desconto = precoMercadoria * desconto / 100
    preco_final = precoMercadoria - valor_desconto
    print(f"Valor de Desconto: R$ {valor_desconto:.2f}")
    print(f"Preço a pagar: R$ {preco_final:.2f}")
    print(" ")

def exercicio9():
    print("########## Exercício 9 ##########")
    print("Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.")
    distancia = float(input("Informe a distância (em Km) a percorrer: "))
    velocidadeMedia = float(input("Informe a velocidade média (em Km/h) esperada para a viagem: "))
    tempo = distancia / velocidadeMedia
    print(f"Tempo estimado de viagem: {tempo:.2f} horas")
    print(" ")

def exercicio10():
    print("########## Exercício 10 ##########")
    print("Escreva um programa que converta uma temperatura digitada em ºC em ºF. A fórmula para essa conversão é `F = ((9 x C) / 5) + 32`")
    celsius = float(input("Informe a temperatura em ºC: "))
    farenheit = ((9 * celsius) / 5) + 32
    print(f"A temperatura em ºF é: {farenheit:.2f}")
    print(" ")

def exercicio11():
    print("########## Exercício 11 ##########")
    print("Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.")
    kmPercorrido = float(input("Informe a quantidade de Km percorrido: "))
    diarias = int(input("Digite a quantidade de diárias: "))
    valorAluguel = kmPercorrido * 0.15 + diarias * 60
    print(f"O valor do aluguel do carro é R$ {valorAluguel:.2f}")
    print(" ")

def exercicio12():
    print("########## Exercício 12 ##########")
    print("Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule o valor de z: z = (x**2 + y**2) / (x-y)**2")
    x = int(input("Informe o valor de x: "))
    y = int(input("Informe o valor de y: "))
    z = (x**2 + y**2) / (x - y)**2
    print(f"O valor de Z é {z}")
    print(" ")

def exercicio13():
    print("########## Exercício 13 ##########")
    print("Escreva um programa que receba o salário de um funcionário (float) e retorne o resultado do novo salário com reajuste de 35%.")
    salarioFuncionario = float(input("Informe o valor do salário: "))
    novoSalario = salarioFuncionario + (salarioFuncionario * 0.35)
    print(f"O novo valor do salário com 35% de reajuste é R${novoSalario:.2f}")
    print(" ")

# Chamando as funções para execução
exercicio1()
exercicio2()
exercicio3()
exercicio4()
exercicio5()
exercicio6()
exercicio7()
exercicio8()
exercicio9()
exercicio10()
exercicio11()
exercicio12()
exercicio13()