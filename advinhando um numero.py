
n1=int(input("Digite um numero entre zero e dez: "))
n2=int(input("tente adivinhar o numero: "))
i=1
while n1!=n2:
    i= i + 1
    if n1 < n2:
        print ("o numero da tentativa é menor")
        n2=int(input("tente adivinhar o numero: "))
    elif n1 > n2:
        print ("o numero da tentativa é maior")
        n2=int(input("tente adivinhar o numero: "))
print ("acertou")
print ("Quantidade de vezes que foram necessárias para acerta: ",i)
