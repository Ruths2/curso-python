dias = int (input ('Quantos dias de aluguel? '))
km = float (input ('Quantos quilômetros foram rodados? '))
#pagar = (60 * dias) + (0.15 * km)
aluguel = 60 * dias
rodou = 0.15 * km
total = aluguel+rodou
print ('\nForam R${:.2f} em {} dias de aluguel \ne R${:.2f} em {} km rodados. \n\n*Um total de R${:.2f} a pagar*.' .format(aluguel, dias, rodou, km, total))
