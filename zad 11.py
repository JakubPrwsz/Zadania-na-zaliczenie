# Napisz program, który oblicza pole całkowite i objętość prostopadłościanu. Dane podane z klawiatury.
# W przypadku podania liczby ujemnej lub 0, program powinien wypisywać komunikat informujący o błędnej wartości i nic nie liczyć.

a = int(input("Podaj długość pierwszej krawędzi: "))
b = int(input("Podaj długość drugiej krawędzi: "))
c = int(input("Podaj długość trzeciej krawędzi: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Błędne dane, możesz podać tylko liczby dodatnie")
else:
     print(f"Pole całkowite wynosi: {2*(a * b + a * c + b * c)} cm^2 a objętość jest równa: {a * b * c} cm^3")