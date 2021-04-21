m = float (input ('Digite o metro:'))

c = 100
mi = 1000

print ('Dentro de {} metros tem {:.0f} centímetros e {:.0f} milímetros!' .format(m, c*m, mi*m))


m = float (input ('Digite o metro:'))

dm = m*10
cm = m*100
mm = m*1000
km = m*0.001
hm = m*0.01
dam = m*0.1

print ('Dentro de {} metros tem {} decímetros, {} centímetros e {} milímetros' .format(m, dm, cm, mm))
print ('{} quilômetros, {} hectômetros e {} decâmetros!' .format(km, hm, dam))
