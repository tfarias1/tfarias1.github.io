# Calaculadora de Gorjetas.
print("Bem vindo a Calculadora de Gorjetas \n")
valor_da_conta = float(input("Informe o total da conta: "))
percentual_gorjeta = int(input("Quantos '%' de gorjeta você quer doar? 10, 12 ou 15?: "))
num_pessoas = int(input("Por quantas pessoas a conta será dividida: "))

valor_gorjeta = (valor_da_conta * (percentual_gorjeta /100))
total =  valor_da_conta + valor_gorjeta
valor_por_pessoa = round(total / num_pessoas, 2)


print(f"Cada pessoa deve pagar: {str(valor_por_pessoa)} \n")
