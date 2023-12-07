#Napisz program liczący od 1 do 10 i zatrzymujący się po wyświetleniu cyfry 6

for i in range(10):
    print(i + 1)
    i += 1
    if i == 6:
        break