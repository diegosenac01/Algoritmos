n1=int(input("Digite o primeiro numero : "))
n2=int(input("Digite o segundo numero: "))
n3=int(input("Digite o terceiro numero: "))
operacao=int(input("Qual tipo de operação deseja efetuar ? 1 - soma, 2 - saber o maior numero, 3 - saber o menor numero, 4 - media:  "))
media=0
maior=0
menor=0
if operacao == 1:
    soma=n1+n2+n3
    print("soma: ",soma)
elif operacao == 4:
    media=(media+n1+n2+n3)/3
    print("media: ", media)
elif operacao==2:
    if (n1 > n2) and (n1 > n3):
        print ("maior: ", n1)
