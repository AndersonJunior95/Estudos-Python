# Desafio proposto: Conversor de Medidas pegar a distância em metros e converter dentre as medidas que foram passadas pelo professor

metros = float(input("Uma distância em metros: "))

print("A medida de {}m corresponde a".format(metros))

km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print("{}km".format(km))
print("{}hm".format(hm))
print("{}dam".format(dam))
print("{:.0f}dm".format(dm))
print("{:.0f}cm".format(cm))
print("{:.0f}mm".format(mm))