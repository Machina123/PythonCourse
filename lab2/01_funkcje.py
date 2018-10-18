# -------- FUNKCJE W PYTHON --------------
# Definicja funkcji:
# def nazwa_funkcji(parametr1, parametr2=default2, ...):
#   ...
#   return (wartosc / None[jak null z C])
#
# prawidłowe wywołania:
# nazwa_funkcji("napis1")
# nazwa_funkcji("napis1", 12.5)
# nazwa_funkcji("napis1", parametr3=10)
# ----------------------------------------
# Ćwiczenie: 
# napisać funckję moj_range(start, end, step) która będzie działała jak range

def moj_range(start, end, step=1):
    rangetab = []
    actstep = 0
    steps = int((end - start) / step)
    if steps < 0:
        return []
    i = start
    while actstep < steps:
        rangetab.append(i)
        i += step
        actstep += 1
    return rangetab

print(moj_range(10,20,1))