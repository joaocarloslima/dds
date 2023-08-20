nome = input("Digite o seu nome:")
salario = int( input("Digite o seu salario:") )

tera_aumento = salario <= 2424
novo_salario = salario * 1.06

if tera_aumento:
    print(nome, "tera aumento. O novo salario é", novo_salario)
else:
    print(nome, "não terá aumento.")