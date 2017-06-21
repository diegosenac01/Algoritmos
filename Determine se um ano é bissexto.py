'''(3) - Determine se um ano é bissexto:
para ser bissexto, o ano deve ser:
	Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
	Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
	Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.'''
bissexto=int(input("Digite um ano para saber se é bissexto : "))
if (bissexto % 4 == 0) or (bissexto % 400 ==0):
    print ("esse ano é bissexto : ", bissexto)
else:
    print ("esse ano NÃO é bissexto : ", bissexto)
