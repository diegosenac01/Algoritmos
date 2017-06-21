'''Faça um jogo de forca...
o sistema deve escolher aleatoriamente uma lista de nomes, como por exemplo, nome dos meses..
O usuário terá só poderá errar 6 vezes, E o programa encerra
a cada acerto deve aparecer a letra na posição correspondente do nome.
quando for digitada todas as letras do nome o sistema deve informar a mensagem: VENCEDOR! '''
passe = str('japao')
chave = []
resposta = []
tentativa = 6
acertou = []
v = 0
for x in range(len(passe)):
  resposta.append('-')
  chave.append(passe[x])

print('Resposta',len(resposta))


while len(acertou) != len(chave) and tentativa > 0:
  letra=str(input('letra: '))
  for x in range(len(chave)):
    if letra == chave[x]:
      resposta[x] = chave[x]


  print('Palavra: ',resposta)



while len(passe) != len(resposta) and tentativa > 0:
 letra = str(input('Digite uma letra: '))
 acerto = False
 for x in range(len(passe)):
   if letra == passe[x]:
     resposta.insert(x,letra)
     acerto = True
 if acerto != True:
   tentativa -= 1
 print('Você ainda possui: ',tentativa,' tentativas')

print('Parabens a palavra correta é ', passe)

