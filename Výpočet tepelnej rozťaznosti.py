### Program pri neznámej a

print("PROGRAM PRI NEZNAMEJ a")

t1 = float(input("Vstupná teplota: "))
t2 = float(input("Výstupná teplota:  "))
ΔL = float(input("Zmena dlžky o: "))
delta_t = t2-t1
lO = -ΔL
a = f"{ΔL/delta_t * lO:.4f}"
print("a = ", a)
print(" ")


### Program pri neznamej ΔL
print("PROGRAM PRI NEZNAMEJ ΔL ")

lo = float(input("Zadaj rozmer: "))
T1 = float(input("Vstupná teplota: "))
T2 = float(input("Výstupna teplota:  "))
a = float(input("koeficient a : "))
delta_T = T2-T1
delta_l = f"{lo}*{a}*{delta_T} ={lo*a*delta_T:.4f} "
print("ΔT = ", delta_T)
print("ΔL = ", delta_l)
print("  ")
print("  ")
print("  ")
