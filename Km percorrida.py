'''Um programa que o usuário informe a Km percorrida e a quantidade de litros abastecidas, o sistema informe o consumo do veículo.'''
consumo=0
km=int(input("Informe quantos quilometros foram percorrido"))
litro=int(input("Informe quantos litros foram consumidos"))
consumo=km/litro
print("O consumo médio é ",consumo,"km/l")
