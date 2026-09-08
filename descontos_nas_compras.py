# Entrada de dados (Valor total da compra)
valor_da_compra = float(input("Digite o valor da compra: R$ "))

# Processamento (Aplicação das estruturas condicionais e operações para obter o valor de desconto)
if valor_da_compra < 200:
    print("Você recebeu um desconto de 5% ! ")
    desconto = (5/100) * valor_da_compra
elif valor_da_compra < 300:
    print("Você recebeu um desconto de 10% !")
    desconto = (10/100) * valor_da_compra
else:
    print("Você recebeu um desconto de 15% !")
    desconto = (15/100) * valor_da_compra
total = valor_da_compra - desconto

# Saída (Informar ao cliente o total com o desconto aplicado e valor formatado)
print(f"O seu total com o desconto aplicado é de R$ {total:.2f}")
print("================================")