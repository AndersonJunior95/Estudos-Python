# Desafio proposto: Faça um programa que leia a altura e largura de uma parede em metros e calcule a quantidade de tinta necessária para pintar a parede

altura = float(input("Qual a altura da parede? "))
largura = float(input("Qual a largura da parede? "))

parede = altura * largura

pintar = parede / 2

print("A sua parede tem {}²M".format(parede))
print("Para pintar a parede {}Litros de tinta".format(pintar))