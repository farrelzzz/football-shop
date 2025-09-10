# Football Shop
Tugas Individu PBP Ganjil 25/26  
Muhammad Farrel Rajendra - 2406495653 - PBP D  
Link Website: https://muhammad-farrel46-footballshop.pbp.cs.ui.ac.id/  

---  
## Tahapan Pengerjaan  

### 1. Inisiasi Proyek Django  
  * Buat direktori football-shop
  * Buat virtual environment: **`python -m venv env`**
  * Aktifkan virtual environment: **`env\Scripts\activate`**
  * Siapkan dependencies dalam requirements.txt, lalu instal: **`pip install -r requirements.txt`**
  * Buat proyek Django: **`django-admin startproject football_news .`**

### 2.  Konfigurasi Environment Variables dan Proyek
  * Membuat dan mengonfigurasi .env dan .env.prod
  * Modifikasi settings.py:
    * Load environment variables dari .env
    * Konfigurasi bagian **`ALLOWED_HOSTS`**, **`PRODUCTION`**, dan **`DATABASES`**

### 3.  Menjalankan Server  
  * Jalankan migrasi database: **`python manage.py migrate`**
  * Jalankan server Django: **`python manage.py runserver`**

### 4. Membuat Aplikasi **`main`** dalam Proyek 
  * Buat direktori **`main`**: **`python manage.py startapp main`**
  * Tambahkan **`main`** ke **`INSTALLED_APPS`**

### 5. Implementasi Model  
  * Isi **`models.py`** dalam aplikasi **`main`** dengan model yang ingin kita buat, yaitu **`Product`** beserta atributnya
  * Migrasi model ke Django: **`python manage.py makemigrations`**
  * Migrasi model ke basis data lokal: **`python manage.py migrate`**

### 6. Menghubungkan View dan Template  
  * Buat fungsi **`show_main`** dalam **`views.py`** yang berada di **`main`**,
    tujuannya agar bisa mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai
  * Modifikasi template  **`main.html`** agar bisa menampilkan nama aplikasi, nama sendiri, dan npm

### 7. Konfigurasi Routing URL
  * Buat berkas  **`urls.py`** di dalam  **`main`**
  * Menambahkan  **`path('', show_main, name='show_main')`** dalam **`urlpattern`** yang ada di **`urls.py`** dalam **`main`** 
  * Menambahkan  **`path('', include('main.urls'))`** dalam **`urlpattern`** yang ada di **`urls.py`** dalam direktori proyek **`football-shop`**

### 8. Deployment Proyek
  * Tambahkan URL deployment PWS dalam **`ALLOWED_HOSTS`** yang berada di **`settings.py`**
  * Push ke GitHub dengan melakukan **`git add`**, **`commit`**, dan **`push`**
  * Push ke PWS: **`git push pws master`**

---
## Peran **`settings.py`** dalam Proyek Django
Dalam proyek Django, **`settings.py`** menjadi tempat di mana semua pengaturan dan konfigurasi seperti URL, daftar aplikasi, daftar host, dan database aplikasi Django didefinisikan. Setiap kali kita mengubah konfigurasi mendasar, modifikasinya dilakukan di **`settings.py`**


---
## Cara Kerja Migrasi Database di Django
  * Buat model di **`models.py`**
  * Migrasi model ke Django: **`python manage.py makemigrations`**. Ini membuat DJango bisa melacak perubahan pada model basis data proyek yang kita buat
  * Migrasi model ke basis data lokal: **`python manage.py migrate`**. Ini  mengubah struktur tabel basis data sesuai dengan perubahan model yang didefinisikan dalam kode terbaru yang kita buat.


---  
## Alasan Django Cocok Untuk Pemula
Karena Django gratis, open source, cepat, memiliki banyak fitur untuk pengembangan web pada umumnya, dan penggunaan MVT cukup memudahkan pemula agar fokus ke proses inti pengembangan. Selain itu, penggunaan Python sebagai bahasa pemrograman membuat kode yang ditulis jadi rapi dan mudah dibaca, sehingga pengembangan bisa dilakukan dengan lebih cepat lagi.

---
## Feedback Untuk Asdos
Tutorial yang diberikan mudah untuk dipahami. Kalaupun ada kendala, bantuan yang diberikan asdos saat sesi tutorial ataupun kolom faq di Discord sudah sangat membantu. 
