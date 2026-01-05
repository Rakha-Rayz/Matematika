luas = int(input("Masukkan luas persegi: "))
ketemu = False

for sisi in range(1, luas + 1):
    if sisi * sisi == luas:
        print("Panjang sisi =", sisi)
        ketemu = True
        break

if not ketemu:
    print(f"Ya Allah mana ada sisi yang sama dengan hasil seperti ${luas}")