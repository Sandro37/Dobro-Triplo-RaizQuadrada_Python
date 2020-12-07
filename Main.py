import math

entrada = float(input("Entre com um valor: "))

valores = []

valores.append(entrada * 2)
valores.append(entrada * 3)
valores.append(math.sqrt(entrada))

print("o dobro de {0} é {1}".format(entrada, valores[0]))
print("O tripo de {0} é {1}".format(entrada, valores[1]))
print("A raiz quadrada de {} é {:.2f}.".format(entrada, valores[2]))