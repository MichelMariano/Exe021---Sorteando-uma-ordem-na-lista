# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.

import random

n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
n5 = str(input('Quinto Aluno: '))

lista = [n1, n2, n3, n4, n5]

random.shuffle(lista)     #.shuffle significa: embaralhar

print('A ordem de apresentação será: ')
print(lista)
