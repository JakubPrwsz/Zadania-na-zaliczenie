#Napisz program z użyciem for liczący od 1 do wartości podanej z klawiatury.

n = int(input("Podaj liczbę do której chcesz żebym liczył: "))

for i in range(n):
    print(i + 1)
    i += 1