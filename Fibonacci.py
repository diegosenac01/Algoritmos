'''A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.'''
fn=int(input("Digite um numero para saber a sequencia fibonacci : "))
z=1
j=1
f=1
i=1
print (j)
for  i in range (fn):
    if f <= fn:
        print (f)
        f= z+j
        j=z
        z=f
