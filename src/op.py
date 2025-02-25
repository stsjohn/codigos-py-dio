#Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre elesnumero1 = 2
num1 = 5
num2 = 20

resultado = num1 + num2
print("o resultado da soma é " + resultado)


operacao = input("Escolha a operação (+, -, *, /): ")
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operação inválida"

print(f"Resultado: {resultado}")
