num=[]
par=[]
imp=[]
i=0
j=0
x=0
print("carregue o vetor")
while i < 6:
    num.append(int(input("")))
    if num[i] % 2 == 0:
        par.append(num[i])
    else:
        imp.append(num[i])
    i=i+1
print(par)
print(imp)
print(num)
