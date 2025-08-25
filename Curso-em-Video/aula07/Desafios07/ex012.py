# Desafio proposto: Faça um algoritmo que leia o preço de um produto e mostre o novo preço, com 5% de desconto

produto = float(input("Digite o valor do Produto: "))

desconto = produto - (produto / 100 * 5)

print("O produto que custava: R${} com um desconto aplicado de 5agora custa R${:.2f} ".format(produto, desconto))