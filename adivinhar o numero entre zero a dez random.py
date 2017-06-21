from random import randint
n1=randint(0, 10)
print(n1)
n2=int(input("tente adivinhar o numero entre zero a dez: "))
i=1
j=1
for j: 1 to 10 do
    i= i + 1
    if n1 < n2:
        print ("o numero da tentativa é menor")
        n2=int(input("tente adivinhar o numero: "))
    elif n1 > n2:
        print ("o numero da tentativa é maior")
        n2=int(input("tente adivinhar o numero: "))
print ("acertou")
print ("Quantidade de vezes que foram necessárias para acerta: ",i)
