from enum import IntEnum

capicity = int(input("Podaj pojemność silnika: "))

Menu_Fuel = IntEnum('Menu_Fuel', {'Spalinowy': 1, 'Hybrydowy': 2, 'Plugin': 3, 'Elektryczny': 4})

fuel = int(input("""Podaj rodzaj napędu:
1 - Spalinowy
2 - Hybrydowy
3 - Hybrydowy plug-in
4 - Elektryczny
"""))

if fuel == 1 or fuel == 2 or fuel == 3 or fuel == 4:

    buyPrice = float(input("Podaj cenę zakupu: "))
    excise = float(0)
    smallExcise = 0.031
    bigExcise = 0.186
    smallExciseHyb = smallExcise / 2
    bigExciseHyb = bigExcise / 2

    
    #funkcja obliczająca małą akcyzę
    def small_excise_count(price, exc):
        return price * exc

    #funkcja obliczająca małą akcyzę dla pojazdów hybrydowych
    def small_excise_hyb_count(price, exc):
        return price * exc

    #funkcja obliczająca dużą akcyzę
    def big_excise_count(price, exc):
        return price * exc

    #funkcja obliczająca dużą akcyzę dla pojazdów hybrydowych i plug-in
    def small_excise_hyb_count(price, exc):
        return price * exc


    if capicity in range(2001):
        if fuel == Menu_Fuel.Spalinowy:
            excise = small_excise_count(buyPrice, smallExcise)
        elif fuel == Menu_Fuel.Hybrydowy:
            small_excise_hyb_count(buyPrice, smallExciseHyb)
        elif fuel == Menu_Fuel.Plugin:
            excise = 0
        elif fuel == Menu_Fuel.Elektryczny:
            excise = 0
        
            


    elif capicity > 2000:
        if fuel == Menu_Fuel.Spalinowy:
            excise = big_excise_count(price, exc)
        elif fuel == Menu_Fuel.Hybrydowy:
            excise = small_excise_hyb_count(price, exc)
        elif fuel == Menu_Fuel.Plugin:
            excise = small_excise_hyb_count(price, exc)
        elif fuel == Menu_Fuel.Elektryczny:
            excise = 0
        
            

    print(excise)

#Jeśli wybór napędu jest z poza przedziały 1-4
else:
    print("Wybierz rodzaj napędu z zakresu: 1-4")
