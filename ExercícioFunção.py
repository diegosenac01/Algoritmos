n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))
n3=int(input("Digite o segundo número: "))
op=int(input("Selecione uma das opções = Soma [1] - Maior [2] - Menor [3] - Media [4]:"))

def exibe1(a,b,c):
    return(a+b+c)

def exibe2(a,b,c):
    return(a+b+c/3)

def exibe3(a,b,c):
    if n1>n2 and n1>n3:
           M=n2
    if n2>n1 and n2>n3:
           M=n2
    if n3>n1 and n3>n2:
           M=n3
    return(M)

def exibe4(a,b,c):
    if n1<n2 and n1<n3:
         m=n1
    if n2<n1 and n2<n3:
         m=n2
    if n3<n1 and n3<n2:
         m=n3
    return(m)


r01=exibe1(n1,n2,n3)
s01=exibe2(n1,n2,n3)
p01=exibe3(n1,n2,n3)
q01=exibe4(n1,n2,n3)

if op==1:
    print("A soma dos 3 números é: ",r01)
if op==2:
    print ("O maior número é: ",p01)
if op==3:
    print("O menor número é: ",q01)
if op==4:
    print("A média é",s01)
