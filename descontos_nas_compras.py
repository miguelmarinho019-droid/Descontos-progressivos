# Entrada de dados (Valor total da compra)
valor_das_compra = float(input("Digite o valor da compra: R$ "))

# Processamento (Aplicação das estruturas condicionais e operações para obter o valor de desconto)
if valor_das_compra < 200:
    print("Você recebeu um desconto de 5% ! ")
    desconto = (5/100) * valor_das_compra
elif valor_das_compra >= 200:
    print("Você recebeu um desconto de 10% !")
    desconto = (10/100) * valor_das_compra
elif valor_das_compra >= 300:
    print("Você recebeu um desconto de 15% !")
    desconto = (15/100) * valor_das_compra
total = valor_das_compra - desconto

# Sáida (Informar ao cliente o total com o desconto aplicado e valor formatado)
print(f"O seu total com o desconto aplicado é de R$ {total:.2f}")
print("================================")