n=0
maior=0
menor=99999
x=0
while x < 10:
	n=int(input ("entre com um numero"))
	x=x+1
	if n >maior:
		maior=n
	if n <= menor:
		menor=n
print("o maior numero é: ",maior)
print("o menor numero é: ",menor)

