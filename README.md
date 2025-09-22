# Football Shop ⚽️
Tugas Individu PBP Ganjil 25/26  
Muhammad Farrel Rajendra - 2406495653 - PBP D  
Link Website: https://muhammad-farrel46-footballshop.pbp.cs.ui.ac.id/  

---  
## Tugas Individu 2

### Tahapan Pengerjaan  
#### 1. Inisiasi Proyek Django  
  * Buat direktori football-shop
  * Buat virtual environment: **`python -m venv env`**
  * Aktifkan virtual environment: **`env\Scripts\activate`**
  * Siapkan dependencies dalam requirements.txt, lalu instal: **`pip install -r requirements.txt`**
  * Buat proyek Django: **`django-admin startproject football_news .`**

#### 2.  Konfigurasi Environment Variables dan Proyek
  * Membuat dan mengonfigurasi .env dan .env.prod
  * Modifikasi settings.py:
    * Load environment variables dari .env
    * Konfigurasi bagian **`ALLOWED_HOSTS`**, **`PRODUCTION`**, dan **`DATABASES`**

#### 3.  Menjalankan Server  
  * Jalankan migrasi database: **`python manage.py migrate`**
  * Jalankan server Django: **`python manage.py runserver`**

#### 4. Membuat Aplikasi **`main`** dalam Proyek 
  * Buat direktori **`main`**: **`python manage.py startapp main`**
  * Tambahkan **`main`** ke **`INSTALLED_APPS`**

#### 5. Implementasi Model  
  * Isi **`models.py`** dalam aplikasi **`main`** dengan model yang ingin kita buat, yaitu **`Product`** beserta atributnya
  * Migrasi model ke Django: **`python manage.py makemigrations`**
  * Migrasi model ke basis data lokal: **`python manage.py migrate`**

#### 6. Menghubungkan View dan Template  
  * Buat fungsi **`show_main`** dalam **`views.py`** yang berada di **`main`**,
    tujuannya agar bisa mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai
  * Modifikasi template  **`main.html`** agar bisa menampilkan nama aplikasi, nama sendiri, dan npm

#### 7. Konfigurasi Routing URL
  * Buat berkas  **`urls.py`** di dalam  **`main`**
  * Menambahkan  **`path('', show_main, name='show_main')`** dalam **`urlpattern`** yang ada di **`urls.py`** dalam **`main`** 
  * Menambahkan  **`path('', include('main.urls'))`** dalam **`urlpattern`** yang ada di **`urls.py`** dalam direktori proyek **`football-shop`**

#### 8. Deployment Proyek
  * Tambahkan URL deployment PWS dalam **`ALLOWED_HOSTS`** yang berada di **`settings.py`**
  * Push ke GitHub dengan melakukan **`git add`**, **`commit`**, dan **`push`**
  * Push ke PWS: **`git push pws master`**

---
### Peran **`settings.py`** dalam Proyek Django
Dalam proyek Django, **`settings.py`** menjadi tempat di mana semua pengaturan dan konfigurasi seperti URL, daftar aplikasi, daftar host, dan database aplikasi Django didefinisikan. Setiap kali kita mengubah konfigurasi mendasar, modifikasinya dilakukan di **`settings.py`**


---
### Cara Kerja Migrasi Database di Django
  * Buat model di **`models.py`**
  * Migrasi model ke Django: **`python manage.py makemigrations`**. Ini membuat DJango bisa melacak perubahan pada model basis data proyek yang kita buat
  * Migrasi model ke basis data lokal: **`python manage.py migrate`**. Ini  mengubah struktur tabel basis data sesuai dengan perubahan model yang didefinisikan dalam kode terbaru yang kita buat.


---  
### Alasan Django Cocok Untuk Pemula
Karena Django gratis, open source, cepat, memiliki banyak fitur untuk pengembangan web pada umumnya, dan penggunaan MVT cukup memudahkan pemula agar fokus ke proses inti pengembangan. Selain itu, penggunaan Python sebagai bahasa pemrograman membuat kode yang ditulis jadi rapi dan mudah dibaca, sehingga pengembangan bisa dilakukan dengan lebih cepat lagi.

---
### Feedback Untuk Asdos
Tutorial yang diberikan mudah untuk dipahami. Kalaupun ada kendala, bantuan yang diberikan asdos saat sesi tutorial ataupun kolom faq di Discord sudah sangat membantu.  

---  

---  
## Tugas Individu 3  
### Mengapa Kita Memerlukan Data Delivery Dalam Implementasi Sebuah Platform
Karena kita perlu mengirimkan data yang telah diolah server ke tampilan web agar bisa menampilkan informasi atau merespons interaksi pengguna secara efektif. Implementasi data delivery yang baik seperti dengan format JSON dan XML penting dilakukan untuk membuat aplikasi yang responsif dan bisa mendukung berbagai platform dari satu backend yang sama, sehingga proses pengembangan aplikasi jadi lebih efisien.    

--- 

### JSON vs XML  
Saya pribadi lebih suka JSON daripada XML karena sintaksnya lebih sederhana seperti pasangan key-value, sehingga mudah dipahami. Selain itu JSON ebih ringan, lebih cepat diurai, dan cocok untuk aplikasi web modern dan API. Itulah beberapa alasan yang menjadikan JSON lebih populer daripada XML.  

---  
### Fungsi Method is_valid() Pada Form Django  
Method is_valid() pada form Django berfungsi untuk memvalidasi data yang dikirim oleh pengguna. Setelah itu, data akan tipe data dari masukan pengguna akan disesuaikan dengan memanggil method clean(). Lalu, data-data yang sudah disesuaikan disimpan di atribut cleaned_data milik form. Method is_valid() juga akan mengumpulkan pesan error di atribut errors milik form. Terakhir, is_valid() akan mengembalikan boolean True jika semua data yang dimasukkan valid. Sebaliknya jika setidaknya ada 1 saja data yang tidak valid, kembaliannya adalah False.  

---  

### Pentingnya csrf_token Saat membuat Form Django  
csrf_token saat membuat form Django penting karena berfungsi sebagai kunci keamanan utama untuk melindungi aplikasi yang dibuat dari serangan Cross-Site Request Forgery (CSRF).

---  

### Langkah Pengerjaan
  * Membuat fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id di main/views.py yang mengembalikan HttpResponse dengan argumen data pada model yang sudah di-serialize sesuai formatnya (dalam hal ini XML atau JSON) dan tpe kontennya berupa "application/{(JSON atau XML)}"
  * Membuat routing pada URL masing-masing views di main/urls.py dengan menambahkan path di urlpatterns sesuai dengan mode views-nya dan fungsinya
  *  Membuat html di main/templates yang bisa menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.
  *  Membuat html di main/templates untuk menambahkan objek model pada app sebelumnya.
  *  Membuat html di main/templates untuk menampilkan detail dari setiap data objek model.
---

### Feedback Untuk Asdos  
Tutorial yang diberikan mudah untuk dipahami. Kalaupun ada kendala, bantuan yang diberikan asdos saat sesi tutorial, kolom faq, dan voice channel Discord sudah sangat membantu.  

---  
### Akses URL Lewat Postman  
<img width="1771" height="908" alt="Screenshot 2025-09-15 221356" src="https://github.com/user-attachments/assets/c24d7772-6dd9-4cdb-88ad-8ec26d928061" />  
<img width="1780" height="910" alt="Screenshot 2025-09-15 221444" src="https://github.com/user-attachments/assets/3c374056-6de6-4328-a519-5803964e4e90" />  
<img width="1792" height="757" alt="Screenshot 2025-09-15 221545" src="https://github.com/user-attachments/assets/34dd4c92-cb29-4319-88f0-2ceff49f42e7" />  
<img width="1783" height="724" alt="Screenshot 2025-09-15 221626" src="https://github.com/user-attachments/assets/ecc93b46-a2d0-4c5e-aa10-7b872eb11b34" />  

---  

## Tugas Individu 4  
### Apa itu Django AuthenticationForm?   
abc

---
   
### Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?  
abc

---  
### Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web? 
abc

---  
### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?  
abc

---  
### Cara Pengerjaan  
  * **Membuat Fungsi dan Form Registrasi**
    * Impor **`UserCreationForm`** dan **`messages`** di **`views.py`**. 
    * Membuat fungsi **`register`** di **`views.py`** untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form (menggunakan **`UserCreationForm`**), menampilkan pesan kepada pengguna setelah melakukan suatu aksi (menggunakan **`messages`**), lalu melakukan redirect setelah data form berhasil disimpan (dengan **`return redirect('main:show_main')`**).
    * Membuat template HTML bernama **`register.html`** di **`main/templates`**.
    * Impor fungsi **`register`** tadi di **`main/urls.py`**, lalu tambahkan path url ke dalam urlpatterns untuk mengakses fungsi **`register`**.
      
  * **Membuat fungsi dan form login**
    * Impor **`AuthenticationForm`**, **`authenticate`**, dan `login`  di **`views.py`**.
    * Membuat fungsi **`login_user`** di **`views.py`** untuk mengautentikasi pengguna yang ingin login, dengan cara: validasi form login (**`if request.method == 'POST'`**) dan buat session untuk untuk pengguna yang berhasil login (**`login(request, user)`**).
    *  Membuat template HTML bernama **`login.html`** di **`main/templates`**.
    *  Impor fungsi **`login_user`** tadi di **`main/urls.py`**, lalu tambahkan path url ke dalam urlpatterns untuk mengakses fungsi **`login_user`**.
   
  * **Membuat fungsi logout**
    * abc
  * **Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data di lokal**
    * abc
  * **Menghubungkan model Product dengan User**
    * abc
  * **Menampilkan detail informasi pengguna yang sedang logged in**
    * abc

--- 
