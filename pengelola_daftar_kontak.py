# Definisikan kelas Kontak untuk mewakili kontak individual
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
# Definisikan kelas ContactManager untuk mengelola daftar kontak
class ContactManager:
    def __init__(self):
        self.contacts = []
    # Cara menambahkan kontak baru ke daftar
    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Kontak {contact.name} ditambahkan.")
    # Metode untuk menampilkan daftar kontak
    def display_contacts(self):
        print("Daftar Kontak:")
        for contact in self.contacts:
            print(f"{contact.name}: {contact.phone}")
# Fungsi utama program
def main():
    # Membuat instansi ContactManager untuk mengelola kontak
    contact_manager = ContactManager()
    # Menu loop untuk interaksi pengguna
    while True:
        print("\nPilih tindakan:")
        print("1. Tambah Kontak")
        print("2. Tampilkan Kontak")
        print("3. Keluar")
        # User input untuk menu pilihan
        choice = input("Masukkan pilihan (1/2/3): ")
        # Melakukan tindakan berdasarkan pilihan pengguna
        if choice == '1':
            # Pengantar pengguna untuk rincian kontak dan membuat objek Kontak baru
            name = input("Masukkan nama kontak: ")
            phone = input("Masukkan nomor telepon kontak: ")
            new_contact = Contact(name, phone)
            # Tambahkan kontak baru ke ContactManager
            contact_manager.add_contact(new_contact)
        elif choice == '2':
            # Menampilkan daftar kontak
            contact_manager.display_contacts()
        elif choice == '3':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
# Memastikan bahwa program utama dijalankan hanya, 
# jika file ini dieksekusi langsung 
if __name__ == "__main__":
    main()
