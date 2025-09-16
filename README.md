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
2) Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
3) Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
4) Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? 
5) Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
6) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
7) Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Tidak ada, penjelasan sangat jelas dan sangat membantu.