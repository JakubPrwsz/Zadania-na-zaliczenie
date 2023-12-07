#Napisz program z użyciem for liczący od 10 do 1 co 2

i = int(10)

for _ in range(10):
    print(i)
    i -= 2
    if i <= 1:
        break