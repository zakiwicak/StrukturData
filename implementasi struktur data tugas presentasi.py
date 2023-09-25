class Binatang():
    def __init__(self, nama, umur, warna):
        self._nama = nama
        self._umur = umur
        self._warna = warna

    def get_nama(self):
        return self._nama

    def set_nama(self, nama_baru):
        self._nama = nama_baru

    def get_umur(self):
        return self._umur

    def set_umur(self, umur_baru):
        self._umur = umur_baru

    def get_warna(self):
        return self._warna

    def set_warna(self, warna_baru):
        self._warna = warna_baru


class Harimau(Binatang):
    def __init__(self, nama, umur, warna, jumlah_garis):
        super().__init__(nama, umur, warna)
        self._jumlah_garis = jumlah_garis

    def get_jumlah_garis(self):
        return self._jumlah_garis

    def set_jumlah_garis(self, jumlah_garis_baru):
        self._jumlah_garis = jumlah_garis_baru

    def deskripsi(self):
        print(
            f"Harimau {self._nama} (id: {id(self._nama)}) berusia {self._umur} tahun, berwarna {self._warna}, dan memiliki {self._jumlah_garis} garis.")


class Singa(Binatang):
    def __init__(self, nama, umur, warna, panjang_bulu):
        super().__init__(nama, umur, warna)
        self._panjang_bulu = panjang_bulu

    def get_panjang_bulu(self):
        return self._panjang_bulu

    def set_panjang_bulu(self, panjang_bulu_baru):
        self._panjang_bulu = panjang_bulu_baru

    def deskripsi(self):
        print(f"Singa {self._nama} (id: {id(self._nama)}) berusia {self._umur} tahun, berwarna {self._warna}, dan memiliki bulu sepanjang {self._panjang_bulu} cm.")


def menu():
    while True:
        print("\n-- Menu --")
        print("1. Deskripsi harimau")
        print("2. Deskripsi singa")
        print("3. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            nama = input("Nama harimau: ")
            umur = int(input("Umur harimau: "))
            warna = input("Warna harimau: ")
            jumlah_garis = int(input("Jumlah garis harimau: "))

            harimau = Harimau(nama, umur, warna, jumlah_garis)
            harimau.deskripsi()

        elif pilihan == "2":
            nama = input("Nama singa: ")
            umur = int(input("Umur singa: "))
            warna = input("Warna singa: ")
            panjang_bulu = float(input("Panjang bulu singa (dalam cm): "))

            singa = Singa(nama, umur, warna, panjang_bulu)
            singa.deskripsi()

        elif pilihan == "3":
            break

        else:
            print("Pilihan tidak dikenali. Silakan coba lagi.")


menu()
