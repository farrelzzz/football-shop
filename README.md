# Football Shop
Tugas Individu PBP Ganjil 25/26  
Muhammad Farrel Rajendra - 2406495653 - PBP D  
Link Website: https://muhammad-farrel46-footballshop.pbp.cs.ui.ac.id/  

---  
## Tahapan Pengerjaan  

### 1. Inisiasi Proyek Django  
  * Buat direktori football-shop
  * Buat virtual environment: "python -m venv env"
  * Aktifkan virtual environment: "env\Scripts\activate"
  * Siapkan dependencies dalam requirements.txt, lalu instal: "pip install -r requirements.txt"
  * Buat proyek Django: "django-admin startproject football_news ."

### 2.  Konfigurasi Environment Variables dan Proyek
  * Membuat dan mengonfigurasi .env dan .env.prod
  * Modifikasi settings.py
    * Load environment variables dari .env
    * Konfigurasi bagian ALLOWED_HOSTS, PRODUCTION, dan DATABASES

### 3.  Menjalankan Server  
  * Jalankan migrasi database: "python manage.py migrate"
  * Jalankan server Django: "python manage.py runserver"  

---
