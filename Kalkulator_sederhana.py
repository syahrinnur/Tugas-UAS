# Berfungsi untuk melakukan penjumlahan
def penjumlahan(a, b):
    return a + b
# Berfungsi untuk melakukan pengurangan
def pengurangan(a, b):
    return a - b
# Berfungsi untuk melakukan perkalian
def perkalian(a, b):
    return a * b
# Berfungsi untuk melakukan pembagian, 
# menangani pembagian dengan nol
def pembagian(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian oleh nol tidak diperbolehkan"
# Fungsi utama program
def main():
    print("Kalkulator Sederhana")
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    # Masukan pengguna untuk pilihan operasi
    pilihan = input("Masukkan nomor operasi (1/2/3/4): ")
    # Masukan pengguna untuk dua nomor
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    # Melakukan operasi yang dipilih dan menampilkan hasilnya
    if pilihan == '1':
        hasil = penjumlahan(angka1, angka2)
        print(f"Hasil penjumlahan: {hasil}")
    elif pilihan == '2':
        hasil = pengurangan(angka1, angka2)
        print(f"Hasil pengurangan: {hasil}")
    elif pilihan == '3':
        hasil = perkalian(angka1, angka2)
        print(f"Hasil perkalian: {hasil}")
    elif pilihan == '4':
        hasil = pembagian(angka1, angka2)
        print(f"Hasil pembagian: {hasil}")
    else:
        print("Pilihan operasi tidak valid")
# Memastikan bahwa program utama dijalankan hanya, 
# jika file ini dieksekusi langsung 
if __name__ == "__main__":
    main()