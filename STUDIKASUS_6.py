import json

nama_file = "inventaris_namabarang.json"

def baca_data():
    try:
        with open(nama_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]
    
def simpan_data(data):
    with open(nama_file, "w") as file:
        json.dump(data, file, indent=4)

while True:
    print("\n=== SISTEM MANAJEMEN INVENTARIS BARANG ===")
    print("1. Lihat Data Barang")
    print("2. Tambah Barang")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        data = baca_data()

        if len(data) == 0:
            print("Belum ada data barang.")
        else:
            print("\n=== DATA INVENTARIS ===")
            for barang in data:
                print("Nama  :", barang["nama"])
                print("Stok  :", barang["stok"])
                print("Harga :", f"Rp{barang['harga']:,}")
    elif pilihan == "2":
        nama = input("Masukkan nama barang: ")
        try:
            stok = int(input("Masukkan stok barang: "))
            harga = int(input("Masukkan harga barang: "))
        except ValueError:
            print("Stok dan harga harus berupa angka.")
            continue
        data = baca_data()

        barang_baru = {
            "nama": nama,
            "stok": stok,
            "harga": harga
        }

        data.append(barang_baru)
        simpan_data(data)

        print("Data barang berhasil ditambahkan.")

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")