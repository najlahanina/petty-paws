## 1.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1.Membuat sebuah proyek Django baru.
      
  - Buat direktori baru untuk dijadikan lokal direktori dan repository github   bernama petty-paws.
     
  - Buka direktori tersebut pada vscode dan jalankan git init, git config user.name, dan git config user.email pada terminal untuk kebutuhan repository github.
    
  - Buat repository baru pada github bernama petty-paws.
      
  - Jalankan perintah git branch -M main, git remote add origin https://github.com/najlahanina/petty-paws.git, dan git push -u origin main untuk membuat  branch dengan nama main, menghubungkan lokal direktori dengan repository github, dan uodate semua perubahan ke github.

  - Jalankan perintah python3 -m venv env dan source env/bin/activate untuk membuat dan mengaktifkan virtual environment untuk directory yang akan digunakan untuk pengembangan proyek Django
      
  - Buat file bernama requirements.txt yang kemudian diisi dengan dependencies yang ingin diinstall, lalu jalankan pip install -r requirements.txt untuk menginstallnya
  
  - Jalankan django-admin startproject petty_paws . untuk membuat proyek baru

  - Menambahkan local host pada ALLOWED_HOSTS di settings.py sebagai host yang diizinkan untuk akses app web

  - Buat file bernama .gitignore untuk memberikan informasi mengenai berkas yang perubahannya tidak perlu ditrack git

  - Lakukan add, commit, dan push dari direktori repositori lokal.

2.Membuat aplikasi dengan nama main pada proyek tersebut.

  - Jalankan perintah python3 manage.py startapp main untuk membuat app baru bernama main pada terminal yang sama.

  - Buka file settings.py dan tambahkan 'main' pada variable INSTALLED_APPS.

  - Dalam direktori main, buat direktori baru bernama templates untuk menyimpan file html yang akan digunakan.

  - Pada direktori templates, buat file bernama main.html yang diisi dengan format 2nama aplikasi, nama, npm, dan kelas.

3.Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
      
  - Buka file urls.py pada direktori petty_paws

  - Tambahkan import "from django.urls import path, include" dan pada variable urlpatters tambahkan path('', include('main.urls')).

4.Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib
      
  - Buka file models.py dan isi dengan atribut yang diperlukan. Saya menggunakan 6 atribut yaitu name (CharField), image (ImageField), brands (CharField),  price (IntegerField), categories (TextField), dan description (TextField)

  - Membangun dan menerapkan migrasi model ke database lokal untuk melacak perubahan yang terjadi pada model database.

5.Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

  - Buka file views.py dan buat fungsi show_main yang berisi nama, npm, dan kelas untuk menghubungkan views dan templates

  - Ubah file main.html menjadi template variable seperti {{ nama }} untuk menampilkan value variable yang sudah didefinisikan dalam context.
 
6.Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

  - Buat file urls.py di direktori main dan isi urlpatterns dengan path('', show_main, name='show_main')

  - '' berguna saat mengakses .../main/ akan memanggil show_main dari views.py

7.Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    
  - Pada terminal yang sama, update repository github dengan menjalankan perintah git add ., git commit -m "komentar", dan git push -u origin main

  - Akses PWS kemudian login dan create new project

  - Pada file settings.py tambahkan URL deployment PWS "nisa-najla-pettypaws.pbp.cs.ui.ac.id" pada ALLOWED_HOSTS.

  - Jalankan perintah yang terdapat pada informasi Project Command pada halaman PWS.

  - Jika ada perubahan kembali pada proyek, cukup jalankan perintah git push pws main:master

## 2.  Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![](https://github.com/najlahanina/petty-paws/blob/main/BaganTugas2PBP.jpeg)
Permintaan dari client dikirim melalui Internet, lalu diteruskan ke Python/Django dan diarahkan ke urls.py. Setelah itu, proses berlanjut ke views.py untuk memproses URL yang diminta. Dalam tahap ini, sistem membaca atau menulis data dari/ke models.py dan database. Data kemudian diinput atau ditampilkan melalui templates. File HTML yang sudah digabung dengan berbagai value yang dibutuhkan akan dikembalikan melalui Internet dan akhirnya ditampilkan di perangkat client.

## 3.  Jelaskan fungsi git dalam pengembangan perangkat lunak!

- Membantu mengorganisir project karena memungkinkan para programmer untuk memiliki salinan lengkap dari seluruh repository, termasuk riwayat perubahan, commit, dan branch. Hal itu karena fitur Distributed Version Control System (DVCS) yang dimiliki git sehingga pengelolaan proyek menjadi lebih terorganisir dan konsisten.

- Memberikan fleksibilitas karena git bersifat open source dan  cross platform sehingga dapat diinstall dan digunakan tanpa masalah di berbagai sistem operasi, seperti Windows, macOS, dan Linux. 

- Memudahkan kolaborasi antar developer melalui fitur merging dan branching karena dapat membuat cabang baru untuk mengembangkan fitur atau memperbaiki bug tanpa mempengaruhi cabang utama lalu menggabungkannya kembali dengan perintah merge. Fitur push dan pull juga mempermudah berbagi dan mengintegrasikan perubahan.

## 4.  Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, framework Django dijadikan permulaan untuk pembelajaran pengembangan perangkat lunak karena framework ini menggunakan bahasa Python sebagai basisnya. Seperti yang kita ketahui, Python merupakan bahasa pemrograman yang termasuk mudah untuk dipelajari untuk pemula karena sintaksnya yang sederhana dan bahasa yang digunakan masih mendekati bahasa “manusia”. Dengan struktur kode yang jelas tentunya akan memudahkan para developer untuk membaca dan memahaminya sehingga akan mempermudah mereka dalam pengembangan perangkat lunak. 

Selain itu, Django juga merupakan framework yang bersifat open source. Hal itu membuat dokumentasinya dapat diakses untuk dipelajari secara bebas dan terperinci. Django juga memiliki banyak fitur yang akan membantu developer dalam pengembangan perangkat lunak.

## 5.  Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut dengan ORM (Object-Relational Mapping) karena model ini berfungsi untuk memetakan data dari database relasional dengan objek dalam kode pemrograman yaitu Python. Model ini juga memungkinkan developer untuk berinteraksi dengan data menggunakan operasi objek Python tanpa harus menulis query SQL secara langsung. Dengan Django ORM merepresentasikan tabel di database dan setiap atribut model adalah kolom dari tabel tersebut. ORM otomatis menangani hubungan antara tabel, membuat operasi data menjadi lebih mudah dan abstrak.