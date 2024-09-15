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
  - Jalankan proyek dengan perintah python3 manage.py runserver dan buka http://localhost:8000/ utnuk melihat web yang sudah dibuat.

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



## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Berguna untuk konektivitas antar komponen karena platform terdiri dari berbagai komponen seperti database, server aplikasi, dan front-end. Dengan data delivery maka data dapat dipindahkan di antara komponen-komponen tersebut dengan cara yang efisien sehingga dapat bekerja dengan baik.
Menjaga keamanan data karena semakin tingginya ancaman keamanan siber. Data delivery dapat melindungi data tersebut  agar tetap rahasia selama transmisi dengan menerapkan enkripsi dan otentikasi. Enkripsi adalah mengubah data menjadi bentuk yang tidak terbaca sedangkan otentikasi untuk memastikan bahwa yang terlibat dalam pertukaran data adalah pihak yang sah. 
Dapat mengelola trafik dan kinerja. Dalam platform yang berskala besar, jumlah data yang dikirim biasanya juga akan besar dan kompleks. Dengan data delivery, platform dapat mengelola trafik yang tinggi dengan menggunakan teknik load balancing dan caching. 

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
XML dan JSON keduanya memiliki tujuan yang sama yaitu untuk menyimpan dan mengirimkan data. Namun, ada beberapa perbedaan antara keduanya yang membuat JSON lebih populer dibandingkan XML.

1. Syntax yang digunakan dalam JSON cenderung lebih sederhana dan ringkas dibandingkan XML. Data di JSON diwakili oleh objek dan array yang mudah dibaca dan ditulis, sedangkan XML memerlukan tag pembuka dan penutup yang membuatnya lebih rumit dan panjang.

2. JSON terintegrasi dengan JavaScript  sehingga mempermudah pengembangan aplikasi web. Data dalam format JSON bisa langsung digunakan dalam kode JavaScript tanpa memerlukan parsing yang rumit, berbeda dengan XML yang membutuhkan parsing tambahan.

3. Dokumentasi skema pada JSON bersifat sederhana dan lebih fleksibel. Sedangkan pada XML dokumentasi skema bersifat kompleks dan kurang fleksibel.

Meskipun secara umum JSON lebih baik dalam banyak kasus dibandingkan XML, XML tetap memiliki kelebihan dalam situasi tertentu. XML lebih fleksibel dalam mendukung struktur data yang kompleks, seperti data biner, timestamp, dan cocok untuk dokumen yang memerlukan markup atau metadata yang rumit. Jadi menurut saya, JSON lebih baik untuk pengiriman data sederhana dan efisien, sedangkan XML lebih cocok untuk dokumen dengan struktur data yang lebih kompleks. 

## 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django berfungsi untuk memeriksa apakah data yang dikirim melalui form memenuhi syarat validasi yang telah didefinisikan. Method ini juga memastikan bahwa input dari pengguna sudah benar sebelum diproses lebih lanjut. Method ini akan memeriksa validitas data dengan melihat apakah semua field dalam form sesuai dengan aturan validasi. Jika semua data valid, method ini mengembalikan nilai True dan mengisi atribut cleaned_data yaitu sebuah dictionary berisi data yang sudah divalidasi dan siap digunakan. Jika data tidak valid, Django menambahkan pesan kesalahan ke form dan mengembalikan False dan memungkinkan penanganan error yang tepat.

Method ini diperlukan karena berperan penting dalam menjamin integritas data dengan memastikan bahwa hanya data valid yang diproses, sesuai dengan aturan yang ditentukan, sehingga mencegah potensi kesalahan atau inkonsistensi dalam aplikasi. Selain itu, method ini memudahkan pengelolaan error karena Django secara otomatis menangani validasi dan kesalahan, sehingga developer dapat dengan mudah menampilkan pesan error yang tepat kepada pengguna. Dengan is_valid(), proses validasi juga disederhanakan, karena validasi dapat dilakukan hanya dengan satu panggilan method, membuat kode lebih bersih dan efisien.

## 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token dibutuhkan saat membuat form di Django untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery), di mana penyerang mengelabui pengguna yang sudah terautentikasi di sebuah situs web untuk melakukan tindakan yang tidak diinginkan, seperti mentransfer dana atau mengubah email. Django menyediakan token CSRF unik untuk setiap sesi pengguna, yang disertakan dalam form dan diperiksa oleh server untuk memastikan bahwa permintaan tersebut berasal dari pengguna sah dan bukan dari sumber berbahaya.

Jika csrf_token tidak ditambahkan, aplikasi rentan terhadap serangan CSRF. Penyerang dapat mengirimkan tautan berbahaya melalui SMS, email, atau pesan obrolan yang, jika diakses oleh pengguna yang sedang login, dapat memicu permintaan berbahaya ke server. Contoh dampaknya bisa berupa perubahan email, transfer dana, atau bahkan akses penuh ke akun pengguna.

Hal tersebut bisa dimanfaatkan penyerang dengan mengarahkan pengguna untuk mengklik tautan berbahaya yang diam-diam mengirimkan permintaan yang tampak sah ke server menggunakan kredensial pengguna. Jika tidak ada token CSRF yang memverifikasi permintaan, server akan mengeksekusi tindakan tersebut, memberi penyerang kendali atas akun atau data pengguna.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat input form untuk menambahkan objek model pada app sebelumnya.

- Pada direktori utama, buat subdirektori bernama templates dan buat file baru bernama base.html. Kemudian isi file tersebut dengan kerangka umum untuk halaman pada proyek nantinya.

- Buka file settings.py lalu tambahkan kode 'DIRS': [BASE_DIR / 'templates'] pada variabel TEMPLATES agar base.html terdeteksi sebagai template.

- Ubah file main.html untuk menggunakan base.html sebagai template utama.

- Buat file baru bernama forms.py pada direktori main dan mengisinya dengan struktur form yang dapat menerima data produk baru. "model = Product" menandakan bahwa isian form akan disimpan sebagai objek Product. "fields" menandakan objek Product memiliki 6 atribut yang dapat diisi melalui form.

- Tambah beberapa import pada file views.py untuk menyediakan akses ke form dan model yang dibutuhkan dalam menampilkan form, memvalidasi input, menyimpan data ke database, serta mengarahkan pengguna ke halaman lain setelah form diproses.

- Setelah itu, buat fungsi baru bernama create_product yang menerima parameter request untuk menghasilkan form untuk tambah data produk ketika data tersebut disubmit pada form.

- Ubah fungsi show_main dengan menambahkan potongan kode berikut "products = Product.objects.all()" dan "'products': products". products akan menyimpan seluruh produk yang ada pada proyek saat ini.

- Buat file baru pada direktori main/templates bernama create_product.html dan isi dengan kode berikut:
  {% extends 'base.html' %} 

  {% block content %}
  <h1>Add New Product</h1>

  <form method="POST">
      {% csrf_token %}
      <table>
          {{ form.as_table }}
          <tr>
              <td></td>
              <td>
                  <input type="submit" value="Add Product"/>
              </td>
          </tr>
      </table>
  </form>

  {% endblock %}

  - {% block content %} ... {% endblock %} adalah konten yang akan mengisi placeholder block content pada base.html
  - <form method="POST> karena user akan memberikan input

  

2. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.

3. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

Buka file urls.py pada direktori main lalu tambahkan import fungsi-fungsi yang sudah dicantumkan pada file views.py dan masukkan urlnya pada variable urlpattern.

- (url)/create-product: Untuk user input product baru

- (url)/xml: Untuk menampilkan representasi seluruh products dalam format XML

- (url)/json: Untuk menampilkan representasi seluruh products dalam format JSON

- (url)/xml/(desired_id): Untuk menampilkan representasi product dengan id yang diinginkan dalam format XML

- (url)/xml/(desired_id): Untuk menampilkan representasi product dengan id yang diinginkan dalam format JSON
