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


# Exercicio 11- As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual: 
# - Salários até R$ 280,00 (incluindo) : aumento de 20% 
# - Salários entre R$ 280,00 e R$ 700,00 : aumento de 15% 
# - Salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# - Salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela: 
# * O salário antes do reajuste;
# * O percentual de aumento aplicado; 
# * O valor do aumento; 
# * O novo salário, após o aumento.
salario = float(input('Informe seu salario: '))
if salario <= 280:
    salario_1 = salario * 1.2
    print(f'Salario antes do reajuste: R${salario}\nPercentual de aumento aplicado: 20%\nO valor do aumento: R${salario * 0.2}\nSalario com o reajuste: R${salario_1}')
elif salario > 280 and salario < 700:
    salario_2 = salario * 1.15
    print(f'Salario antes do reajuste: R${salario}\nPercentual de aumento aplicado: 15%\nO valor do aumento: R${salario * 0.15}\nSalario com o reajuste: R${salario_2}')
elif salario >= 700 and salario < 1500:
    salario_3 = salario * 1.1
    print(f'Salario antes do reajuste: R${salario}\nPercentual de aumento aplicado: 10%\nO valor do aumento: R${salario * 0.1}\nSalario com o reajuste: R${salario_3}')
elif salario >= 1500:
    salario_4 = salario * 1.05
    print(f'Salario antes do reajuste: R${salario}\nPercentual de aumento aplicado: 5%\nO valor do aumento: R${salario * 0.05}\nSalario com o reajuste: R${salario_4}')
else:
    print('Informe Apenas numeros')
print('\n')


# Exercicio 12- Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês. 
# Desconto do IR: 
# Salário Bruto até 900 (inclusive) - isento 
# Salário Bruto até 1500 (inclusive) - desconto de 5% 
# Salário Bruto até 2500 (inclusive) - desconto de 10% 
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.

h, vh = int(input('Quantas horas você trabalhou: ')), int(input('Qual o valor da sua hora: '))

slb = h * vh
clc_i1, clc_i2, clc_i3, clc_i4 = slb * 0.00, slb * 0.05, slb * 0.10, slb * 0.20
clc_inss, clc_fgts = slb * 0.10, slb * 0.11
tlt_1, tlt_2, tlt_3, tlt_4 = clc_i1 + clc_inss, clc_i2 + clc_inss, clc_i3 + clc_inss,  clc_i4 + clc_inss 


if slb <= 900:
    print(f'Salário Bruto: R${slb}\nIR: R${clc_i1}\nINSS: R${clc_inss}\nFGTS: R${clc_fgts}\nTotal De Descontos: R${tlt_1}\nSalário Liquido: R${slb - tlt_1}')

elif slb > 900 and slb <= 1500:
    print(f'Salário Bruto: R${slb}\nIR: R${clc_i2}\nINSS: R${clc_inss}\nFGTS: R${clc_fgts}\nTotal De Descontos: R${tlt_2}\nSalário Liquido: R${slb - tlt_2}')

elif slb > 1500 and slb <= 2500:
    print(f'Salário Bruto: R${slb}\nIR: R${clc_i3}\nINSS: R${clc_inss}\nFGTS: R${clc_fgts}\nTotal De Descontos: R${tlt_3}\nSalário Liquido: R${slb - tlt_3}')

elif slb > 2500:
    print(f'Salário Bruto: R${slb}\nIR: R${clc_i4}\nINSS: R${clc_inss}\nFGTS: R${clc_fgts}\nTotal De Descontos: R${tlt_4}\nSalário Liquido: R${slb - tlt_4}')

else:
    print('Valor Inválido')

print('\n')


# Exercicio 13- Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. 
dias_pergunta = input('1- Domingo\n2- Segunda\n3- Terça\n4- Quarta\n5- Quinta\n6- Sexta\n7- Sabado')

if dias_pergunta == '1':
    print('Domingo')
elif dias_pergunta =='2':
    print('Segunda')
elif dias_pergunta == '3':
    print('Terça')
elif dias_pergunta == '4':
    print('Quarta')
elif dias_pergunta == '5':
    print('Quinta')
elif dias_pergunta == '6':
    print('Sexta')
elif dias_pergunta == '7':
    print('Sabado')
else:
    print('Valor Inválido')

print('\n')


# Exercicio 14- Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
# Média de Aprovação   Conceito
# Entre 9.0 e 10.0         A
# Entre 7.5 e  9.0         B
# Entre 6.0 e  7.5         C
# Entre 4.0 e  6.0         D
# Entre 4.0 e  0           E






# Exercicio 15- 


print('\n')
