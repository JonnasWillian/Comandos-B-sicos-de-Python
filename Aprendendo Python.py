print ("Ola, mundo")
#Print imprime uma mensagem na tela a mensagem so aparece dps dos () e das ""
#numero = input ("Digite o numero :")
#Input é a variavel de entrada de dados
print ("Fim teste")
print ("Começo, meio e fim")
""""
Tabela
De
Linhas
De
Recados
POR
Multiplas linhas
"""
# -*- coding: utf-8 -*-
print ("Olá mundo")
# Coding utf8 utilizado para apropriacao de acentos 
minha_variavel = "Eu sei"
print (minha_variavel)
# a opecao minha_variavel salva dados q podem ser utilizados um tempo dps
#As variaveis podem ser inteiras, fluturantes, istrings ou Booleana
var1 = 1 #Inteira
var2 = 1.1 #Flutuante
var3 = "Eu sou uma istring" #String, uma estring precisa das "" para saber qual mensagem deve ser salva
print (var1)
print (var2)
print (var3)
#Quando for imprimir uma variável não é necassrio a utilização das "", caso use as "" você ira imprimir as palavras colocadas, não o valor
"""""
Operadores relacionais 
== Igual
!= Diferente 
< Menor
> Maior
>= Maior ou igual
<= Divisão
"""
x = 2
y = 3
soma = x + y
print (x > y)
print (x < y)
#Perceba q a operação é respondida com questões de verdadeiro e falso
print (x + y)
#Veja q a operação ja é respodinda pelo próprio print
"""""
Operadores lógioos
AND duas condições sejam verdadeiras
OR pelo menos uma condição seja verdadeira
NOT inverte o valor
"""
print (x < y and y > x )
""""
iF = condição se algo for acontecer tipo:  if condição: 
Else = Condição se o "if" não ocorrer
Elife = Caso seja necessario mais condições entre o if e o else
"""
if x > y:
	print ("X é maior q Y")
elif x == y:
	print ("X é igual a Y")
else:
	print ("Y é maior q x")
#Para sair do processo de codificação de uma condição basta adicionar mais uma linha de programção e apagar o espaçamento
""""
Estrutura de repetição
while: usado quando não sabemos exatamente quantas vezes o bloco será repetido
for: usado quando sabemos quantas vezes o bloco será repetido
"""
a = 1
while x < 5:
	print (x)
	x += 1 # Isso é o mesmo que x = x+1
	#O Coloquei um contador pra aumentar o valor de x, para que ele chegue a 5 e saia do programa
lista = [0 ,1, 2, 3, 4, 5]
lista2 = ["ola", "mundo","!"]
for i in lista:
	print (i)
""""
A lista pode caber vários valores, sejam inteiros, flutuantes, string, etc
O "i" do "for" percorre toda a lista, verificando dado por dado por cada item na lista e o print imprimi o item
"""
for i in range (10):
	print (i)
"""
Cria uma lista com o tamanho definido no primeiro valor dado
A contagem em programação sempre começa do 0
"""
for i in range (10, 20, 2):
	print (i)
"""
Quando você adiciona um segundo valor que primerio é o Número que o contador começa
O segundo número é até aonde o contador dever ir 
E o terceiro valor é de quanto em quantos números o contador irá avançar
"""
j = 2
r = 0
try: 
	print (a/b)
except:
	print("Nao e permitida")
"""
O comando TRY pede ao sistema q ele faça uma tentativa de execução
E o comando EXCEPT executa uma função caso o comando TRY falhe
"""
import random
numero = random.randint (0, 10)
print (numero)
"""
import e random são funções de escolha de numeros aleatorios
O primeiro numero em parenteses fala apartir de qual numero começa a contagem e o outro numero fala aonde termina
"""    