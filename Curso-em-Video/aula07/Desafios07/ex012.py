# Desafio proposto: Calcular desconto de um determinado produto

produto = float(input("Digite o valor do Produto: "))

desconto = produto - (produto / 100 * 5)

print("O produto que custava: R${} com um desconto aplicado de 5agora custa R${:.2f} ".format(produto, desconto))