#Napisz program z wykorzystaniem dowolnej pętli sumujący 3 liczby wczytane z klawiatury

b = int(0)

for _ in range(3):
    a = int(input("Podaj liczbę do zsumowania: "))
    b = b + a

print(b)