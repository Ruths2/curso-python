real = float (input ('Quanto de dinheiro tem em sua carteira? \nR$'))
dolar = real/5.69
euro = real/6.78
print ('Considerando que o dolar está US$5,69 e o euro €6,78, você poderá comprar:\nUS${:.2f} dolares e €{:.2f} euros.' .format(dolar, euro, real))
