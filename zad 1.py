#Zadanie 1 Napisz program umożliwiający obliczenie ile paliwa spala samochód na 100 km. Dane wczytane z klawiatury. 
#Podajemy ilość zużytego paliwa w litrach i pokonaną odległośćto zużyte paliwo 22 litry i przejechana trasa 600 km.


d = int(input("Podaj dystans jaki pokonał samochód: "))
f = int(input("Podaj ile zużyto paliwa: "))

f = round((f * 100) / d, 3)

print(f"Samochód miał spalanie {f} litrów benzyny na 100 km ")