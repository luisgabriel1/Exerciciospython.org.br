# Exercicio 1- Faça um Programa que peça dois números e imprima o maior deles.
# O outro jeito tbm seria :
'''
x = 0
lista_num = []
while x <= 1:
    numeros_para_lista = int(input('Digite um numero : '))
    lista_num += [numeros_para_lista]
    x += 1
print(f'O MAIOR  NUMERO É : {max(lista_num)}')
'''
# Tbm poderia usar While
numero1, numero2 = int(input('Digite um numero: ')), int(input('Digite mais um numero: '))
lista = [numero1, numero2]
print(f'O MAIOR É : {max(lista)}')
print('\n')


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
print('\n')


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
print('\n')


# Exercicio 4- Faça um Programa que verifique se uma letra digitada é vogal ou consoante
letra = input('Digite uma letra: ').upper()
vogal = ['A', 'E', 'I', 'O', 'U', 'ÃO', 'AO']
verificacao = 'É vogal' if letra in vogal else 'É consoante'
print(verificacao)
print('\n')


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
print('\n')


# Exercicio 6- Faça um Programa que leia três números e mostre o maior deles. 
tres_numeros = [3, 5, 7]
print(f'O maior é : {max(tres_numeros)}')
print('\n')


# Exercicio 7- Faça um Programa que leia três números e mostre o maior e o menor deles. 
tres_numeros_maior_menor = [3, 5, 7]
print(f'O maior é : {max(tres_numeros_maior_menor)}\nO menor é : {min(tres_numeros_maior_menor)}')
print('\n')
# Exercicio 8- Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
#O outro jeito seria: 
'''
preco1, preco2, preco3 = int(input('Informe o primeiro valor: R$ ')), int(input('Informe o segundo valor: R$ ')), int(input('Informe o terceiro valor: R$ '))
precos =  [preco1, preco2, preco3]
print(f'O mais barato é : R${min(precos)}')
print('\n')

'''
x, precos = 0, []
while x <= 2:
    preco = int(input('Informe os valores dos produtos : '))
    precos += [preco]
    x += 1
print(f'O mais barato é : R${min(precos)}')
print('\n')


# Exercicio 9- Faça um Programa que leia três números e mostre-os em ordem decrescente. 
numeros = [1, 2, 3]
print(numeros [::-1])
print('\n')


# Exercicio 10- Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. 
print('Qual turno você estuda ? ')
turnos = input('Envie M para MATUTINO\nEnvie V para VESPERTINO\nEnvie N para NOTURNO\nEnvie: ').upper()
if turnos == 'M':
    print('Bom Dia !')
elif turnos == 'V':
    print('Boa Tarde !')
elif turnos == 'N':
    print('Boa Noite !')
else:
    print('Valor Invalido')
print('\n')
