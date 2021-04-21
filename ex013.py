s = float (input ('Digite o seu salário: R$'))
#r = 115/100*s
r = s+s*15/100
print ('O seu salário de R${} com reajuste de 15% ficará no valor de R${:.2f}' .format(s, r))