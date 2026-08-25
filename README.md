\# Oscila: Predictive Maintenance Berbasis Edge-AI



\## 1. Deskripsi Proyek

Oscila adalah sistem pemantauan kondisi mesin terintegrasi yang dirancang untuk mendeteksi anomali getaran secara real-time. Mengusung arsitektur Edge-AI pada mikrokontroler ESP32-S3 dengan sensor MPU6050, Oscila memitigasi risiko kerusakan mesin dan mengurangi downtime di sektor Smart Manufacturing.



\## 2. Prasyarat Sistem

\- Docker Desktop: Pastikan aplikasi Docker terinstal dan berjalan.

\- Git: Untuk melakukan clone repositori.

\- Port 8000: Pastikan port 8000 tidak digunakan oleh aplikasi lain.



\## 3. Setup Guide (Instalasi dan Eksekusi)

Panduan ini disediakan agar panitia dapat menjalankan aplikasi secara lokal menggunakan docker compose.

\- Buka terminal pada komputer Anda.

\- Lakukan clone repositori: git clone https://github.com/dudiahay/Oscila
- Masuk ke direktori: cd Oscila

\- Bangun dan jalankan kontainer: docker-compose up -d --build

\- Akses antarmuka sistem melalui browser di alamat: http://localhost:8000/

\- Hentikan layanan dengan perintah: docker-compose down



\## 4. Skenario Pengujian (Mock Data)

Produk ini memiliki mock data mode di mana perangkat lunak tetap bisa berjalan meski tanpa perangkat keras fisik. Jika antarmuka diakses saat server berjalan tanpa ESP32-S3, sistem akan otomatis menampilkan "Mode: Mock Data Mode (Hardware Offline)". Sistem akan terus memperbarui prediksi secara dinamis untuk keperluan penjurian.

