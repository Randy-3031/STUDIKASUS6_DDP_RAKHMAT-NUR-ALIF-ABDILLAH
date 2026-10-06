# STUDIKASUS6_DDP_RAKHMAT NUR ALIF ABDILLAH
# Sistem Manajemen Inventaris Barang

NAMA : RAKHMAT NUR ALIF ABDILLAH <br>
NIM : 2609116100

<img width="1366" height="728" alt="● STUDIKASUS_6 py - Intel - Visual Studio Code 10_6_2026 8_49_26 PM" src="https://github.com/user-attachments/assets/ca65643b-501a-4625-8e52-958a0aa03a43" />

**Bagian Awal**
- import json memanggil modul bawaan Python untuk membaca dan menulis file berformat JSON.
- nama_file adalah variabel yang menyimpan nama file tempat data barang disimpan, jadi tidak perlu menulis ulang nama file di banyak tempat.

**Fungsi baca_data()**
- Fungsi ini membaca data barang dari file JSON dan mengembalikannya dalam bentuk list.
- open(nama_file, "r") membuka file dalam mode baca, dan json.load() mengubah isi file menjadi list Python.
- try-except menangani error. Jika file belum ada (FileNotFoundError) atau isinya kosong/rusak (JSONDecodeError), fungsi mengembalikan list kosong [] sehingga program tidak crash.

**Fungsi simpan_data(data)**
- Fungsi ini menyimpan data ke file JSON agar tidak hilang saat program ditutup.
- Mode "w" menulis ulang isi file dengan data terbaru.
- json.dump() mengubah list Python menjadi format JSON, dan indent=4 membuat isi file rapi dan mudah dibaca.**

**Perulangan Utama dan Menu**
- while True membuat program berjalan terus-menerus sampai pengguna memilih keluar (sesuai instruksi soal).
- print menampilkan daftar menu, dan input menerima pilihan pengguna.

<img width="1366" height="728" alt="● STUDIKASUS_6 py - Intel - Visual Studio Code 10_6_2026 8_50_11 PM" src="https://github.com/user-attachments/assets/da47e46c-686c-41a8-bc01-c43f93cec8f6" />

**Menu 1: Lihat Data Barang**
- Memanggil baca_data() untuk mengambil data dari file.
Jika data kosong, program menampilkan pesan "Belum ada data barang".
Jika ada data, for menampilkan nama, stok, dan harga setiap barang. Harga diformat dengan pemisah ribuan lewat f"Rp{...:,}"

**Menu 2: Tambah Barang**
- Pengguna memasukkan nama, stok, dan harga barang. int() mengubah input stok dan harga menjadi angka.
- try-except ValueError mencegah crash jika pengguna mengetik huruf. Program menampilkan pesan error lalu continue kembali ke menu.
- Data lama dibaca dulu dengan baca_data(), supaya barang baru ditambahkan ke data yang sudah ada, bukan menimpanya.
- barang_baru adalah dictionary yang berisi data satu barang.
- data.append() menambahkan barang baru ke list, lalu simpan_data() menyimpannya ke file secara permanen.

**Menu 3: Keluar**
- break menghentikan perulangan while True sehingga program berakhir.

**Pilihan Tidak Valid**
- Jika pengguna memasukkan selain 1, 2, atau 3, program menampilkan pesan dan menu muncul kembali.

<img width="1366" height="728" alt="● STUDIKASUS_6 py - Intel - Visual Studio Code 10_6_2026 8_52_36 PM" src="https://github.com/user-attachments/assets/3faa12e5-2b01-43b0-879c-24386127debe" />
BERIKUT ADALAH TERMINAL DARI KODE DIATAS.

<img width="1366" height="728" alt="● STUDIKASUS_6 py - Intel - Visual Studio Code 10_6_2026 8_53_02 PM" src="https://github.com/user-attachments/assets/c9c0ef8f-6e5f-4d77-803a-583e268d2848" />
BERIKUT ADALAH OUTPUT DARI FILE JSON.
