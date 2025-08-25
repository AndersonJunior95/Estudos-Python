# Desafio proposto: Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

diasAlugel = int(input("Quantos dias alugados? "))
kmRodados = float(input("Quantos KM rodados? "))

resultado = (diasAlugel * 60) + (kmRodados * 0.15)

print("O total a pagar é R${}".format(resultado))