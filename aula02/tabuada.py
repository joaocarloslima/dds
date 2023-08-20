numero = int(input("Digite o valor para calcular a tabuada:"))

for i in range(0, 11):
    #print(i, "x", numero, "=", i * numero )
    #print("{} x {} = {}".format(i, numero, i*numero))
    #print("{a} x {b} = {c}".format(a=i, b=numero, c=i*numero))
    print(f"{i} x {numero} = {i*numero}")
