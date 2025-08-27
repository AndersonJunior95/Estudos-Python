# As maças custam R$1,30 se forem comprada menos de uma dúzia, e R$ 1,00 se forem compradas pelos menos 12. Escreva um programa que leia o número de maças compradas. calcule e e escreva o custo total da compra.

print("="*20, "OLHA A FEIRA!!!", "="*20)

n1 = int(input("Digite maças você deseja comprar \n Maças: "))

if n1 <= 11:
    total = n1 * 1.30
    print("="*20, "Vablor da Feira", "="*20)
    print(f"As maças custaram \nR${total}")
else:
    total = n1 * 1.00
    print("="*20, "Valor da Feira", "="*20)
    print(f"As maças custaram \nR${total}")