#Napisz program wczytujący wartość a z klawiatury. Program sprawdza czy liczba jest parzysta. Wyświetl stosowne komunikaty.

a = float(input("Podaj a żeby sprawdzić czy liczba jest parzysta: "))

if a % 2:
    print("liczba jest nieparzysta")
else:
    print("Liczba jest parzysta")