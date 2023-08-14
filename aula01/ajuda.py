saldo = 10
credito = 20

total = saldo + credito

tenho_dinheiro = total >= 50
tenho_companhia = True

print("Você tem R$", total, "disponivel")
print("Devo ir?", tenho_dinheiro and tenho_companhia)