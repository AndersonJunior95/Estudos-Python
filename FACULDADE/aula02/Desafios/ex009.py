# Desafio Proposto: Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não pe necessário considerar o mês em que a pessoa nasceu).

n1 = int(input("Digite o ano atual: "))
n2 = int(input("Digite sua data de nascimento: "))

total = n1 - n2

if total >= 16:
    print(f"Você tem {total} anos e já pode votar")
else:
    print(f"Você ainda tem {total} anos e não pode votar")