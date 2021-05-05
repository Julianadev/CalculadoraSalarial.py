

def linha():
	linha = ("*"*35)
	return linha

print(linha())

hora = float(input(f"Quanto você ganha por hora: R$ "))
mes = float(input(f"Quantas horas você trabalha por mes: "))
resultado = (hora * mes)

print(linha())
print(f'Seu Salário Bruto no final do mês é R$ {resultado}')
print(linha())

ir = (11 * resultado)/100
inss = (8*resultado)/100
sindicato = (5*resultado)/100

print("Descontos: \n"
	f"Imposto de Renda - 11% = R$ {ir}\n"
	f"Imposto - 8% = R$ {inss} \n"
	f"Sindicato - 5% = R$ {sindicato}" 
	)
print(linha())
print(f"Total de decontos - R$ {ir + inss + sindicato}")
print(linha())
print(f"Com os descontos mensais seu salário liquido no final do mês é de R$ {resultado - ir - inss- sindicato}")
print("*"*75)



