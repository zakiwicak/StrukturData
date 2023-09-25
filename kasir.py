class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)


class Cashier:
    def __init__(self):
        self.queue = Queue()
        self.current_customer = None

    def add_customer(self, customer):
        self.queue.enqueue(customer)
        print("Pelanggan ditambahkan:", customer)

    def serve_customer(self):
        if self.current_customer is None:
            if not self.queue.is_empty():
                self.current_customer = self.queue.dequeue()
                print("Melayani pelanggan:", self.current_customer)
            else:
                print("Tidak ada pelanggan dalam antrian.")
        else:
            print("Selesaikan pelayanan pelanggan saat ini terlebih dahulu.")

    def finish_serving(self):
        if self.current_customer is not None:
            print("Selesai melayani pelanggan:", self.current_customer)
            self.current_customer = None
        else:
            print("Tidak ada pelanggan yang sedang dilayani.")

    def display_queue(self):
        if self.queue.is_empty():
            print("Antrian kosong.")
        else:
            print("Antrian:")
            for customer in self.queue.items:
                print(customer)


# Fungsi untuk menampilkan menu
def print_menu():
    print("==== Menu Kasir ====")
    print("1. Tambah Pelanggan")
    print("2. Layani Pelanggan")
    print("3. Selesai Melayani")
    print("4. Tampilkan Antrian")
    print("5. Keluar")


# Fungsi untuk memproses pilihan menu
def process_menu_choice(choice, cashier):
    if choice == "1":
        customer = input("Masukkan nama pelanggan: ")
        cashier.add_customer(customer)
    elif choice == "2":
        cashier.serve_customer()
    elif choice == "3":
        cashier.finish_serving()
    elif choice == "4":
        cashier.display_queue()
    elif choice == "5":
        print("Keluar...")
        exit()
    else:
        print("Pilihan tidak valid.")


# Fungsi utama
def main():
    cashier = Cashier()

    while True:
        print_menu()
        choice = input("Masukkan pilihan (1-5): ")
        process_menu_choice(choice, cashier)
        print()


# Menjalankan program utama
if __name__ == "__main__":
    main()
