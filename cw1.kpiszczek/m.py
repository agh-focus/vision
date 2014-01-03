#Programik rozpoznajacy jaka jest wartosc monet na kartce papieru.

from SimpleCV import Image, Blob
import numpy as np


img = Image("monety.png")
monety = img.invert().findBlobs(minsize = 500)
wartosc = 0.0

monety_przekatne_wartosci = np.array
([
[ 15.5, 0.01],
[ 16.5, 0.1],
[ 23.0, 1]
]);

#Skalowanie jest tu najwiekszym problemem (ponizej skaluje na podstawie 1gr). 
skala = monety_przekatne_wartosci[0,0]/min([m.radius()*2 for m in monety])

for m in monety:
    przekatna_w_mm = m.radius() * 2 * skala
    tab_roznic = np.abs(przekatna_w_mm - monety_przekatne_wartosci[:,0])
    indeks = np.where(tab_roznic == np.min(tab_roznic))[0][0]
    wartosc += monety_przekatne_wartosci[indeks, 1]


print "Calkowita wartosc monet to: ", wartosc, " zl"

#Przy skalowaniu na podstawie najwiekszej wartosci z tablicy czyli 1 zl program zwraca zly wynik 1.13zl.
# Myli jedna 10gr z 1gr. Mozna by stworzyc tablice skal dla kazdej z 5 monet i potem policzyc srednia z
# tych skal