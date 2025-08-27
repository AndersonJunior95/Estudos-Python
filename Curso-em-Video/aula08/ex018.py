# Desafio proposto: Faça um programa que leia um ângulo qaulquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input("Digite o Ângulo: "))

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print("De acordo com o Ângulo {} \n Seno: {:.2f} \n Cosseno: {:.2f} \n Tangente: {:.2f}".format(angulo, seno, cosseno, tangente))