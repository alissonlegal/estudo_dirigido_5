'''5 - Calcula aumento salario(salário mínimo)
'''
def calcula(salario, percentual):
    valor_do_aumento = (salario / 100) * percentual

    salario_novo = salario + (salario / 100) * percentual

    mostrar_na_tela(salario, percentual, valor_do_aumento, salario_novo)

def mostrar_na_tela(salario, percentual, valor_do_aumento, salario_novo):
    print("O salário antes do reajuste era: %.2f." % (salario))

    print("O percentual de aumento foi de: %d%%." % (percentual))

    print("O valor do aumento foi de: %d." % (valor_do_aumento))

    print("O novo salrio ficou em: %.2f." % (salario_novo))

salario = float(input("Digite o salário: "))

if salario <= 724.00:
    calcula(salario, 20)

elif salario > 724.00 and salario <= 1448.00:
    calcula(salario, 15)

elif salario > 1448.00 and salario <= 3620.00:
    calcula(salario, 10)

else:
    calcula(salario, 5)