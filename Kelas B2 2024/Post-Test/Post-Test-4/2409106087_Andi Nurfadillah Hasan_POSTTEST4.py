def login_system():
    username = "Dilla"
    password = "87" 
    
    login_attempts = 0 
    max_attempts = 3  

    while login_attempts < max_attempts:
        input_username = input("Masukkan Username: ")  
        input_password = input("Masukkan Password: ") 

        if input_username == username and input_password == password:
            print("Login berhasil\n")
            return True  
        else:
            login_attempts += 1
            print(f"Login gagal")
    
    print("Terlalu banyak percobaan login. Program berhenti.")
    return False

def bmi_calculator():
    while True:
        print("\nKalkulator BMI (Body Mass Index)")
        
        berat_mg = float(input("Masukkan berat badan (mg): "))
        
        tinggi_km = float(input("Masukkan tinggi badan (km): "))

        berat_kg = berat_mg / 1_000_000
        tinggi_m = tinggi_km * 1_000

        bmi = berat_kg / (tinggi_m ** 2)

        if bmi < 18.5:
            status = "Kurus"
        elif 18.5 <= bmi < 24.9:
            status = "Normal"
        elif 25 <= bmi < 29.9:
            status = "Berlebih"
        else:
            status = "Obesitas"

        print(f"Berat: {berat_kg:.2f} kg, Tinggi: {tinggi_m:.2f} m, BMI: {bmi:.2f}, Status: {status}")

        keluar = input("Apakah anda ingin keluar? (ya/tidak): ")
        if keluar.lower() == 'ya':
            print("Program berhenti. Terima Kasih.")
            break  

if login_system():  
    bmi_calculator()  
    