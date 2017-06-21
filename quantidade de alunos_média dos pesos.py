'''7) Faça um programa que o usuário informe a quantidade de alunos de uma turma, o sistema deve
ler o peso e altura de cada aluno, ao final informar a média dos pesos, alturas e imc.
8) o programa anterior, deve informar ao final o aluno com maior e menor imm'''
imc=0
mediaaltura=0
mediapeso=0
somaaltura=0
somapeso=0
altura=0
peso=0
i=1
aluno=int(input("informe a quantidade de alunos"))
for i in range (aluno):
    peso=float(input("informe o peso do aluno",))
    somapeso=somapeso+peso
    altura=int(input("informe a altura do aluno",))
    somaaltura=somaaltura+altura
    i=i+1
mediapeso=(mediapeso+somapeso)/aulo
mediaaltura=(mediaaltura+somaaltura)/aluno
imc=(somapesopeso/(somaaltura*somaaltura))/aluno
print("media dos pesos", mediapeso)
print("media das alturas", mediaaltura)
print("media dos imc", imc)
