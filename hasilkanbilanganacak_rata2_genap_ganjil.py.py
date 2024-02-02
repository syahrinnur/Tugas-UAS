import random
# Berfungsi untuk menghasilkan daftar nomor acak dalam rentang tertentu
def generate_random_numbers(n):
    return [random.randint(1, 100) for _ in range(n)]
# Berfungsi untuk menghitung rata-rata dari daftar angka
def find_average(numbers):
    return sum(numbers) / len(numbers)
# Berfungsi untuk mengklasifikasikan angka ke dalam kategori genap dan ganjil
def classify_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return even_numbers, odd_numbers
# Fungsi utama program
def main():
    try:
        # Masukan pengguna untuk jumlah angka acak yang akan dihasilkan
        n = int(input("Masukkan jumlah angka yang ingin digenerate: "))
        if n <= 0:
            print("Jumlah angka harus lebih dari 0.")
            return
        # Menghasilkan angka acak
        random_numbers = generate_random_numbers(n)
        print(f"Angka yang digenerate: {random_numbers}")
        # Menghitung dan menampilkan rata-rata angka yang dihasilkan
        average = find_average(random_numbers)
        print(f"Rata-rata angka: {average:.2f}")
        # Mengklasifikasikan dan menampilkan angka genap dan ganjil
        even_numbers, odd_numbers = classify_numbers(random_numbers)
        print(f"Angka genap: {even_numbers}")
        print(f"Angka ganjil: {odd_numbers}")

    except ValueError:
        print("Masukkan angka yang valid.")
# Memastikan bahwa program utama dijalankan hanya, 
# jika file ini dieksekusi langsung 
if __name__ == "__main__":
    main()
