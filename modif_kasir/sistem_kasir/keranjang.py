class Keranjang:
    def __init__(self, member=False):
        self.daftar_barang = []
        self.member = member
  
    def tambah_produk(self, produk_baru, jumlah):
        if jumlah <= 0:
            print("jumlah ga valid")
            return
        
        if produk_baru.stok < jumlah:
            print("stok ga cukup")
            return
        
        produk_baru.stok -= jumlah
        self.daftar_barang.append({
            "produk": produk_baru,
            "jumlah": jumlah
        })
        
        print(f"berhasil tambah: {produk_baru.nama} x{jumlah}")
    
    def hapus_produk(self, nama_produk):
        for item in self.daftar_barang:
            if item["produk"].nama == nama_produk:
                item["produk"].stok += item["jumlah"]
                self.daftar_barang.remove(item)
                print(f"{nama_produk} dihapus")
                return
        print("barang ga ketemu")
    
    def hitung_total(self):
        total = 0
        for item in self.daftar_barang:
            total += item["produk"].harga * item["jumlah"]
        return total
  
    def cetak_struk(self):
        print("\n struk belanja ")
        for item in self.daftar_barang:
            p = item["produk"]
            j = item["jumlah"]
            print(f"- {p.nama} x{j} : Rp{p.harga * j}")
      
        total = self.hitung_total()

        if self.member:
            diskon = total * 0.05
            print(f"diskon member (5%) : -Rp{diskon}")
            total -= diskon
        
        ppn = total * 0.11
        print(f"ppn (11%) : Rp{ppn}")
        total += ppn
        
        print(f"total akhir : Rp{total}")
        return total
    
    def bayar(self, uang):
        total = self.cetak_struk()
        
        if uang < total:
            print("uang kurang")
        else:
            kembalian = uang - total
            print(f"uang diterima : Rp{uang}")
            print(f"kembalian : Rp{kembalian}")