#Operadores de divisão (/) e resti da divisão (%)
#divisão = 15 / 2
#resto = 15 % 2

#print('Divisão:', divisão)
#print('Resto:', resto)

#Ler um número para ver se ele é par ou impar
numero = int(input("informe um numero"))
#calcula o resto da divisão do numero por 2
resto = numero % 2
#olha para o valor do resto
if resto == 0:
    print(numero, 'É par!')
else :
    print(numero, "É impar")
