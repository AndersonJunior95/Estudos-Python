# Desafio proposto pelo professor: Uma revendedora de carros usados paga seus funcionarios(vendedores) um salário fixo por mês, mais uma comissão fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuada. Escreva um algoritmo que leia o número de carros por ele vendido, total de suas vendas, o salário fixo que ele recebe por carro vendido, calcule e escreva o salário recebido pelo vendedor

'''

carrosVendidos = int(input("Digite a quantidade de carros vendidos: "))
totalVendas = float(input("Digiteo o valor dos carros vendidos: "))
salarioFixo = float(input("Digite o salário fixo: "))
comissaoCarro = int(input("Digite a comissão fixa: "))

comissaoTotal = comissaoCarro * carrosVendidos

percentual = totalVendas * 0.05

salarioTotal = salarioFixo + percentual + comissaoTotal

print ("O salário deu {:.2f}".format(salarioTotal))

'''

valFixo = 150
valVendasCarro = 10000
nome = ""
qtdCarro = 0
salario = 0
com1 = 0
com2 = 0

nome = input("Digite o nome do funcionário. \n Nome: ")
salario = float(input("Digite o salário desse funcionário \n Salário: "))
qtdCarros = int(input("Digite quantos carros que o funcionário vendeu. \n Qunatidade: "))


valVendas = qtdCarros * valVendasCarro
com1 = qtdCarros * valFixo
com2 = (qtdCarros * valVendasCarro) * 0.05
salarioFinal = salario + com1 + com2

print (f"Funcionário: {nome} \nSalário: {salario} \nQuantidade de carros vendidos: {qtdCarro} \n Salário Final: {salarioFinal}")