# Desafio proposto pelo professor: Crie um programa que calcule o abastecimento de um veiculo, sendo que o prelo é R$ 4,00 p/litro

abastecimento = float(input("Digite a quantidade de litros que deseja abastecer: "))

preco = 4.00

calculo = abastecimento * preco

print ("O valor do abastecimento deu R${}".format(calculo))