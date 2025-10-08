# Tugas 2

1) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). 
Saya memulai dengan menganalisis kode tutorial 1 yang kemarin sudah disampaikan, memahami dengan detail mengenai setiap barisnya, setelah itu kembali mengimplementasikannya ke dalam project baru. 

2) Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan 
tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
https://drive.google.com/file/d/1ix1VDBU9cDCMaXzoDPKGfZhtf1i8gfCz/view?usp=sharing

urls.py bertugas untuk melakukan routing, atau mengarahkan ke berkas views.py, apabila url yang diminta cocok dengan pola routing. Setelah itu, views.py mengambil data dari models.py dan memilih template html untuk menampilkan data.


3) Jelaskan peran settings.py dalam proyek Django!
Sebagai pusat konfigurasi dalam implementasi proyek. misalnya, INSTALLED untuk list aplikasi yang dipakai, DATABASES untuk mengatur database, mengatur path template, dll. 

4) Bagaimana cara kerja migrasi database di Django?
Migrasi berguna untuk melakukan sinkronisasi model python dengan strktur tabel database. jadi, ketika ada perubahan pada model, maka perllu dilakukan migrasi agar Django dapat membaca perubahan yang terjadi dan menyesuaikannya dengan tabel database

5) Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Karena Django menggunakan bahasa python yang merupakan bahasa pertama yang dipelajari oleh kebanyakan pemula atau orang-orang yang baru saja terjun ke pemrograman. Selain itu, Django juga menggunakan pola MVT yang biasa digunakan dalam industri

6) Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Tidak ada, penjelasan sangat jelas dan sudah sangat cukup membantu

# Tugas 3

1) Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Karena dalam pengimplementasian sebuah platform, diperlukan adanya transfer data antar sistem atau layanan lain. Data delivery dibutuhkan dalam memastikan data dipindahkan dan dapat diakses dengan efisien dan akurat antar berbagai komponen sistem atau pengguna akhir. 

Selain itu, data delivery juga penting dalam menjaga akuntabilitas dan konsistensi, dimana pengiriman data yang terstruktur memastikan data yang dikirim konsisten sehingga sesuai dengan format yang diharapkan dan dapat diolah datanya dengan baik, untuk kepentingan platform selanjutnya. Integrasi antar sistem menjadi mudah, pengambilan keputusan dapat dilakukan dengan lebih cepat, dan hal ini juga dapat meningkatkan pengalaman pengguna karena kecepatan pengiriman data yang cepat dan terstrukur memungkinkan aplikasi dalam memberikan respons yang cepat, seperti dalam menampilkan konten, gambar, status, dll.

2) Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Keduanya memiliki kelebihan dan kekurangannya masing^masing. terdapat beberapa hal mengapa json menjadi lebih populer:
    a) Ringan dan lebih cepat
        Json lebih singkat dan sederhana jika dibandingkan dengan xml, ukurannya juga lebih kecil sehingga trensfer data menjadi lebih cepat
    b) Mudah dibaca
        Json memiliki struktur yang lebih 'clean' dan mudah dipahami
    c) Didukung oleh banyak browser/platform
        Hampir semua browser modern saat ini dapat memproses data json dengan lancar, sehingga user dapat mengakses berbagai website tanpa masalah

3) Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi ini memastikan field yang diisi oleh user sesuai dengan ketentuan yang telah ditetapkan oleh developer. Django akan mengecek setiap field form berdasarka tipe data, kewajiban mengisi, panjnag maksimal, format khusus, atau validasi kustom lainnya. Jika form tidak valid (atau mengembalikan False), Django akan menyimpan pesan error di form.errors yang dapat ditampilakn ke user. 

Method ini sangat dibutuhkan karena dapat memberikan kemudahan dalam melakukan validasi atas input user yang memerlukan beberapa penyesuain, sehingga developer tidak perlu menambahkan banyak logika tambahan untuk melakukan validasi tersebut. Data yang masuk dijamin aman dan sesuai aturan, pemrosesan data selanjutnya juga menjadi mudah, dan developer dapat lebih mudah dalam menampilkan feedback user. 

4) Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? 
csrf merupakan token keamanan yang unik untuk setiap form. Token ini digunakan untuk memastikan bahwa request POST yang diterima berasal dari situs kita sendiri, bukan dari pihak ketiga lainnya yang berusaha berbuat jahat. csrf sangat dibutuhkan karena dapat mencegah serangan dari penyerang yang membuat request palsu, misalnya dalam mengganti password, menghapus data, atau melakukan transaksi. 

Token unik ini memberikan kepastian bahwa hanya request yang sah yang bisa memodifikasi data. Tanpa token ini, situs akan menjadi lebih rentan terhadap manipulasi oleh pihak ketiga. Jika tidak menambahkab csrf_token, maka form POST akan gagal diproses dengan menampilkan error 403, dan sistem menjadi sangat rentan atas serangan 

5) Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Penyerang dapat melakukan request palsu yang seolah-olah dilakukan oleh user. csrf dapat mengidentifikasi asal request apakah berasal dari situs atau pihak ketiga lainnya. Contohnya, ketika ada request palsu untuk mengganti password user, hal tersebut dapat menjadi masalah karena penyerang dapat mengotak-atik data pribadi user asli, hingga menggunakan asset berharga lainnya. Di sisi lain, user tersebut tidak dapat mengakses akunnya sendiri karena password telah diganti

6) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Saya mencoba untuk membuka tutorial dari awal (0-2) dan benar-benar memahami maksud setiap kode. saya menggunakan bantuan internet dan ai dalam mendalami setiap baris kode, serta tidak lupa dalam mencari sumber yang kredibel. Dalam beberapa hal, saya juga mencoba untuk melakukan modifikasi agar dapat memastikan tingkat pemahaman saya.

7) Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Tidak ada, penjelasan sangat jelas dan sangat membantu.

hasil akses POSTMAN
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)
![alt text](image-4.png)

# Tugas 4
1) Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
Django authentication adalah sistem bawaan dalam kerangka kerja Django yang dirancang untuk melakukan verifikasi identitas pengguna/autentikasi dan memberikan apa yang boleh dilakukan oleh pengguna atau otorisasi. Kelebihannya, sistem ini sudah siap pakai, sehingga developer tidak perlu membuat benar-benar dari nol. Django auth juga sudah mendukung keamanan seperti login attemps. password reset & change. User dan permission dapat langsung dikelola melalui Django admin tanpa interface baru. Sistem ini juga mendukung middleware & decorators seperti @login_required

2) Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi berfungsi untuk mengidentifikasi siapa pengguna tersebut, memastikan bahwa pengguna benar-benar pemilik akun. Misalnya, login dengan menggunakan username & password. Dalam hal ini Django menggunakan django.contrib.auth untuk fitur autentikasi, dimana terdapayt model user dengan atribut username, password, email, dll. fitur login dan logout, serta menggunakan AuthenticationMiddleware untuk mengenali user dari session dan decorator @login_required untuk melindungi view

Otorisasi memnentukan apa yang boleh dilakukan oleh pengguna tersebut. Contohnya, admin dapat menambahkan produk, namun user (pembeli) hanya bisa melihat/membeli katalog produknya saja. Pada django, terdapat fitur permissions dan groups dalam mendukung otorisasi

3) Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Cookies adalah data yang disimpan di sisi klien atau browser. Kelebihannya, data yang disimpan dapat disimpan untuk jangka panjang, tidak membebani servar karena semua data ada pada client, dan mudah diakses untuk kebutuhan tertentu. Kekurangannya, Cookies memiliki kapasitas penyimpanan yang terbatas, hanya 4 KB per cookie. Dalam segi keamanan, cookie juga kurang aman karena mudah diakses dan dimanipulasi oleh user, sehingga anya cocok untuk data ringan, bukan data berat dan sensitif.

Session merupakan data yang disimpan dari sisi server, sedangkan klien hanya mneyimpan sessions id yang biasanya disimpan di cookie. Kelebihannya, session aman untuk menyimpan data sensitif, karena tidak disimpan di client, bisa menyimpan data lebih besar daripada cookie, dan server bisa mengontrol masa hidup dan invalidasi session secara langsung. namun, session membebani server karena harus menyimpan state untuk setiap user. Jika skalabilitas tinggi (banyak user) maka butuh mekanisme secara lanjut agar dapat ditangani. Karena klien tetap menyimpan session id di cookie, maka tetap ada risiko pencurian session

4) Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Tidak otomatis aman secara default. terdapat beberapa hal yang perlu diwaspadai, karena cookies menyimpan data pada sisi klien, yaitu pencurian cookie, manipulasi cookie, cross site scripting, dan cross site request forgery. Django menangani hal ini dengan mengenkripsi session cookie sehingga djangotida menyimpan data session langsung di cookie, melainkan hanya session id. Adapun HttpOnly, yang membuat session cookie tidak dapat diakses oleh JavaScript, sehingga mencegah pencurian via XSS. Selain itu Django juga menggunakan token CSRF dan mengimplementasikan Session Expiration.

5) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Dalam menerapkan fungsi login dan registrasi, saya perlu menambahkan template html baru untuk tampilan login dan registrasi. Selain itu, pada views.py saya melakukan import dari django.contrib.auth untuk nanti melakukan autentikasi, serta menambahkan fungsi khusus untuk melakukan register dan login. Setelah itu, saya menghubungkan semuanya menggunakan perantara yang diatur pada urls.py

Untuk menghubungkan model Product dengan User, saya perlu melakukan import User pada models.py dan manambah atribut baru pada Product untuk menyimpan user dengan menggunakan ForeignKey dan mengakses produk user dengan product.user

Untuk menampilkan username yang sedang login, saya cukup mengakses product.user.username. sedangkan untuk menampilkan last login, saya menggunakan data dari cookies dengan menyimpan data bernama last_login yang isinya timestamp terakhir kalo pengguna login.

# Tugas 5
1) Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas pengambilan CSS dimulai dari Inline Style>ID Selector>Class, Atribut, dan Pseudo-class>Element dan Pseudo-element>Universal Selector.
a. Inline Style
Inline style ditulis langsung di dalam tag html dengan menggunakan atribut style. Hal ini menjadikan inline style lebih prioritas, karena menempel langsung dengan elemen yang ingin diberikan style.
contohnya, ```<p style="color:blue;">Teks ini biruuuu</p>```
b. ID Selector
Menggunakan tanda tagar di depan ID. Karena ID unik, maka penggunaan ID Selector memiliki spesifikasi yang sangat tinggi, karena langsung mengacu kepada satu ID tertentu.
contohnya, ```<p id="judul">Hello</p>``` pada kode HTML, sedangkan pada kode CSS ```#judul { color: blue; }``` yang artinya style tersebut akan diimplementasikan pada text "Hello"
c. Class, Atribut, dan Pseudo-class 
Class dapat digunakan oleh banyak elemen di kode HTML. Berbeda dengan ID yang hanya boleh digunakan oleh salah satu elemen sehingga menjadikannya unik dan langsung menuju ke elemen yang spesifik. Contoh class adalah ```<p class="highlight">Ini teks</p>``` dan pada CSS ditandai dengan diawali titik sebelum nama class (contoh: .highlight). 

Sedangkan atribut, menunjukkan informasi tambahan mengenai elemen tersebut, prioritasnya setara dengan class. Contohnya, pada HTML ```<input type="text" />``` dengan CSS ```[type="text"] { border: 1px solid; } ```. 

Pseudo-class merupakan kondisi tertentu yang sedang berlangsung pada elemen seperti ketika dalam keadaan default, hover, dan selected, contohnya pada HTML ```<a href="#">Link</a>``` dan pada CSS ```<a href="#">Link</a>```

d. Element dan Pseudo-element
Element Selector menargetkan elemen HTML secara langsung berdasarkan tag yang digunakan. Prioritasnya lebih rendah dibanding class dan ID. Contohnya, pada HTML: ```<p>Hello World</p>``` dan pada CSS: ```p { color: black; }``` yang artinya style tersebut akan diterapkan pada semua elemen ```<p>``` di halaman. 

Sedangkan Pseudo-element menargetkan bagian tertentu dari elemen, seperti baris pertama, sebelum atau sesudah konten. Contohnya pada HTML: ```<p>Hello World</p>``` dan pada CSS:```p::first-line { font-weight: bold; }``` yang artinya hanya baris pertama dari teks "Hello World" yang akan dibuat tebal.

e. Universal Selector
Universal Selector menargetkan semua elemen di halaman dengan tanda *, tetapi prioritasnya sangat rendah dibanding selector lain. Contohnya, pada HTML: ```<p>Hello</p> <div>World</div>``` dan pada CSS: ```* { margin: 0; padding: 0; }``` yang artinya semua elemen di halaman akan memiliki margin dan padding nol, kecuali ada aturan lain yang lebih spesifik.

Sedangkan Inheritance (pewarisan) adalah properti yang diturunkan dari elemen induk ke anaknya, seperti color atau font-family. Contohnya pada HTML:
```<div style="color: purple;">```
  ```<p>Hello World</p>```
```</div>```
dan pada CSS tidak perlu ditulis lagi karena properti color diwariskan, sehingga teks "Hello World" akan berwarna ungu.

2) Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design merupakan konsep untuk menyesuaikan tampilan web sesuai dengan device yang sedang dipakai oleh pengguna (desktop, mobile, tablet). Konsep ini penting karena sebagai developer, perlu diperhatikan inklusivitas aplikasi yang dibuat, sehingga aplikasi dapat digunakan secara universal. Contoh aplikasi yang sudah menerapkannya adalah Tokopedia dan Shopee. Sedangkan yang belum menerapkan responsive design adalah Siak-NG, karena memiliki tampilan yang sama baik dalam mode desktop maupun mobile. 

3) Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin merupakan ruang di luar elemen, atau jarak antara elemen dengan elemen lain di sekitarnya. contoh implementasi pada CSS 
```div｛```
  ```margin: 20px;  ```     
  ```margin-top: 10px;  ```
  ```margin-right: 15px; ```
  ```margin-bottom: 10px;```
  ```margin-left: 15px;  ```
```}```

Border merupakan garis atau bingkai yang mengelilingi elemen, dan juga berada di antara padding dan margin. 
contoh implementasi CSS
```div {```
  ```border: 2px solid black;   ```
  ```border-radius: 10px;      ``` 
  ```border-style: dashed;   ```  
  ```border-color: red;       ```
```}```

Sedangkan padding, merupakan jarak yang ada pada kkonten elemen terhadap tepi border. contoh implementasi CSS
```div {```
  ```padding: 20px;       ```
  ```padding-top: 10px;   ```
  ```padding-right: 15px;  ```
  ```padding-bottom: 10px;```
  ```padding-left: 15px;   ```
```}```

4) Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox merupakan sistem layout satu dimensi yang mengatur elemen dalam baris (row) atau kolom (column) secara fleksibel. Flexbox memudahkan penyusunan elemen secara horizontal atau vertikal, pengaturan jarak antar elemen, serta alignment tanpa perlu banyak margin atau padding manual. 
Contoh implementasi CSS

```.container {```
  ```display: flex;               ``` 
  ```flex-direction: row;         ``` 
  ```justify-content: space-between; ``` 
  ```align-items: center;         ```
```}```

```css```
```.item {```
  ```flex: 1;                     ``` 
```}```

Sedangkan grid Layout merupakan sistem layout dua dimensi yang mengatur elemen dalam baris dan kolom secara presisi. Grid Layout sangat cocok untuk layout kompleks seperti dashboard atau galeri, karena dapat mengontrol ukuran, posisi, dan jarak antar elemen dengan mudah. Contoh implementasi CSS:  
```css```
```.container {```
  ```display: grid;                     ```
  ```grid-template-columns: 1fr 2fr 1fr;```
  ```grid-template-rows: auto;          ```
  ```gap: 10px;                         ```
```}```

```css```
```.item1 {```
  ```grid-column: 1 / 3;   ```
```}```

```css```
```.item2 {```
  ```grid-row: 1 / 2;      ```
```}```

5) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Saya mulai dengan membuat halaman-halaman utama seperti login, register, tambah product, edit product, dan detail product agar tampilannya lebih menarik dan user-friendly. Saya memastikan setiap form memiliki label jelas, input field yang nyaman digunakan, dan tombol submit yang menonjol. Saya menambahkan warna kontras, padding dan margin yang rapi.

Saya mendesain halaman daftar product menggunakan card untuk menampilkan setiap produk agar terlihat rapi dan menarik. Saya menggunakan flexbox atau grid layout sehingga card tersusun dengan baik dan ada jarak antar card. Saya menambahkan bayangan, border-radius, dan warna yang konsisten untuk mempercantik tampilannya. Saya juga memastikan halaman ini responsive, misalnya menampilkan 1-3 card per baris di desktop dan 1 card per baris di mobile.

Saya menambahkan logika agar halaman daftar product bisa menyesuaikan dengan kondisi data. Jika belum ada product yang tersimpan, saya menampilkan gambar ilustrasi dan pesan agar pengguna tahu bahwa halaman ini kosong. Jika sudah ada product, saya menampilkan setiap product dalam bentuk card, lengkap dengan gambar, nama, harga, deskripsi, dan dua tombol untuk edit dan hapus, sehingga pengguna bisa langsung melakukan tindakan pada produk yang ada.

Saya membuat navbar yang responsive agar pengguna bisa mengakses fitur-fitur aplikasi dengan mudah, baik di desktop maupun di mobile. Saya menggunakan flexbox untuk menyusun menu item secara horizontal di layar besar, dan menambahkan hamburger menu untuk layar kecil.

# Tugas 6
1) Apa perbedaan antara synchronous request dan asynchronous request?
Synchronous request adalah jenis permintaan yang dikirim dari client ke server di mana browser harus menunggu respons dari server terlebih dahulu sebelum bisa melanjutkan proses lainnya. Artinya, halaman akan "terhenti" sementara hingga server mengembalikan data. Misalnya, ketika pengguna mengirim form login dengan cara konvensional (tanpa AJAX), halaman akan melakukan refresh penuh setelah tombol submit ditekan, karena browser menunggu hasil respon server terlebih dahulu.

Sedangkan asynchronous request (atau dikenal dengan AJAX – Asynchronous JavaScript and XML) memungkinkan browser untuk mengirim dan menerima data dari server tanpa perlu melakukan refresh pada halaman secara keseluruhan. Jadi, pengguna tetap bisa berinteraksi dengan elemen lain di halaman sambil menunggu respon dari server. Cara kerja ini membuat website terasa lebih interaktif dan cepat, karena hanya bagian tertentu dari halaman yang diperbarui, bukan seluruhnya.

2) Bagaimana AJAX bekerja di Django (alur request–response)?
AJAX bekerja dengan cara mengirim request secara asinkron dari client (biasanya melalui JavaScript menggunakan fetch() atau XMLHttpRequest) menuju server Django. Saat pengguna melakukan aksi tertentu, seperti menekan tombol atau mengisi form, JavaScript akan men-trigger fungsi AJAX yang mengirimkan data ke URL tertentu yang sudah diatur di urls.py.

Kemudian, Django akan memproses request tersebut di views.py. Jika views.py mendeteksi bahwa request berasal dari AJAX (biasanya dengan request.headers.get('X-Requested-With') == 'XMLHttpRequest'), maka Django akan memberikan response berupa data JSON. Setelah itu, JavaScript di sisi client akan menerima response tersebut dan memperbarui elemen HTML tertentu (seperti tabel, daftar produk, atau status) tanpa harus me-refresh seluruh halaman. Alur ini menjadikan komunikasi antara client dan server lebih efisien.

3) Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
Keuntungan utama penggunaan AJAX adalah peningkatan kecepatan dan interaktivitas aplikasi web. Dengan AJAX, hanya bagian tertentu dari halaman yang diperbarui, sehingga waktu respon menjadi jauh lebih cepat dibanding render penuh. Misalnya, ketika pengguna menambah produk baru, hanya daftar produk yang diperbarui tanpa perlu memuat ulang seluruh halaman — hal ini membuat pengalaman pengguna menjadi lebih halus dan efisien.

Selain itu, AJAX membantu mengurangi beban server karena tidak perlu mengirim seluruh template HTML setiap kali ada perubahan data kecil. Penggunaan AJAX juga sangat cocok untuk fitur real-time seperti pencarian instan, notifikasi, atau pembaruan status pengguna tanpa perlu reload. Secara keseluruhan, AJAX membantu menciptakan aplikasi yang lebih responsif dan modern.
4) Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
Keamanan saat menggunakan AJAX pada fitur login dan register sangat penting, terutama karena data sensitif seperti username dan password dikirimkan ke server. Untuk memastikan keamanan, Django menyediakan mekanisme CSRF token (Cross-Site Request Forgery token) yang wajib disertakan pada setiap request POST, termasuk yang dikirim melalui AJAX. Token ini memastikan bahwa request memang berasal dari situs resmi, bukan dari pihak ketiga yang berusaha melakukan serangan.

Selain itu, data yang dikirim melalui AJAX sebaiknya selalu menggunakan HTTPS agar terenkripsi selama proses transmisi. Developer juga sebaiknya melakukan validasi data di sisi server menggunakan is_valid() pada form Django, agar tidak ada input yang berbahaya masuk ke sistem. Django juga dapat membatasi percobaan login yang gagal untuk mencegah serangan brute force. Dengan menggabungkan semua lapisan keamanan tersebut, AJAX dapat digunakan dengan aman tanpa mengorbankan perlindungan data pengguna.
5) Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
AJAX memberikan dampak besar terhadap peningkatan User Experience (UX) di sebuah website. Dengan AJAX, interaksi antar pengguna dan sistem menjadi lebih cepat dan dinamis karena halaman tidak perlu dimuat ulang setiap kali ada perubahan kecil. Hal ini membuat pengguna merasa aplikasi lebih responsif dan “hidup”, mirip seperti aplikasi mobile.

Selain itu, AJAX membantu mengurangi gangguan visual seperti reload halaman yang tiba-tiba atau hilangnya posisi scroll pengguna. Contohnya, ketika pengguna menekan tombol "Simpan" pada form, sistem dapat menampilkan pesan “Data berhasil disimpan” secara langsung tanpa memuat ulang seluruh halaman. Pengalaman seperti ini terasa jauh lebih nyaman dan efisien bagi pengguna. Dengan demikian, AJAX membantu menciptakan aplikasi web yang lebih interaktif, cepat, dan menyenangkan untuk digunakan.