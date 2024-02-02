# Fungsi untuk menghitung total belanja berdasarkan harga dan jumlah barang
def hitung_total(harga_barang, jumlah_barang):
    total = harga_barang * jumlah_barang
    return total
# Fungsi untuk menghitung diskon berdasarkan total belanja
def hitung_diskon(total_belanja):
    diskon = 0
    # Diskon 10% jika total belanja lebih dari 100000
    if total_belanja > 100000:
        diskon = 0.1 * total_belanja
    # Diskon 5% jika total belanja lebih dari 50000
    elif total_belanja > 50000:
        diskon = 0.05 * total_belanja
    return diskon
# Fungsi utama program
def main():
    print("Selamat datang di Program Penghitung Total Belanja")
    # Input data barang dari pengguna
    nama_barang = input("Masukkan nama barang: ")
    harga_barang = float(input("Masukkan harga barang per unit: "))
    jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))
    # Menghitung total belanja, diskon, dan total setelah diskon
    total_belanja = hitung_total(harga_barang, jumlah_barang)
    diskon = hitung_diskon(total_belanja)

    total_setelah_diskon = total_belanja - diskon
    # Menampilkan detail belanja
    print("\nDetail Belanja:")
    print(f"Nama Barang: {nama_barang}")
    print(f"Harga Barang per Unit: {harga_barang}")
    print(f"Jumlah Barang: {jumlah_barang}")
    print(f"Total Belanja: {total_belanja}")
    print(f"Diskon: {diskon}")
    print(f"Total Setelah Diskon: {total_setelah_diskon}")

    print("\nTerima kasih telah berbelanja!")
# Memastikan bahwa program utama dijalankan hanya, 
# jika file ini dieksekusi langsung
if __name__ == "__main__":
    main()
