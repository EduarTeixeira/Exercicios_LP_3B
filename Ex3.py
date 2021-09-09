n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
lista = [n1, n2, n3, n4]
media = sum(lista) / len(lista)
print("A sua média é {}".format(media))