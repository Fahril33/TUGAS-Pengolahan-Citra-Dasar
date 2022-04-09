# TUGAS-Pengolahan-Citra-Dasar

<h4>komponen dan file dalam Project ini disusun oleh : </h4><br>
Nama  : M. Fahril <br>
NIM   : F55120033 <br>
Kelas : A 
<br>
<br>
<br>
<br>

<h3> Mengubah citra RGB menjadi citra Grayscale </h3>
<br>
<p>
    Nilai suatupixelmemiliki nilai dalam rentang tertentu, dari nilai minimum sampainilai maksimum. Jangkauan yang digunakan berbeda-beda tergantung dari jeniswarnanya. Namun secara umum untuk citra 8-bit jangkauannya adalah 0–255.Citra dengan penggambaran seperti ini digolongkan ke dalam citra integer.Berikut ini jenis-jenis citra berdasarkan nilaipixelnya (Darma, 2010). <br>
1. Citra Warna(True Color)
Pada citra warna, setiap titik mempunyai warna yang spesifik yang merupakankombinasi dari 3 warna dasar, yaitu merah, hijau, dan biru. Format citra ini seringdisebut sebagai citra RGB (red-green-blue). Setiap warna dasar mempunyaiintensitas sendiri dengan nilai maksimum 255 (8 bit), dan warna minimum adalahputih.Redmemilikiwarna minimum putih dan warna maksimum merah. Greenmemilikiwarna minimum putih dan warna maksimum hijau.Bluememilikiwarnaminimum putih dan warna maksimum biru. Misalnya warna kuning merupakankombinasi warna merah dan hijau sehingga nilai RGB-nya adalah (255 255 0).Dengan demikian setiap titik (pixel) pada citra warna membutuhkan data 3byte(Balza dan Kartika, 2005). <br>
2. Citra Grayscale
Citragrayscale merupakan citra digital yang hanya memiliki satu nilai kanal padasetiap pikselnya, dengan kata lain nilai bagianred,greendanbluememiliki warnayang sama, yaitu warna dari hitam, keabuan, dan putih. Nilai tersebut digunakanuntuk menunjukan tingkat intensitas. Tingkatan keabuan disini merupakan warnaabu dengan berbagai tingkatan dari hitam hingga mendekati putih. Gambar 5menunjukan warnagrayscalepada citra 8bit, yaitu dari warna hitam, keabuan dan putihpada setiap nilai bagian red, green dan blue.
</p> 
<br>
<h3>Transformasi Negatif</h3>
<br>
<p>
    Negatif dari suatu citra dengan tingkat keabuan antara [0, L-1] dapat dihitung menggunakan transformasi negatif dengan rumus berikut: <br>
s = L – 1 – r <br>
Membalik intensitas citra dengan rumus seperti di atas akan menghasilkan negatif dari photo. Pencarian negatif dari suatu citra cocok untuk memperbaiki gambar yang memiliki rincian sub citra terang pada area yang gelap, khususnya jika ukuran dari area gelap cukup dominan.
</p>
<br>
<p>
<h3>Contrast Stretching</h3>
<br>
<p>
    Salah satu di antara fungsi linier sepotong-sepotong yang paling sederhana adalah transformasi “contrast stretching”. Citra dengan kekontrasan rendah bisa disebabkan oleh kurangnya pencahayaan, kurangnya rentang dinamis dari peralatan sensor citra, atau setting lensa yang salah pada saat pengambilan citra. Ide dibalik “contrast stretching” adalah meningkatkan rentang dinamis tingkat keabuan dari citra. <br>
Jika OpenCV sudah terinstal di project, berikut contoh hasil proses Contrast stretching dengan menggunakan gambar citra original sel darah.
</p>
<br>
<h4>Operasi Morfologi</h3>
<br>
<p>
    Pengolahan citra morfologi adalah kumpulan dari operasi non-linier yang berhubungan dengan bentuk atau morfologi fitur dalam sebuah citra. Menurut Wikipedia, operasi morfologi hanya bergantung pada urutan relatif nilai piksel, bukan pada nilai numeriknya, dan oleh karena itu sangat cocok untuk pemrosesan gambar biner. Operasi morfologis juga dapat diterapkan pada gambar skala abu-abu sehingga fungsi transfer cahayanya tidak diketahui dan oleh karena itu nilai piksel absolutnya tidak terlalu menarik atau sedikit. <br>
Teknik morfologi menyelidiki gambar dengan bentuk kecil atau template yang disebut structuring element. Elemen penataan diposisikan di semua lokasi yang mungkin dalam gambar dan dibandingkan dengan lingkungan piksel yang sesuai. Beberapa operasi menguji apakah elemen "cocok" dalam lingkungan, sementara yang lain menguji apakah itu "memukul" atau memotong lingkungan.
</p>
