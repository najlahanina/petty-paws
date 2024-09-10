1.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Membuat sebuah proyek Django baru.
      Pertama, buat direktori baru untuk dijadikan lokal direktori dan repository github bernama petty-paws.
      Kedua, buka direktori tersebut pada vscode dan jalankan git init, git config user.name, dan git config user.email pada terminal untuk kebutuhan repository github.
      Ketiga, buat repository baru pada github bernama petty-paws.
      Keempat, menjalankan perintah git branch -M main, git remote add origin https://github.com/najlahanina/petty-paws.git, dan git push -u origin main untuk membuat  branch dengan nama main, menghubungkan lokal direktori dengan repository github, dan uodate semua perubahan ke github.
      Kelima, menjalankan perintah python3 -m venv env dan source env/bin/activate untuk membuat dan mengaktifkan virtual environment untuk directory yang akan digunakan untuk pengembangan proyek Django
      Keenam, 

    - Membuat aplikasi dengan nama main pada proyek tersebut.
      Pertama, menjalankan perintah python3 manage.py startapp main untuk membuat app baru bernama main pada terminal yang sama.
      Kedua, membuka file settings.py dan tambahkan 'main' pada variable INSTALLED_APPS.
      Ketiga, dalam direktori main, membuat direktori baru bernama templates untuk menyimpan file html yang akan digunakan.
      Keempat, pada direktori templates, buat file bernama main.html yang diisi dengan nama aplikasi, nama, npm, dan kelas.

    - Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
      Pertama, buka file urls.py pada direktori petty_paws
      Kedua, tambahkan import "from django.urls import path, include" dan pada variable urlpatters tambahkan path('', include('main.urls')).

    - Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib
      Pertama, buka models.py dan isi dengan atribut yang diperlukan. Saya menggunakan


    -  Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    - Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    - Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

2.  Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![](https://github.com/najlahanina/petty-paws/blob/main/BaganTugas2PBP.jpeg)

Permintaan dari client dikirim melalui Internet, lalu diteruskan ke Python/Django dan diarahkan ke urls.py. Setelah itu, proses berlanjut ke views.py untuk memproses URL yang diminta. Dalam tahap ini, sistem membaca atau menulis data dari/ke models.py dan database. Data kemudian diinput atau ditampilkan melalui templates. File HTML yang sudah digabung dengan berbagai value yang dibutuhkan akan dikembalikan melalui Internet dan akhirnya ditampilkan di perangkat client.



3.  Jelaskan fungsi git dalam pengembangan perangkat lunak!
    Git adalah salah satu jenis dari version control system yang populer digunakan oleh para programmer. Dengan berbagai fitur yang dimilikinya, Git biasa digunakan untuk memantau perubahan kode selama proses pengembangan perangkat lunak. Berikut adalah beberapa fungsi utama Git yang berguna dalam pengembangan pengembangan perangkat lunak:
    - Membantu mengorganisir project
      Dengan git, memungkinkan para programmer untuk memiliki salinan lengkap dari seluruh repository, termasuk riwayat perubahan, commit, dan branch. Hal itu karena fitur Distributed Version Control System (DVCS) yang dimiliki git. Dengan fitur tersebut yang tiap perubahannya dicatat dengan baik maka pengelolaan proyek menjadi lebih terorganisir dan konsisten.
    - Memberikan fleksibilitas 
      Git, yang merupakan perangkat lunak open source dan bersifat cross platform, dapat diinstal dan digunakan tanpa masalah di berbagai sistem operasi, seperti Windows, macOS, dan Linux. Ini memberikan fleksibilitas bagi para programmer dari berbagai latar belakang untuk bekerja dalam sistem operasi yang mereka suka.
    - Memudahkan dalam berkolaborasi
      Melalui fitur merging dan branching, Git juga sangat memudahkan kolaborasi antar developer. Setiap programmer memiliki kemampuan untuk membuat cabang baru untuk mengembangkan fitur atau memperbaiki bug tanpa mempengaruhi cabang utama. Setelah selesai, mereka dapat menggunakan perintah merge untuk menggabungkan perubahan kembali ke kode sumber utama. Selain itu, Git memungkinkan proses berbagi kode melalui fitur push dan pull, yang memudahkan pengintegrasian perubahan antar programmer. Caching dan kompresi data mendukung proses commit, branching, dan merge Git, yang membuatnya tetap cepat bahkan pada proyek yang besar.

4.  Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    Menurut saya, framework Django dijadikan permulaan untuk pembelajaran pengembangan perangkat lunak karena framework ini menggunakan bahasa Python sebagai basisnya. Seperti yang kita ketahui, Python merupakan bahasa pemrograman yang termasuk mudah untuk dipelajari untuk pemula karena sintaksnya yang sederhana dan bahasa yang digunakan masih mendekati bahasa “manusia”. Dengan struktur kode yang jelas tentunya akan memudahkan para developer untuk membaca dan memahaminya sehingga akan mempermudah mereka dalam pengembangan perangkat lunak. 

5.  Mengapa model pada Django disebut sebagai ORM?
    Model pada Django disebut dengan ORM (Object-Relational Mapping) karena model ini berfungsi untuk memetakan objek dalam Python ke dalam struktur basis data relasional. Model ini juga memungkinkan developer untuk berinteraksi dengan data menggunakan operasi objek Python tanpa harus menulis query SQL secara langsung. Selain itu, model pada Django disebut ORM karena model ini juga mendukung pengelolaan relasi antar model dalam basis data. Contohnya yaitu One-to-One, One-to-Many, dan Many-to-Many. Dengan didefinisikan menggunakan bidang ForeignKey, OneToOneField, dan ManyToManyField, developer akan mendapat relasi antar model secara intuitif dan model ini akan menangani pembuatan relasi tersebut dalam basis data secara otomatis.  
