class Barang:
    def __init__(self, nama: str, harga: float, stok: int):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def hitung_total_nilai(self) -> float:
        return self.harga * self.stok

    def __str__(self) -> str:
        return f"{self.nama} | Harga: Rp {self.harga:,.0f} | stok: {self.stok} | total nilai: Rp {self.hitung_total_nilai():,.0f}"

    # --- PENGUJIAN KODE (Tes Bagian 1) ---
# 1. Membuat 2 objek barang baru
laptop = Barang(nama="Laptop Gaming", harga=15000000, stok=3)
mouse = Barang(nama="Mouse Wireless", harga=250000, stok=10)

# 2. Cetak barang (otomatis memanggil __str__)
print(laptop)
print(mouse)

# 3. Cek hasil kalkulasi nilai total laptop saja
print("Total nilai laptop saja:", laptop.hitung_total_nilai())