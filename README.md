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
Django AuthenticationForm merupakan form bawaan dari sistem autentikasi Django yang didesain khusus untuk mekanisme login pengguna dengan menyediakan fields yang dibutuhkan pada umumnya dan logika validasi untuk autentikasi pengguna. Kelebihannya adalah mudah digunakan dan sudah menyediakan fields juga logika validasi untuk autentikasi pengguna. Kekurangannya adalah sangat bergantung pada model User, sehingga jika kita mau menambahkan field khusus yang tidak ada di user lain misalnya, maka kita perlu override form-nya atau membuat form yang khusus untuk user tersebut.  

---
### Apa Perbedaan Antara Autentikasi dan Otorisasi? Bagaiamana Django Mengimplementasikan Kedua Konsep Tersebut?  
**`Autentikasi`** merupakan proses untuk memverifikasi siapa pengguna yang menggunakan web aplikasi, sedangkan **`Otorisasi`** merupakan proses untuk memverifikasi apa saja akses yang dimiliki user. Contoh implementasi **`Autentikasi`** oleh Django adalah mekanisme login pengguna dengan menggunakan **`AuthenticationForm`** dan fungsi **`login`** bawaan Django. Lalu, contoh implementasi **`Otorisasi`** oleh Django adalah mekanisme pengguna hanya bisa melihat halaman utama dan detail produk jika ia sudah login, caranya dengan menambahkan dekorator **`@login_requiered(login_url='/login')`** di fungsi-fungsi yang menampilkan halaman utama dan detail produk.

---  
### Apa Saja Kelebihan dan Kekurangan Session dan Cookies Dalam Konteks Menyimpan State di Aplikasi web? 
  * Cookies
    * Kelebihan:
      * Penyimpanan jangka panjang karena data pengguna tetap disimpan di perangkatnya meski browser ditutup.
      * Implementasinya lebih sederhana.
      * Proses yang cepat karena datanya disimpan di sisi klien dan mengurangi beban kerja server.
    * Kekurangan
      * Ukuran penyimpanan terbatas.
      * Pengguna dan pihak ketiga dapat meliht data yang disimpan, sehingga ada kemungkinan data itu disalahgunakan.
        
  * Session
    * Kelebihan
      * Keamanan yang lebih baik karena informasi yang disimpan di server lebih terjaga.
      * Ukuran penyimpanan yang lebih besar.
    * Kekurangan
      * Berakhir saat browser ditutup
      * Overhead kinerja
      * Implementasinya lebih kompleks

---  
### Apakah Penggunaan Cookies Aman Secara Default Dalam Pengembangan Web, atau Apakah Ada Risiko Potensial yang Harus Diwaspadai? Bagaimana Django Menangani Hal Tersebut?  
Secaara default, penggunaan cookies tidak sepenuhnya aman. Seperti yang disampaikan sebelumnya, pihak ketiga bisa saja mengakses data pengguna yang disimpan di cookies dan menyalahgunakannya. Salah satu penanganan yang dilakukan Django adalah menggunakan token CSRF unik saat mengisi data di formulir HTML. Token CSRF akan dicocokkan dengan nilai di cookie CSRF saat permintaan POST diproses. Karena pihak ketiga tidak dapat mengetahui token ini, mereka tidak bisa membuat permintaan yang valid, sehingga melindungi dari serangan CSRF.

---  
### Cara Pengerjaan  
#### 1. Membuat Mekanisme Registrasi
  * Impor **`UserCreationForm`** dan **`messages`** di **`views.py`**. 
  * Membuat fungsi **`register`** di **`views.py`** untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form (menggunakan **`UserCreationForm`**), menampilkan pesan kepada pengguna setelah melakukan suatu aksi (menggunakan **`messages`**), lalu melakukan redirect setelah data form berhasil disimpan (dengan **`return redirect('main:show_main')`**).
  * Membuat template HTML halaman **`register`** bernama **`register.html`** di **`main/templates`**.
  * Impor fungsi **`register`** tadi di **`main/urls.py`**, lalu tambahkan path url ke dalam urlpatterns untuk mengakses fungsi **`register`**.

#### 2. Membuat Mekanisme login
  * Impor **`AuthenticationForm`**, **`authenticate`**, dan **`login`**  di **`views.py`**.
  * Membuat fungsi **`login_user`** di **`views.py`** untuk mengautentikasi pengguna yang ingin login, dengan cara: validasi form login (**`if request.method == 'POST'`**) dan buat session untuk untuk pengguna yang berhasil login (**`login(request, user)`**).
  * Membuat template HTML halaman **`login`** bernama **`login.html`** di **`main/templates`**.
  * Impor fungsi **`login_user`** tadi di **`main/urls.py`**, lalu tambahkan path url ke dalam urlpatterns untuk mengakses fungsi **`login_user`**.
   
#### 3. Membuat Mekanisme logout
  * Impor **`logout`**  di **`views.py`**.
  * Membuat fungsi **`logout_user`** di **`views.py`** untuk melakukan mekanisme **`logout`**, dengan cara: menghapus sesi pengguna yang saat ini masuk (dengan **`logout(request)`**) dan mengarahkan pengguna ke halaman login dalam aplikasi Django (dengan cara **`return redirect('main:login')`**).
  * Menambahkan tombol logout di **`main/templates/main.html`**.
  *  Impor fungsi **`logout_user`** tadi di **`main/urls.py`**, lalu tambahkan path url ke dalam urlpatterns untuk mengakses fungsi **`logout_user`**.
      
#### 4. Membuat Dua (2) Akun Pengguna Dengan Masing-masing Tiga (3) Dummy Data di Lokal
  * Membuat akun pengguna baru dengan klik tombol **`Register now`** di halaman **`login`**.
  * Masukkan username dan password sesuai syarat di halaman **`register`**
  * Klik tombol **`+ Add Product`** di halaman utama, lalu isi keterangan dari produk yang ingin ditambahkan. Ulangi sampai kamu sudah menambahkan tiga produk.
  * Lakukan tiga poin di atas untuk akun pengguna berikutnya.
       
#### 5. Menghubungkan Model Product Dengan User
  * Impor **`User`** di **`main/models.py`**.
  * Tambahkan field **`user`** di model **`Product`**.
  * Lakukan migrasi dengan cara **`python manage.py makemigrations`** dan **`python manage.py migrate`**.
  * Modifikasi fungsi **`create_news`** di **`main/views.py`** agar kita bisa mengisi field **`user`** sebelum menyimpan objek hasil dari form.
  * Modifikasi fungsi **`show_main`** di **`main/views.py`** agar menampilkan halaman utama dengan filter produk berdasarkan pembuatnya (semua atau dirinya sendiri).
  * Tambahkan tombol filter My dan All di **`main.html`**.
  * Tambahkan nama author di **`news_detail.html`**

#### 6. Menampilkan Detail Informasi Pengguna yang Sedang Logged In
  * Modifikasi **`context`** di fungsi **`show_main`** dengan menggganti value dari **`'name'`** menjadi **`request.user.username`** dan menggganti value dari **`'last_login'`** menjadi **`request.COOKIES.get('last_login', 'Never')`**.
  * Karena fungsi **`show_main`** akan melakukan **`return render(request, "main.html", context)`**, maka username yang sedang login beserta waktu terakhir ia login akan ditampilkan di halaman utama.

--- 

## Tugas Individu 5 
### Urutan Prioritas Pengambilan CSS Selector untuk suatu elemen HTML 
 1. Inline Style (semua yang ada di style tag):  style yang ditulis langsung di dalam tag HTML menggunakan atribut style.
 2. ID Selector: menggunakan ID pada tag sebagai selector-nya. ID bersifat unik dalam satu halaman web. ID dapat ditambahkan pada halaman template HTML.
 3. Classes Selector: memungkinkan kita untuk mengelompokkan elemen dengan karakteristik yang sama..
 4. Eleement Selector: memungkinkan kita mengubah properti untuk semua elemen yang memiliki tag HTML yang sama. 
   
### Pentingyna Responsive Design Dalam Pengembangan Aplikasi Web
  * Responsive design penting diterapkan karena menjangkau pengguna di semua perangkat, meningkatkan pengalaman pengguna, peringkat SEO yang lebih baik, efisiensi dalam pemeliharan dan pengembangan, dan bisa meningkatkan penjualan.
  * Contoh aplikasi dengan responsive design: theguardian.com, karena tata letaknya bisa menyesuaikan dengan ukuran layar perangkat milik pengguna, sehingga penggunaannya lebih mudah.
  * Contoh aplikasi tanpa responsive design: spacejam.com, karena tata letak di laptop dengan di hp sama saja, tidak disesuaikan, sehingga penggunaannya kurang nyaman.
### Perbedaan Antara Margin, Border, dan Padding, Serta Cara Implementasinya
Margin adalah ruang transparan di luar elemen yang berfungsi untuk memberi jarak antara elemen tersebut dengan elemen lainnya. Border adalah garis yang mengelilingi elemen, tepat di luar padding. Sementara itu, Padding adalah ruang transparan di dalam border yang menciptakan jarak antara border dengan konten elemen itu sendiri.
Cara implementasinya adalah di dalam file .css kita di suatu .elemen misalnya, kita isi saja margin: {jarak}px, border: {jarak}px, dan padding: {jarak}px.

### Konsep Flex Box dan Grid Layout Beserta Kegunaannya
  * Flexbox
    * dirancang untuk mengatur ruang di antara item dalam sebuah wadah (container), meski saat ukurannya tidak diketahui.     * sangat fleksibel dan bekerja di sepanjang satu sumbu saja, baik horizontal maupun vertikal.
    * bisa digunakan untuk membuat navigasi bar, layout komponen kecil, dan distribusi ruang.
  * Grid
    * dirancang untuk menangani tata letak halaman yang kompleks
    * dengan grid kita bisa membuat sumbu baris dan kolom secara bersamaan seperti di microsoft excel, sehingga penempatannya lebih presisi.
    * bisa digunakan untuk membuat tata letak halaman utama, galeri gambar, sampai form yang lebih advanced.

### Cara Pengerjaan
#### 1. Implementasi Fungsi Mengedit Produk
  * Buat fungsi delete_product
    ```css 
    def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)
    ```
  * import fungsi delete_product ke urls.py
  * letakkan path nya di urlpatterns
    ```css
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    ```
#### 2. Implementasi Fungsi Menghapus Produk
  * Buat fungsi edit_product
    ```css
    def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
    ```
  * import fungsi edit_product ke urls.py
  * letakkan path nya di urlpatterns
    ```css
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    ```
#### 3. Kustomisasi Halaman Login
  ```css
{% extends 'base.html' %}

{% block meta %}
<title>Login - Football Shop</title>
{% endblock meta %}

{% block content %}
<div class="bg-gray-900 w-full min-h-screen flex items-center justify-center p-8"> <!--ubah background ke abu abu gelap-->
  <div class="max-w-md w-full">
    <div class="bg-gray-800 rounded-lg border border-white p-6 sm:p-8 form-style"> <!--card buat login juga jadi abu abu gelap-->
      <div class="text-center mb-8">
        <h1 class="text-2xl font-bold text-white mb-2">Sign In</h1> <!--warna teks jadi putih terang-->
        <p class="text-gray-400">Welcome back to Football Shop</p>
      </div>

      <!-- Form Errors Display -->
      {% if form.non_field_errors %}
        <div class="mb-6">
          {% for error in form.non_field_errors %}
            <div class="px-4 py-3 rounded-md text-sm border bg-red-50 border-red-200 text-red-700">
              {{ error }}
            </div>
          {% endfor %}
        </div>
      {% endif %}

      {% if form.errors %}
        <div class="mb-6">
          {% for field, errors in form.errors.items %}
            {% if field != '__all__' %}
              {% for error in errors %}
                <div class="px-4 py-3 rounded-md text-sm border bg-red-50 border-red-200 text-red-700 mb-2">
                  <strong>{{ field|title }}:</strong> {{ error }}
                </div>
              {% endfor %}
            {% endif %}
          {% endfor %}
        </div>
      {% endif %}

      <form method="POST" action="" class="space-y-6">
        {% csrf_token %}
        
        <div>
          <label for="username" class="block text-sm font-medium text-white mb-2">Username</label> <!--ubah warna teks di label-->
          <input 
            id="username" 
            name="username" 
            type="text" 
            required 
            class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-white rounded-md focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition-colors" 
            placeholder="Enter your username">
        </div>

        <div>
          <label for="password" class="block text-sm font-medium text-white mb-2">Password</label> <!--ubah warna teks di label-->
          <input 
            id="password" 
            name="password" 
            type="password" 
            required 
            class="w-full px-4 py-3 bg-gray-700 border border-gray-600 text-white rounded-md focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition-colors" 
            placeholder="Enter your password">
        </div>

        <button 
          type="submit" 
          class="w-full bg-blue-600 text-white font-medium py-3 px-4 rounded-md hover:bg-blue-700 transition-colors">
          Sign In
        </button>
      </form>

      <!-- Messages Display -->
      {% if messages %}
        <div class="mt-6">
          {% for message in messages %}
            <div 
              class="
                px-4 py-3 rounded-md text-sm border
                {% if message.tags == 'success' %}
                  bg-blue-50 border-blue-200 text-blue-700
                {% elif message.tags == 'error' %}
                  bg-red-50 border-red-200 text-red-700
                {% else %}
                  bg-gray-700 border-gray-600 text-gray-300
                {% endif %}
              ">
              {{ message }}
            </div>
          {% endfor %}
        </div>
      {% endif %}

      <div class="mt-6 text-center pt-6 border-t border-gray-700"> <!-- garis pemisah dan teks di bagian bawah diubah -->
        <p class="text-gray-400 text-sm">
          Don't have an account? 
          <a href="{% url 'main:register' %}" class="text-blue-500 hover:text-blue-400 font-medium">
            Register Now
          </a>
        </p>
      </div>
    </div>
  </div>
</div>
{% endblock content %}
  ```
#### 4. Kustomisasi Halaman Register
```css
{% extends 'base.html' %}

{% block meta %}
<title>Register - Football Shop</title>
{% endblock meta %}

{% block content %}
<div class="form-style">
  <div class="min-h-screen bg-gray-900 flex items-center justify-center p-8">
    <div class="max-w-md w-full relative z-10">
      <div class="bg-gray-800 border border-gray-200 rounded-lg p-8 shadow-sm">
      <div class="text-center mb-8">
        <h2 class="text-2xl font-semibold text-white mb-2">Join Us</h2>
        <p class="text-gray-500">Create your Football Shop account</p>
      </div>

      <!-- Form Errors Display -->
      {% if form.non_field_errors %}
        <div class="mb-6">
          {% for error in form.non_field_errors %}
            <div class="px-4 py-3 rounded text-sm border bg-red-50 border-red-200 text-red-700">
              {{ error }}
            </div>
          {% endfor %}
        </div>
      {% endif %}

      {% if form.errors %}
        <div class="mb-6">
          {% for field, errors in form.errors.items %}
            {% if field != '__all__' %}
              {% for error in errors %}
                <div class="px-4 py-3 rounded text-sm border bg-red-50 border-red-200 text-red-700 mb-2">
                  <strong>{{ field|title }}:</strong> {{ error }}
                </div>
              {% endfor %}
            {% endif %}
          {% endfor %}
        </div>
      {% endif %}

      <form method="POST" action="" class="space-y-5">
        {% csrf_token %}
        
        <div>
          <label for="username" class="block text-sm font-medium text-white mb-2">Username</label>
          <input 
            id="username" 
            name="username" 
            type="text" 
            required 
            class="w-full px-4 py-3 border border-gray-300 rounded focus:outline-none focus:border-blue-500 transition duration-200" 
            placeholder="Choose a username">
        </div>

        <div>
          <label for="password1" class="block text-sm font-medium text-white mb-2">Password</label>
          <input 
            id="password1" 
            name="password1" 
            type="password" 
            required 
            class="w-full px-4 py-3 border border-gray-300 rounded focus:outline-none focus:border-blue-500 transition duration-200" 
            placeholder="Create a password">
        </div>

        <div>
          <label for="password2" class="block text-sm font-medium text-white mb-2">Confirm Password</label>
          <input 
            id="password2" 
            name="password2" 
            type="password" 
            required 
            class="w-full px-4 py-3 border border-gray-300 rounded focus:outline-none focus:border-blue-500 transition duration-200" 
            placeholder="Confirm your password">
        </div>

        <button 
          type="submit" 
          class="w-full bg-blue-600 text-white font-medium py-3 px-4 rounded hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition duration-200">
          Create Account
        </button>
      </form>

      <!-- Messages Display -->
      {% if messages %}
        <div class="mt-6">
          {% for message in messages %}
            <div 
              class="
                px-4 py-3 rounded text-sm border
                {% if message.tags == 'success' %}
                  bg-blue-50 border-blue-200 text-blue-700
                {% elif message.tags == 'error' %}
                  bg-red-50 border-red-200 text-red-700
                {% else %}
                  bg-gray-50 border-gray-200 text-gray-700
                {% endif %}
              ">
              {{ message }}
            </div>
          {% endfor %}
        </div>
      {% endif %}

      <div class="mt-6 text-center">
        <p class="text-gray-500 text-sm">
          Already have an account? 
          <a href="{% url 'main:login' %}" class="text-blue-600 hover:text-blue-700 font-medium">
            Sign In
          </a>
        </p>
      </div>
      </div>
    </div>
  </div>
</div>
{% endblock content %}
```
#### 5. Kustomisasi Halaman Tambah Produk
```css
{% extends 'base.html' %}
{% block meta %}
<title>Add Product - Football Shop</title>
{% endblock meta %}

{% block content %}
<div class="bg-gray-900 w-full min-h-screen">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    
    <!-- Back Navigation -->
    <div class="mb-6">
      <a href="{% url 'main:show_main' %}" class="text-white hover:text-white font-medium transition-colors">
        ← Back to Product
      </a>
    </div>
    
    <!-- Form -->
    <div class="bg-gray-800 rounded-lg border border-white p-6 sm:p-8 form-style">
      <div class="mb-8">
        <h1 class="text-2xl font-bold text-white mb-2">Add New Product</h1>
        <p class="text-gray-400">Share your football product with the community</p>
      </div>
      
      <form method="POST" class="space-y-6">
        {% csrf_token %}
        {% for field in form %}
          <div>
            <label for="{{ field.id_for_label }}" class="block text-sm font-semibold text-white mb-2">
              {{ field.label }}
            </label>
            <div class="w-full">
              {{ field }}
            </div>
            {% if field.help_text %}
              <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
            {% endif %}
            {% for error in field.errors %}
              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
            {% endfor %}
          </div>
        {% endfor %}
        
        <div class="flex flex-col sm:flex-row gap-4 pt-6 border-t border-gray-200">
          <a href="{% url 'main:show_main' %}" class="order-2 sm:order-1 px-6 py-3 border border-white text-white rounded-md font-medium hover:bg-gray-50 transition-colors text-center">
            Cancel
          </a>
          <button type="submit" class="order-1 sm:order-2 flex-1 bg-blue-600 text-white px-6 py-3 rounded-md font-medium hover:bg-blue-700 transition-colors">
            Publish Product
          </button>
        </div>
      </form>
    </div>
  </div>
</div>
{% endblock %}
```
#### 6. Kustomisasi Halaman Edit Produk
```css
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>Edit Product - Football Shop</title>
{% endblock meta %}

{% block content %}
<div class="bg-gray-900 w-full min-h-screen">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    
    <!-- Back Navigation -->
    <div class="mb-6">
      <a href="{% url 'main:show_main' %}" class="text-white hover:text-gray-400 font-medium transition-colors">
        ← Back to Product
      </a>
    </div>
    
    <!-- Form -->
    <div class="bg-gray-800 rounded-lg border border-white p-6 sm:p-8 form-style">
      <div class="mb-8">
        <h1 class="text-2xl font-bold text-white mb-2">Edit Product</h1>
        <p class="text-gray-400">Update your football product</p>
      </div>
      
      <form method="POST" class="space-y-6">
        {% csrf_token %}
        {% for field in form %}
          <div>
            <label for="{{ field.id_for_label }}" class="block text-sm font-medium text-white mb-2">
              {{ field.label }}
            </label>
            <div class="w-full">
              {{ field }}
            </div>
            {% if field.help_text %}
              <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
            {% endif %}
            {% for error in field.errors %}
              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
            {% endfor %}
          </div>
        {% endfor %}
        
        <div class="flex flex-col sm:flex-row gap-4 pt-6 border-t border-gray-200">
          <a href="{% url 'main:show_main' %}" class="order-2 sm:order-1 px-6 py-3 border border-white text-white rounded-md font-medium hover:bg-gray-50 transition-colors text-center">
            Cancel
          </a>
          <button type="submit" class="order-1 sm:order-2 flex-1 bg-blue-600 text-white px-6 py-3 rounded-md font-medium hover:bg-blue-700 transition-colors">
            Update Product
          </button>
        </div>
      </form>
    </div>
  </div>
</div>
{% endblock %}
```
#### 7. Kustomisasi Halaman Detail Produk
```css
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>{{ product.title }} - Football Shop</title>
{% endblock meta %}

{% block content %}
<div class="bg-gray-900 w-full min-h-screen">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        
        <!-- Back Navigation -->
        <div class="mb-6">
            <a href="{% url 'main:show_main' %}" class="text-white hover:text-gray-400 font-medium transition-colors">
                ← Back to Product
            </a>
        </div>
        
        <!-- Article -->
        <article class="bg-gray-800 rounded-lg border border-gray-200 overflow-hidden">
            
            <!-- Header -->
            <div class="p-6 sm:p-8">
                <div class="flex flex-wrap items-center gap-2 mb-4">
                    <span class="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-blue-600 text-white">
                        {{ product.get_category_display }}
                    </span>
                    {% if product.is_featured %}
                        <span class="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-yellow-100 text-yellow-800">
                            Featured
                        </span>
                    {% endif %}
                    {% if product.is_product_hot %}
                        <span class="inline-flex items-center px-3 py-1 rounded-md text-xs font-medium bg-red-100 text-red-800">
                            Hot
                        </span>
                    {% endif %}
                </div>
                
                <h1 class="text-3xl sm:text-4xl font-bold text-white leading-tight mb-4">
                    {{ product.name }}
                </h1>
                
                <div class="flex flex-wrap items-center text-sm text-gray-300 gap-4">
                    <time datetime="{{ product.created_at|date:'c' }}">
                        {{ product.created_at|date:"M j, Y g:i A" }}
                    </time>
                    <span>{{ product.product_views }} views</span>
                </div>
            </div>

            <!-- Featured Image -->
            {% if product.thumbnail %}
                <div class="px-6 sm:px-8">
                    <img src="{{ product.thumbnail }}" 
                         alt="{{ product.name }}" 
                         class="w-full h-64 sm:h-80 lg:h-96 object-cover rounded-lg">
                </div>
            {% endif %}

            <!-- Content -->
            <div class="p-6 sm:p-8">
                <div class="prose prose-lg max-w-none">
                    <div class="text-white leading-relaxed whitespace-pre-line text-base sm:text-lg">
                        {{ product.description }}
                    </div>
                </div>
            </div>

            <!-- Author Info -->
            <div class="border-t border-gray-200 p-6 sm:p-8 bg-gray-50">
                <div class="flex items-center justify-between">
                    <div>
                        <div class="font-medium text-gray-900">
                            {% if product.user %}
                                <p>Author: {{ product.user.username }}</p>
                            {% else %}
                                <p>Author: Anonymous</p>
                            {% endif %}
                        </div>
                        <p class="text-sm text-gray-700">Author</p>
                    </div>
                </div>
            </div>
        </article>
    </div>
</div>
{% endblock content %}
```
#### 8. Kustomisasi Halaman Daftar Produk
```css
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>Football Product</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}
<div class="bg-gray-900 w-full pt-16 min-h-screen">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">

    <!-- Header Section -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-white mb-2">Explore the Latest Football Essentials</h1>
      <p class="text-gray-400">Scroll Through Our Collection and Elevate Your Play</p>
    </div>

    <!-- Filter Section -->
    <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-8 bg-gray-800 rounded-lg border border-white p-4">
      <div class="flex space-x-3 mb-4 sm:mb-0">
        <a href="?" class="{% if request.GET.filter == 'all' or not request.GET.filter  %} bg-blue-600 text-white border border-white{% else %}bg-white text-gray-700 border border-gray-300{% endif %} px-4 py-2 rounded-md font-medium transition-colors hover:bg-white hover:text-blue-600 hover:border-blue-600">
          All Product
        </a>
        <a href="?filter=my" class="{% if request.GET.filter == 'my' %} bg-blue-600 text-white{% else %}bg-white text-gray-900 border border-gray-900{% endif %} px-4 py-2 rounded-md font-medium transition-colors hover:bg-white hover:text-blue-600 hover:border-blue-600">
          My Product
        </a>
      </div>
      {% if user.is_authenticated %}
        <div class="text-sm text-gray-400">
          Last login: {{ last_login }}
        </div>
      {% endif %}
    </div>

    <!-- Product Grid -->
    {% if not product_list %}
      <div class="bg-gray-800 rounded-lg border border-white p-12 text-center">
        <div class="w-32 h-32 mx-auto mb-4">
          <img src="{% static 'image/no-image.jpg' %}" alt="No product available" class="w-full h-full object-contain">
        </div>
        <h3 class="text-lg font-medium text-white mb-2">No product found</h3>
        <p class="text-gray-200 mb-6">Be the first to share football product with the community.</p>
        <a href="{% url 'main:add_product' %}" class="inline-flex items-center px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors">
          Add Product
        </a>
      </div>
    {% else %}
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {% for product in product_list %}
          {% include 'card_product.html' with product=product %}
        {% endfor %}
      </div>
    {% endif %}
  </div>
</div>
{% endblock content %}
```
#### 9. Buat Tombol Edit dan Hapus Produk Untuk Setiap Card Product
```css
{% load static %}
<article class="bg-gray-800 rounded-lg border border-white hover:shadow-lg transition-shadow duration-300 overflow-hidden">
  <!-- Thumbnail -->
  <div class="aspect-[16/9] relative overflow-hidden">
    {% if product.thumbnail %}
      <img src="{{ product.thumbnail }}" alt="{{ product.title }}" class="w-full h-full object-cover">
    {% else %}
      <div class="w-full h-full bg-gray-200"></div>
    {% endif %}

    <!-- Category Badge -->
    <div class="absolute top-3 left-3">
      <span class="inline-flex items-center px-2.5 py-0.5 rounded-md text-xs font-medium bg-blue-600 text-white">
        {{ product.get_category_display }}
      </span>
    </div>

    <!-- Status Badges -->
    <div class="absolute top-3 right-3 flex space-x-2">
      {% if product.is_featured %}
        <span class="inline-flex items-center px-2 py-1 rounded text-xs font-medium bg-yellow-100 text-yellow-800">
          Featured
        </span>
      {% endif %}
      {% if product.is_product_hot %}
        <span class="inline-flex items-center px-2 py-1 rounded text-xs font-medium bg-red-100 text-red-800">
          Hot
        </span>
      {% endif %}
    </div>
  </div>

  <!-- Content -->
  <div class="p-5">
    <div class="flex items-center text-sm text-gray-300 mb-3">
      <time datetime="{{ product.created_at|date:'c' }}">
        {{ product.created_at|date:"M j, Y" }}
      </time>
      <span class="mx-2">•</span>
      <span>{{ product.product_views }} views</span>
    </div>

    <h3 class="text-lg font-semibold text-white mb-3 line-clamp-2 leading-tight">
      <a href="{% url 'main:show_product' product.id %}" class="hover:text-blue-600 transition-colors">
        {{ product.name }}
        <p> Rp. {{product.price}} </p>
      </a>
    </h3>

    <p class="text-gray-200 text-sm leading-relaxed line-clamp-3 mb-4">
      {{ product.description|truncatewords:20 }}
    </p>

    <!-- Action Buttons -->
    {% if user.is_authenticated and product.user == user %}
      <div class="flex items-center justify-between pt-4 border-t border-gray-100">
        <a href="{% url 'main:show_product' product.id %}" class="text-blue-600 hover:text-blue-700 font-medium text-sm transition-colors">
          More Details
        </a>
        <div class="flex space-x-2">
          <a href="{% url 'main:edit_product' product.id %}" class="text-gray-300 hover:text-gray-700 text-sm transition-colors">
            Edit
          </a>
          <a href="{% url 'main:delete_product' product.id %}" class="text-red-600 hover:text-red-700 text-sm transition-colors">
            Delete
          </a>
        </div>
      </div>
    {% else %}
      <div class="pt-4 border-t border-gray-100">
        <a href="{% url 'main:show_product' product.id %}" class="text-blue-600 hover:text-blue-700 font-medium text-sm transition-colors">
          More Details →
        </a>
      </div>
    {% endif %}
  </div>
</article>
```
#### Buat Navigation Bar Untuk Fitur-fitur pada Aplikasi yang Responsive Terhadap Perbedaan Ukuran Device, Khususnya Mobile dan Desktop.
```css
<nav class="fixed top-0 left-0 w-full bg-white border-b border-gray-200 shadow-sm z-50">
    <div class="max-w-7xl mx-auto px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <h1 class="text-xl font-semibold text-gray-900">
            <span class="text-blue-600">Football</span> Shop
          </h1>
        </div>
        
        <!-- Desktop Navigation -->
        <div class="hidden md:flex items-center space-x-8">
          <a href="/" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">
            Home
          </a>
          <a href="{% url 'main:add_product' %}" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">
            Add Product
          </a>
        </div>
        
        <!-- Desktop User Section -->
        <div class="hidden md:flex items-center space-x-6">
          {% if user.is_authenticated %}
            <div class="text-right">
              <div class="text-sm font-medium text-gray-900">{{ name|default:user.username }}</div>
              <div class="text-xs text-gray-500">{{ npm|default:"Student" }} - {{ class|default:"Class" }}</div>
            </div>
            <a href="{% url 'main:logout' %}" class="text-red-600 hover:text-red-700 font-medium transition-colors">
              Logout
            </a>
          {% else %}
            <a href="{% url 'main:login' %}" class="text-gray-600 hover:text-gray-900 font-medium transition-colors">
              Login
            </a>
            <a href="{% url 'main:register' %}" class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded font-medium transition-colors">
              Register
            </a>
          {% endif %}
        </div>
        
        <!-- Mobile Menu Button -->
        <div class="md:hidden flex items-center">
          <button class="mobile-menu-button p-2 text-gray-600 hover:text-gray-900 transition-colors">
            <span class="sr-only">Open menu</span>
            <div class="w-6 h-6 flex flex-col justify-center items-center">
              <span class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm"></span>
              <span class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm my-0.5"></span>
              <span class="bg-current block transition-all duration-300 ease-out h-0.5 w-6 rounded-sm"></span>
            </div>
          </button>
        </div>
      </div>
    </div>
    <!-- Mobile Menu -->
    <div class="mobile-menu hidden md:hidden bg-white border-t border-gray-200">
      <div class="px-6 py-4 space-y-4">
        <!-- Mobile Navigation Links -->
        <div class="space-y-1">
          <a href="/" class="block text-gray-600 hover:text-gray-900 font-medium py-3 transition-colors">
            Home
          </a>
          <a href="{% url 'main:add_product' %}" class="block text-gray-600 hover:text-gray-900 font-medium py-3 transition-colors">
            Add Product
          </a>
        </div>
        
        <!-- Mobile User Section -->
        <div class="border-t border-gray-200 pt-4">
          {% if user.is_authenticated %}
            <div class="mb-4">
              <div class="font-medium text-gray-900">{{ name|default:user.username }}</div>
              <div class="text-sm text-gray-500">{{ npm|default:"Student" }} - {{ class|default:"Class" }}</div>
            </div>
            <a href="{% url 'main:logout' %}" class="block text-red-600 hover:text-red-700 font-medium py-3 transition-colors">
              Logout
            </a>
          {% else %}
            <div class="space-y-3">
              <a href="{% url 'main:login' %}" class="block text-gray-600 hover:text-gray-900 font-medium py-3 transition-colors">
                Login
              </a>
              <a href="{% url 'main:register' %}" class="block bg-green-600 hover:bg-green-700 text-white font-medium py-3 px-4 rounded text-center transition-colors">
                Register
              </a>
            </div>
          {% endif %}
        </div>
      </div>
    </div>
    <script>
      const btn = document.querySelector("button.mobile-menu-button");
      const menu = document.querySelector(".mobile-menu");
    
      btn.addEventListener("click", () => {
        menu.classList.toggle("hidden");
      });
    </script>
  </nav>
```
## Tugas Individu 6
### Perbedaan Synchronous Request dengan Asynchronous Request
 * Synchronous Request
   * Blocking: kode akan berhenti dan menunggu sampai respons dari server sudah selesai sebelum melanjutka eksekusi kode berikutnya.
   * Pengalaman Pengguna (User Experience): di browser, antarmuka pengguna (User Interface) jadi tidak responsif selama request berlangsung karena thread utama yang menangani User Interface juga di-blocking.
   * Penggunaan: Jarang digunakan untuk operasi I/O (Input/Output) yang memakan waktu lama di client-side (seperti AJAX) karena buruk bagi User Experience.
     
 * Asynchronous Request
   * Non-Blocking: Kode tidak berhenti dan tidak menunggu respons. Saat permintaan dikirim eksekusi kode langsung lanjut ke baris berikutnya.
   * Pengalaman Pengguna (User Experience): di browser, antarmuka pengguna (User Interface) tetap responsif karena thread utama UI tidak diblokir, sehingga pengguna masih bisa berinteraksi dengan halaman.
   * Penggunaan: umum digunakan untuk sebagian besar interaksi jaringan di web modern (misalnya, menggunakan AJAX, Fetch API, atau XMLHttpRequest dengan pengaturan asinkron) karena meningkatkan User Experience.

### Alur Request-Response AJAX di Django
<img width="569" height="324" alt="image" src="https://github.com/user-attachments/assets/3cee98f5-493d-4980-ac6f-d27d4d85809a" />

  1. Sebuah event terjadi pada halaman web (contohnya tombol submit data ditekan
  2. Sebuah XMLHttpRequest object dibuat oleh JavaScript
  3. XMLHttpRequest object mengirimkan request ke server
  4. Server memproses request tersebut
  5. Server mengembalikan response kembali kepada halaman web
  6. Response dibaca oleh JavaScript
  7. Aksi berikutnya akan dipicu oleh JavaScript sesuai dengan langkah yang dibuat (contohnya memperbarui data di halaman tersebut)
  (kredit: https://pbp-fasilkom-ui.github.io/ganjil-2026/docs/tutorial-5)

### Keuntungan Mengguanakan AJAX Dibandingkan Render Biasa di Django
  * Lebih Responsif karena pengguna tidak perlu menunggu seluruh halaman dimuat ulang hanya untuk perubahan kecil, sehingga memberikan User Experience yang lebih baik.
  * Serveer hanya mengirimkan data yang diperlukan (misal dalam format JSON), bukan seluruh markup HTML, CSS, atau aset lainnya, sehinffa proses dari request sampai response jadi lebih cepat.
  * Hemat bandwith dan mengurangi beban server karena hanya memerlukan data mentah, sehingga server tidak perlu menghabiskan waktu dan sumber daya untuk merender ulang seluruh template HTML untuk setiap pembaruan kecil.
     
### Cara Memastikan Keamanan Saat Menggunakan AJAX Untuk Fitur Login Dan Register di Django
  * Perlindungan terhadap CSRF (Cross-Site Request Forgery)
    * Pastikan setiap permintaan (request) AJAX dengan POST ke view Django menyertakan CSRF Token yang valid.
    * Django bisa menolak jika permintaan tidak memiliki token atau tokennya tidak cocok.
    * CSRF Token bisa didapatkan dari cookie.
  * Enkripsi Data (HTTPS)
    * Selalu gunakan HTTPS di lingkungan (environment) produksi.
    * HTTPS mengenkripsi semua data yang dikirimkan antara browser pengguna dan server, sehingga username dan password yang dikirimkan (saat kita login misalnya) tidak terlihat oleh pihak ketiga.
  * Validasi Data di Sisi Server
    * Meski sudah melakukan validasi di sisi klien dengan JavaScript, kita perlu validasi lagi di sisi server Django agar lebih aman.
    * Kita bisa menggunakan Forms atau Rest Framework Serializers milik Django untuk memastikan data-data yang dikirim pengguna formatnya sudah benar dan aman. 
  * Pengelolaan Sesi dan Otentikasi
    * Setelah login berhasil melalui AJAX, kita bisa gunakan fungsi bwaan Django untuk menetapkan sesi kepada pengguna dan mengurus pembuatan cookie sesi yang aman. Fungsi yang dimaksud adalah **`django.contrib.auth.login(request, user)`**
    * Pastikan password yang disimpan di basis data sudah di-hash 
  * Menghindari Pengembalian Data Sensitif
    * Meminimalkan respons JSON dengan hanya mengirimkan informasi yang dibutuhkan saja. Misal saat kita login, JSON hanya mengirimkan pesan login-nya sukses atau gagal.
    * Jangan pernah menyertakan data sensitif (seperti password) dalam respons JSON yang dikirim kembali ke browser.
       
### Bagaimana AJAX Memengaruhi Pengalaman Pengguna (User Experience) pada Website
AJAX bisa membuat website lebih responsif dan terasa lebih cepat karena membuat pengguna tidak perlu menunggu lama untuk melihat pembaruan yang dia lakukan di website. Hal itu bisa terjadi karena AJAX hanya memuat data yang benar-benar baru/diperlukan, bukan semua markup HTML, CSS, dan aset lainnya. Selain itu, AJAX bekerja secara asynchronous, sehingga permintaan yang dikirimkan bisa dikerjakan tanpa menunggu permintaan saat ini selesai dahulu dan tanpa mengurangi interaksi pengguna dengan elemen User Interface lainnya.



