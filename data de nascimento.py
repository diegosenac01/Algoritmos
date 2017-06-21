'''0. Faça um algoritmo que leia a data de nascimento(dia, mês e ano), e informe a idade correta'''
idade=0
dia=int(input("Digite o dia de seu nascimento "))
mes=int(input("Digite o mês de seu nascimento "))
ano=int(input("Digite o ano de seu nascimento "))
anoatual=int(input("Digite o ano atual "))
mesatual=int(input("Digite o mes atual "))
diaatual=int(input("Digite o dia atual "))
anofinal=0
if mes < mesatual:
    idade=idade+(anoatual-ano)
    print("sua idade: ",idade)
if mes >= mesatual:
    idade=1-(anoatual-ano)
    print("sua idade: ",idade)
if mes == mesatual and dia > diaatual :
    idade=idade+(anoatual-ano)
    print("sua idade: ",idade)
