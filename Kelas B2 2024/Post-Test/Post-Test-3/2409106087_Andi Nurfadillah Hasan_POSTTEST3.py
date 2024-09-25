berat_mg = float(input("Masukkan berat badan dalam miligram (mg): "))
tinggi_km = float(input("Masukkan tinggi badan dalam kilometer (km): "))

berat_kg = berat_mg / 1000000

tinggi_m = tinggi_km * 1000

BMI = berat_kg / (tinggi_m **2)

if BMI < 18.5:
    Kategori = "Underweight"
elif BMI < 24.9:
    Kategori = "Normal"
elif BMI < 29.9:
    Kategori = "Overweight"
else:
    Kategori = "Obesity"

print(f"BMI Anda adalah {BMI:.2f}")
print(f"Kategori Anda adalah {Kategori}")