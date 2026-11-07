nome = input("Qual o nome do aluno?: ")

nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))
nota_3 = float(input("Nota 3: "))

lista = []
lista.append(nota_1)
lista.append(nota_2)
lista.append(nota_3)

media = sum(lista)/len(lista)

print("o(a)", nome, "possui a média", media)
if media >= 7:
   print("O aluno", nome, "passou")
else:
    print("O aluno", nome, "não passou!")
