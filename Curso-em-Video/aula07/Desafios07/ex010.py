# Desafio proposto: Criar um programa que leia o valor disponível na carteira de uma pessoa em reais e exiba quantos dólares ela poderia obter na conversão.

carteira = float(input("Quanto dinheiro você tem na carteira? "))

conversao = carteira / 5.42

print ("Com R${:.2f} você obtém US${:.2f}".format(carteira, conversao))