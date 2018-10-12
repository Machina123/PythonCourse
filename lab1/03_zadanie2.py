# Zadanie 2
# - analogiczne do zadania 1
# - pobrać dni tygodnia z pliku tekstowego
# - jeżeli długość nazwy jest parzysta, wypisać ciąg liczb zaczynający się od długości tej nazwy aż do zera włącznie
# - wypisać znak z nazwy który znajduje się na pozycji [długość napisu % 5]

f = open("03_zadanie2_dane.txt", "r")

for linia in f:
    l = len(linia)
    if(l % 2 == 0) :
        for i in range(l, -1, -1):
            print(i, end=' ')
    print(linia[l%5])

f.close()