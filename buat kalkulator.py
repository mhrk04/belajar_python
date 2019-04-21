print("kalkulator")
print("Hanya menyokong operasi tambah, tolak, darab & bahagi")
print("darab = * , bahagi = /")

nom1 = float(input("Sila masukkan nombor :"))
op = input("Jenis operasi :")
nom2 = float(input("Sila masukkan nombor kedua :"))

if op == "+":
    print(nom1+nom2)
elif op == "-":
    print(nom1-nom2)
elif op == "/":
    print(nom1/nom2)
elif op == "*":
    print(nom1*nom2)
elif op == "%":
    print(nom1%nom2)
else:
    print("jenis operasi anda salah")