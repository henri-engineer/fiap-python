print("########## Exercício 1 ##########")
print("Faça um programa que exiba seu nome na tela")
print("Henrique Augusto Cruz")
a = 2
b = 3
print(" ")
print("########## Exercício 2 ##########")
print("Escreva um programa que exiba o resultado de 2a x 3b, em que a vale 3 e b vale 5.")
print((2*a)*(3*b))
print(" ")
print("########## Exercício 3 ##########")
print("Escreva um programa que calcule a soma de três variáveis e imprima o resultado na tela.")
c = 1
d = 4
e = 7
print(c+d+e)
print(" ")
print("########## Exercício 4 ##########")
print("Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela.")
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
print(num1+num2)
print(" ")

print("########## Exercício 5 ##########")
print("Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.")
valorEmMetros = float(input("Digite o valor em metros "))
print(valorEmMetros,"m -> ", valorEmMetros*1000,"cm")
print(" ")

print("########## Exercício 6 ##########")
print("Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.")
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
print("Total em segundos: ",dias*86400 + horas*3600 + minutos*60 + segundos)
print(" ")

print("########## Exercício 7 ##########")
print("Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.")
salario = float(input("Digite o salário: "))
aumento = float(input("Digite o percentual de aumento: "))
print("Valor de Aumento: R$", salario*aumento/100)
print("Novo Salário: R$",salario+(salario*aumento/100))
print(" ")

print("########## Exercício 8 ##########")
print("Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.")
precoMercadoria = float(input("Digite o preço da mercadoria: "))
desconto = float(input("Digite o percentual de desconto: "))
print("Valor de Desconto: R$", precoMercadoria*desconto/100)
print("Preço a pagar: R$", precoMercadoria-(precoMercadoria*desconto/100))
print(" ")

print("########## Exercício 9 ##########")
print("Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.")
distancia = float(input("Informe a distância (em Km) a percorrer: "))
velocidadeMedia = float(input("Informa a velocidade média (em Km/h) espearada para a viagem: "))
tempo = distancia / velocidadeMedia
print("Tempo estimado de viagem: %.2f" %tempo, "horas")
print(" ")

print("########## Exercício 10 ##########")
print("Escreva um programa que converta uma temperatura digitada em ºC em ºF. A fórmula para essa conversão é `F = ((9 x C) / 5) + 32`")
celsius = float(input("Informe a temperatura em ºC: "))
farenheit = ((9*celsius)/5)+32
print("A temperatura em ºF é: %.2f" %farenheit)
print(" ")

print("########## Exercício 11 ##########")
print("Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.")
kmPercorrido = float(input("Informe a quantidade de Km percorrido: "))
diarias = int(input("Digite a quantidade de diárias: "))
valorAluguel = kmPercorrido*0.15 + diarias * 60
print("O valor do aluguel do carro é R$%.2f" %valorAluguel)
print(" ")

print("########## Exercício 12 ##########")
print("Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule o valor de z: z = (x**2 + y**2) / (x-y)**2`")
x = int(input("Informe o valor de x: "))
y = int(input("Informe o valor de y: "))
z = (x**2 + y**2) / (x-y)**2
print("O valor de Z é ",z)
print(" ")

print("########## Exercício 13 ##########")
print("Escreva um programa que receba o salário de um funcionário (float) e retorne o resultado do novo salário com reajuste de 35%.")
salarioFuncionario = float(input("Informe o valor do salário: "))
print("O valor do salário com 35% de reajuste é R$",salarioFuncionario+(salarioFuncionario*0.35))
print(" ")