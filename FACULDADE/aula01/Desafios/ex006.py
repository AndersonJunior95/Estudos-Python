# Desafio proposto pelo professor: Uma revendedora de carros usados paga seus funcionarios(vendedores) um salário fixo por mês, mais uma comissão fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuada. Escreva um algoritmo que leia o número de carros por ele vendido, total de suas vendas, o salário fixo que ele recebe por carro vendido, calcule e escreva o salário recebido pelo vendedor

carrosVendidos = int(input("Digite a quantidade de carros vendidos: "))
totalVendas = float(input("Digiteo o valor dos carros vendidos: "))
salarioFixo = float(input("Digite o salário fixo: "))
comissaoCarro = int(input("Digite a comissão fixa: "))


comissaoTotal = comissaoCarro * carrosVendidos

percentual = totalVendas * 0.05

salarioTotal = salarioFixo + percentual + comissaoTotal

print ("O salário deu {:.2f}".format(salarioTotal))
