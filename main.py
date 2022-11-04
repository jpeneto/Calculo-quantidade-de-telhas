largura = float(input("Digite a largura do telhado com beiral "))
comprimento = float(input("Digita o comprimento do telhado com beiral "))
inclinacao = float(input("Digite a inclinação do telhado "))

valor_fc = {0:1.000, 5:1.001, 10:1.005, 15:1.011, 20:1.020, 25:1.031, 30:1.044, 35:1.059, 40:1.077, 45:1.097, 50:1.0118, 55:1.141, 60:1.166, 70:1.221, 75:1.250,
      80:1.281, 85:1.312, 90:1.345, 95:1.379, 100:1.414}

fc = valor_fc[inclinacao]

inclinacao =  inclinacao / 100 #(inclinacao /= 100)


area = (largura * comprimento) * fc
print(f"Area = {area:.3f}" )

R = float(input("Digite o rendimento da telha por metro quadrado conforme especificado pelo fabricante "))
# calcula a quantidade de telhas:

Qt = int(area * R)

print(f"Quantidade de telhas = {Qt}")