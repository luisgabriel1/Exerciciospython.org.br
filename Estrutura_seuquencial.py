import math
# Exercicio 1- Faça um programa que mostre "Olá Mundo"
print()
print('Olá mundo')
print()
# Exercicio 2- Faça um programa que peça o numero e então mostre a mensagem o numero informado foi [NUMERO]
numero = int(input('Escolha um numero:  '))
print(f'O numero informado foi: {numero}')
print()
# Exercicio 3- Faça um programa que peça dois numeros e imprima a soma
valor = int(input('Envie um numero para somar:  '))
valor_1 = int(input('Escolha o segundo numero para somar ao primeiro:  '))
soma = valor + valor_1
print(soma)
print()
# Exercicio 4- Faça um programa que peça as 4 notas bimestrais e mostre a media 
nota_1 = int(input('Qual foi sua primeira nota do bimestre ?  '))
nota_2 = int(input('Qual a sua segunda nota do bimestre ?  '))
nota_3 = int(input('Qua a sua terceira nota do bimestre ?  '))
nota_4 = int(input('Qual a sua quarta nota do bimestre ?  '))
media = nota_1 + nota_2 + nota_3 + nota_4
print(f'Sua nota media escolar foi de {media / 4}')
print()
# Exercicio 5- Faça um programa que converta metros para centimetros
metros = int(3)
centimetros = int(metros * 100)
print(f'O valor em centimetros foi {centimetros}')
print()
# Exercicio 6- Faça um programa que peça o raio de um circulo, calcule e mostre a area
raio = int(input('Qual o raio do seu circulo ?   '))
area =  int(math.pi * raio**2)
print(f'Há area do seu circulo é de {area}cm')
print()
# Exercicio 7- Faça um programa que calcule a area de um quadrado, em seguida mostra o dobro da area
comprimento = int(10)
largura = int(14)
area_quadrado = comprimento * largura
total = area_quadrado * 2
print(f'A area do seu quadrado é {total}')
print()
# Exercicio 8- Faça um programa que pergunte quanto você ganha por hora e o numero de horas trabalhadas no mês, calcule e mostre o total do seu salario no mês
valor_hora = int(input('Quanto custa sua hora ?  '))
horas_trabalhadas_mes = int(input('Quantas horas você trabalhou no mês ?  '))
total_salario = int(valor_hora * horas_trabalhadas_mes)
print(f'O seu salario mensal foi de R${total_salario}')
print()
# Exercicio 9- Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre em graus Celsius
graus_fahrenheit = int(input('Quantos graus em fahrenheit você deseja converter para Celsius ?  '))
formula_celsius = int(5 * ((graus_fahrenheit - 32) / 9))
print(f'A temperatura em Graus Celsiu é de {formula_celsius}')
print()
# Exercicio 10- Faça um programa que peça a temperatura em Graus Celsius, tranforme e mostre em graus Fahrenheit
graus_celsius = int(input('Quantos graus em Celsius você deseja converter para Fahrenheit ?  '))
formula_fahrenheit = int(9 * graus_celsius / 5 + 32)
print(f'A temperatura em Graus Fahrenheit é de {formula_fahrenheit}')
print()
# Exercicio 11 - faça um programa que peça 2 numeros inteiros e um numero real. Calcule e mostre: 
# a. O produto do dobro do primeiro com a metade do segundo.
# b. A soma do triplo do primeiro com o terceiro.
# c. O terceiro elevado ao cubo 
primeiro_valor = int(input('Qual o primeiro valor ?  '))
segundo_valor = int(input('Qual o segundo valor ?  '))
terceiro_valor = float(input('Qual o terceiro valor tem que conter . exemplo 5.3 ?  '))
a = int((primeiro_valor*2) + (segundo_valor / 2))
b = int(primeiro_valor * 3 + terceiro_valor)
c = int(terceiro_valor**3)
print(f'A = {a} \n B = {b} \n C = {c}')
print()
# Exercicio 12- Tendo como dados de entrada a altura de uma pessoa, construa um algoritimo que calcule seu peso ideal, usando a seguinte formula (72.2*altura) - 58 
altura = float(input('Qual sua altura ?')  )
calculo = int((72.7*altura) - 58)
print(f'O peso ideal para sua altura é de {calculo}')
print()
# Exercicio 13 - Tendo como dados de entrada (h) de uma pessoa construa um algoritimo que calcule seu peso ideal usando as seguintes formula:
# a. Para homens: (72.7 * h) - 58
# b. Para mulheres: (62.1 * h) - 44.7
homens = 'h'
mulheres = 'm'
genero = input('Você é homen ou mulher, se for homen envie: h  se for mulher envie: m >  ')
if genero == homens:
    altura_h = float(input('Qual sua altura ?  ')  )
    aa = int((72.7 * altura_h) - 58)
    print(f'O peso ideal para o Sr é de {aa}')
else:
     genero == mulheres
     altura_m = float(input('Qual a sua altura ? ')  )
     bb = float(62.1 * altura_m) - 44.7
     print(f'O peso ideal para a Sra é de {bb}')
print()
# Exercicio 14- João pescador tem que pagar R$4 de multa por kilo excedente, João precisa de um programa que leia a variavel peso(peso de peixes) e calcule o excesso.
# Gravar na variavel excesso a quantidade de quilos além do limite
# E na variavel multa o valor da multa que joão devera pagar
# Imprima os dados do programa com as mensagens adequadas
peso_pescados = int(50)
peso_maximo = int(50)
excesso = int(peso_pescados - peso_maximo)
multa = int(4 * excesso)
if peso_pescados > peso_maximo:
    print(f'João você tem que pagar R${multa} você excedeu {excesso} quilos do permitido')
else: 
    peso_pescados <= peso_maximo
    print(f'João você não pagara nenhuma multa dessa vez Parabens!!')
print()
# Exercicio 15- Faça um programa que pergunte quanto você ganha por hora e o numero de horas trabalhadas no mês.
# Calcule e mostre o total do seu salario no referido mês, sabendo-se que são descontados:
# Imposto_de_renda = 11%
# INSS = 8%
# Sindicato = 5%
# a. salario bruto / b. quanto pagou no INSS / c. quanto pagou no sindicato / d. o salario liquido / e. o total que foi descontado e salario liquido
preco_hora = int(input('Quanto você ganha por hora ?  '))
horas_mes = int(input('Quantas horas você trabalhou no mês ?  '))
salario_bruto = int(preco_hora * horas_mes)
Ir = int(salario_bruto * 0.11)
Inss = int(salario_bruto * 0.08)
sindicato = int(salario_bruto * 0.05)
impostos = int(Ir + Inss + sindicato)
salario_liquido = int(salario_bruto - impostos)
print(f'+  Salário Bruto : R${salario_bruto}')
print(f'- Ir (11%) : R${Ir}')
print(f'- INSS (8%) : R${Inss}')
print(f'- sindicato (5%) : R${sindicato}')
print(f'= salário liquido : R${salario_liquido}')
print(f'- Total descontados : R${impostos} \n= Total salario : R${salario_liquido}')
print()
# Exercicio 16- Faça um programa para uma loja de tintas, o programa deve pediro tamanho em m² da area a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 m² e que a tinta é vendida em latas de 18L, que custam R$80
# Informe ao usuario a quantidade de latas de tinta a serem compradas e o preço total.
medida = float(input('Quantos m² tem area que deseja pintar ?\n'))
litros = 18
valor_lata = 80
qtd_litro = medida / 3
qtd_lata = math.ceil(qtd_litro / litros)
preco = math.ceil(qtd_lata * valor_lata)
print(f'Qtd lata : {qtd_lata: 5.2f}\nValor : R${preco: 5.2f}')
print()
print()
# Exercicio 17- Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da area a ser pintada.
# Considere que a cobertura da tinta é de 1L para cada 6 m² e que a tinta é vendida em latas de 18L, que custam R$80, ou em galões de 3,6L que custam R$25
# Informe ao usuario as quantidades de tinta a serem compradas e os respectivos preços em 3 situações
# - Comprar apenas latas de 18L
# - Comprar apenas galões de 3,6L
# - Misturar latas e galões, de forma que o desperdicio de tinta seja menor. Acrescente 10% de folga e sempre arredonde para cima, isto é, sempre latas cheias
import math
medida = float(input('Quantos m² tem a area que deseja pintar ?\n'))
ltr = math.ceil(medida / 6 )
lt = ltr 
x = 0 # Contador
qtd = 0 # Acumulador
l_l = 18
l_g = 3.6
v_g = 25
v_l = 80
qtd_lata = math.ceil(ltr/ l_l)
preco_l = math.ceil(qtd_lata * v_l)
qtd_galao = math.ceil(ltr / l_g)
preco_g = math.ceil( qtd_galao * v_g )

while l_l <= ltr:
    ltr = ltr - l_l
    x += 1
    qtd = ltr
print()
z = math.ceil(qtd / l_g)
p_g = math.ceil(z * v_g)
medida_1 = math.ceil(lt - qtd)
y1 = math.ceil(int(medida_1 / 18))
p_l = math.ceil(y1 * v_l) 
print(f'Latas & Galões:\nLatas: {y1}\nGalões: {z}\nValor: R${p_g + p_l}')
print()
print()
print(f'LATA:\nQtd: {qtd_lata}\nValor: R${preco_l}\n\nGALÃO:\nQtd: {qtd_galao}\nValor: R${preco_g}')

# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)
# Tamanho do arquivo em megabytes / (velocidade de download em megabits / 8) = tempo em segundos.
tm_arq = int(input('Qual o tamanho do arquivo, passe me MB:\n'))
vlc = int(input('Informe quantos mbps sua internet alcança:\n'))
cl_tmp_seg = tm_arq / (vlc / 8)
cl_seg_para_min = float(cl_tmp_seg / 60)
print(f'INFORMAÇÕES:\nTamanho Arq: {tm_arq}\nDowload em Mbps: {vlc}\nTempo: {cl_seg_para_min:5.2f}m')

# FIM