n = input ('Digite o nome do aluno:')
p = float (input ('Digite a nota de português:'))
m = float (input ('Digite a nota de matemática:'))
#s = p+m
s = (p+m)/2

#print ('A média escolar do {} é {}!' .format(n, s/2))
#print ('A média escolar do {} é {}!' .format(n, s))
print ('A média escolar do {} é {:.1f}!' .format(n, s))
