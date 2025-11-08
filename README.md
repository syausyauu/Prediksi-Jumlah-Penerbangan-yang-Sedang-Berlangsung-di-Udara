## Prediksi Jumlah Penerbangan yang Sedang Berlangsung di Udara (Concurrent Flight)

Codingan ini bertujuan untuk memprediksi jumlah penerbangan yang sedang berlangsung (concurrent flights) di wilayah Amerika Serikat menggunakan data historis penerbangan domestik tahun 2019. Masalah ini diformulasikan sebagai regresi dan dianalisis menggunakan pendekatan machine learning.

Setiap hari, ribuan penerbangan terjadi di AS. Mengetahui berapa banyak pesawat yang sedang terbang pada waktu tertentu dapat membantu pengambilan keputusan dalam pengelolaan lalu lintas udara, penjadwalan bandara, dan infrastruktur transportasi.

### Dataset
- Sumber: U.S. Department of Transportation (2019)
- Cakupan: Penerbangan domestik di AS
- Ukuran: \~7 juta baris
- Fitur Utama: Waktu keberangkatan, waktu kedatangan, bandara asal, jarak, tanggal penerbangan, dll.

### Langkah Analisis
1. Eksplorasi dan Pembersihan Data
   * Menghapus data null dan outlier
   * Konversi waktu ke format datetime dan validasi durasi penerbangan
2. Feature Engineering
   * Menghitung jumlah penerbangan yang sedang berlangsung berdasarkan overlap waktu
   * Ekstraksi fitur waktu (jam, hari, bulan, dsb)
3. Pemodelan Regresi
   * Dua model dibandingkan:
     * **Random Forest Regressor** (dengan RandomizedSearchCV)
     * **XGBoost Regressor** (dengan GridSearchCV)
   * Evaluasi menggunakan metrik RMSE dan R²

### Hasil

* **XGBoost menghasilkan performa lebih baik** dibanding Random Forest
* Fitur paling berpengaruh: jam keberangkatan, bulan, jarak, dan jumlah penerbangan aktif dalam waktu berdekatan

### Kesimpulan

* Prediksi jumlah penerbangan aktif sangat memungkinkan dengan data waktu dan informasi penerbangan dasar
* XGBoost unggul dalam menangani data kompleks dengan interaksi nonlinier
* Analisis lanjutan dapat dilakukan dengan menambahkan data cuaca atau kepadatan bandara

### Teknologi yang Digunakan
* Python (Pandas, NumPy, Scikit-learn, XGBoost)
* Jupyter Notebook
* Matplotlib & Seaborn
* RandomizedSearchCV, GridSearchCV
