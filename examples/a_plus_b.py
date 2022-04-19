from hackrform import read, display

print("aqui tem print!")

a = read("Qual o valor de a?", dtype=int)
b = read("Qual o valor de b?", dtype=int)
soma = a + b

display("a + b = " + str(soma))
