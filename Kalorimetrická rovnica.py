import math

### Hladáme "t"
hladame_t = False
hladame_m2 = True



if hladame_t:
    m1 = float(input("Zadaj hmotnosť prvého telesa: "))                     ### Hmotnosť v kg
    c1 = float(input("Zadaj mernú tepelnú kapacitu prvého telesa: "))
    t1 = float(input("Zadaj počiatočnú teplotu prvého telesa: "))
    m2 = float(input("Zadaj hmotnosť druhého telesa: "))                    ### Hmotnosť v kg
    c2 = float(input("Zadaj mernú tepelnú kapacitu druhého telesa: "))
    t2 = float(input("Zadaj začiatočnú teplotu druhého telesa: "))

#Q = m * c * (t2 - t1)

    cmt1 = (c1 * m1 * t1)
    cmt2 = (c2 * m2 * t2)
    cm2 = (c2 * m2)
    cm1 = (c1 * m1)
    cm3 = (c2 * m2) + (c1 * m1)
    cmt3 = (c1 * m1 * t1) + (c2 * m2 * t2)
    t = float(f'{cmt3 / cm3}')
    tt1 = f'{t - t1}'
    print("c1 * m1 * Δt = c2 * m2 * Δt")
    print("============================")
    print("c1 * m1 * (t1 - t)  = c2 * m2 * (t - t2)")
    print("____________________________")
    print("t = c1 * m1 * t1 + c2 * m2 * t2 / \n  m1 * c1 + m2 * c2")
    print("============================")
    print(f't = {t:.2f}°C')
    if tt1 >= "0":
        print(f'Teleso sa ohreje o {tt1:.4}°C')
    else:
        print(f'Teleso sa ochladí o {tt1:.4}°C')

if hladame_m2:
    m1 = float(input("Zadaj hmotnosť studenšieho telesa: "))                     ### Hmotnosť v kg
    t1 = float(input("Zadaj teplotu studenšieho telesa: "))
    Vysledna_t = float(input("Zadaj výslednu teplotu po ustálení: "))
    t2 = float(input("Zadaj začiatočnú teplotu druhého telesa: "))
    Vt1 = Vysledna_t - t1
    Vt2 = t2 - Vysledna_t
    m2 = (m1 * Vt1) / Vt2
    print('m2 = m1 * (t - t1) / t2 - t ')
    print(f'm2 = {m1} * ({Vysledna_t} - {t1}) / ({t2} - {Vysledna_t})')
    print("============================")
    print(f"m2 = {m2:.4} kg => {m2:.4} l.")


