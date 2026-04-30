import random

class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self._kode_produk = None #ini ya ibu tambahannya, untuk nyiapin tempat data asli (atribut private)
        
        self.kode_produk = None #yang ini untuk manggil setter

    @property
    def kode_produk(self):
        return self._kode_produk

    @kode_produk.setter
    def kode_produk(self, value):
        if value is None:
            self._kode_produk = f"DBY{random.randint(100,999)}"
        else:
            self._kode_produk = value