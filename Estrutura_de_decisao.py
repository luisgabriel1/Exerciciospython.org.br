# Exercicio 1- Faça um Programa que peça dois números e imprima o maior deles.
# O outro jeito tbm seria :
'''
numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite mais um numero: '))
lista = [numero1, numero2]
print(f'O MAIOR É : {max(lista)}')

'''
# Tbm poderia usar for e in no lugar do While
x = 0
lista_num = []
while x <= 1:
    numeros_para_lista = int(input('Digite um numero : '))
    lista_num += [numeros_para_lista]
    x += 1
print(f'O MAIOR  NUMERO É : {max(lista_num)}')
print(f'\n')


# Exercicio 2- Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
# O outro jeito seria:
'''
valor = float(input('Digite um valor: '))
if valor >= 1:
    print('É POSITIVO ')
elif valor == 0:
    print('ZERO É NEUTRO ')
else:
    print('É NEGATIVO ')

'''
valor = float(input('Digite um valor: '))
mensagem = 'É POSITIVO' if valor >= 1 else 'É NEGATIVO'
print(mensagem)
print(f'\n')


# Exercicio 3- Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# O outro jeito seria:
'''
pergunta = input('Informe F para Feminino\nInforme M para Masculino\nInforme: ').upper()
if pergunta == 'F':
    print('Sexo Feminino')
elif pergunta == 'M':
    print('Sexo Masculino')
else:
    print('Sexo Inválido')


'''
pergunta = input('Informe F para Feminino\nInforme M para Masculino\nInforme: ').upper()
sexo, sexo1 = 'Sexo Inválido'if pergunta != 'F' and 'M' else 'Sexo Feminino', 'Sexo Masculino'if pergunta == 'M' else 'Sexo Inválido',
if pergunta == 'F':
    print(sexo) 
else:
    print(sexo1)
print(f'\n')


# Exercicio 4- Faça um Programa que verifique se uma letra digitada é vogal ou consoante
letra = input('Digite uma letra: ').upper()
vogal = ['A', 'E', 'I', 'O', 'U', 'ÃO', 'AO']
verificacao = 'É vogal' if letra in vogal else 'É consoante'
print(verificacao)
print(f'\n')


# Exercicio 5- Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1, nota2 = int(input('Informe a primeira nota: ')), int(input('Informe a segunda nota: '))
calculo_media = (nota1 + nota2) // 2
if calculo_media == 10:
    print('Aprovado com Distinção')
elif calculo_media >= 7:
    print('Aprovado')

else: 
    print('Reprovado')