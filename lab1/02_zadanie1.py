# Zadanie 1
# - zdefiniować kolekcję zawierającą nazwy dni tygodnia
# - jeżeli długość nazwy jest parzysta, wypisać ciąg liczb zaczynający się od długości tej nazwy aż do zera włącznie
# - wypisać znak z nazwy który znajduje się na pozycji [długość napisu % 5]

weekdays = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]

for day in weekdays:
    l = len(day)
    if(l % 2 == 0) :
        for i in range(l, -1, -1):
            print(i, end=' ')
    print(day[l%5])
