'''Informe o tipo de triangulo com os dados informados pelo usuário'''
base=int(input("Digite o tamanho da base: "))
lado1=int(input("Digite o tamanho do lado direito: "))
lado2=int(input("Digite o tamanho do lado esquerdo: "))
if (base == lado1) and (lado2 == lado1):
    print (" Esse triangulo é Equilatero ")
elif (lado1 == lado2) or (base == lado1) or (base == lado2):
    print (" Esse triangulo é Isosceles")
elif (base != lado1) and (lado1 != lado2) and (base != lado2):
    print(" Esse triangulo é Escaleno")
print ()
