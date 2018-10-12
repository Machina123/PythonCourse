napis = "Hello World!"  # zmienne w Pythonie nie mają określonego typu
print(napis)
print(napis[5])     # odwołanie do konkretnego znaku / elementu kolekcji
print(napis[-2])    # można stosować liczby ujemne, wtedy liczenie zacznie się od końca

# Listy (nie mylić z tablicami! działają podobnie, ale to nie to samo)
lista = ["abc", 123, 45.67]     # typ danych wewnętrznych jest dowolny, można mieszać typy
print(lista)    # wypisywanie całej listy

# Pętla for - przechodzi po czym się tylko da
for element in lista:   # czytaj: dla każdego elementu (dalej nazywanego "element") w kolekcji lista, zrób ...
    print(element)      # uwaga na wcięcia! (dobry edytor zamienia taba na 4 spacje, Python gubi się przy tabach xD)

# Zapis pętli for znanej z języka C/C++, na przykład:
# for(int i=0; i < 10; i++) {
#   cout << i;
# }
for i in range(10):
    print(i)

# range to tak naprawdę kolekcja zawierająca jakiś zakres liczb
# range(start, stop, krok) - będzie zawierać liczby od "start" do "stop" (ale bez "stop"), za każdym razem zwiększane o "krok"
#   - "krok" może być liczbą ujemną
#   - domyślnie "start" wynosi 0, nie musimy go podawać
#   - domyślnie "krok" wynosi 1, nie musimy go podawać
