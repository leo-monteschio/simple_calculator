valor_1 = float(input("Digite o primeiro valor: "))
operador = input("Digite o operador (+, -, *, /): ")
valor_2 = float(input("Digite o segundo valor: "))

if operador == "+":
  print (f" Resultado: {valor_1 + valor_2}")

elif operador == "-":
  print (f" Resultado: {valor_1 - valor_2}")

elif operador == "*":
  print (f" Resultado: {valor_1 * valor_2}")

elif operador == "/":
  if valor_2 == 0:
    print ("Não é possível dividir por zero")
  else:
    print (f" Resultado: {valor_1 / valor_2}")
  
else:
  print("Operador inválido")
