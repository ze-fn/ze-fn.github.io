---
layout: distill
title: "Biaya UKT di Negara Bagian Amerika Serikat"
description: Latihan Analisis Data Eksploratif (ADE)
tags: [Statistics, Excel, Bahasa Indonesia]
categories: [Journal]
date: 2026-05-04
authors:
  - name: Zelvy Fauzan
    affiliations:
     name: Independent
featured: false
mermaid:
  enabled: true
  zoomable: true
toc:
  - name: Dataset
  - name: Pembersihan Data
  - name: Penamaan/Pelabelan
  - name: Tipe Data
  - name: Summary Statistics
  - name: Visualisasi
  - name: Validasi
  - name: Verifikasi
  - name: Interpretasi
---

# Dataset

Data diambil dari repository [TidyTuesdayR](https://github.com/rfordatascience/tidytuesday/blob/main/data/2018/2018-04-02/us_avg_tuition.xlsx).

1. Simpan file Excel
2. Buka dataset menggunakan Microsoft Excel atau Google Spreadsheet

> ##### Catatan
>
> Microsoft Excel dan Spreadsheet mungkin akan ada perbedaan sedikit dari segi data direpresentasikan. Saya akan fokus ke Microsoft Excel.
{: .block-warning}

# Pembersihan Data

Analisis data perlu data yang bersih dan rapi. Alur kerja yang biasa dilakukan adalah sebagai berikut:

1. Impor data.
2. Cek penamaan setiap kolom; ubah penamaan jika kurang sesuai
3. Cek tipe data masing-masing kolom; sesuaikan data jika kurang/tidak sesuai
4. Cek _summary statistics_ dari tiap kolom; gunakan skala Log pada kolom tertentu rentang satu kolom tersebut terlalu ekstrim.
5. Visualisasi
6. Validasi
7. Verifikasi
8. Interpretasi

Pada konteks ini, dataset memiliki kolom (1) `State` dan (2) `2004-05` sampai `2015-16`.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/biaya_ukt_negara_bagian_us/data_inspect1.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

# Penamaan/Pelabelan
 
Kolom `2004-05` sampai `2015-16` bisa disederhanakan menjadi `2004`, `2005`, `2006`, ..., `2015`, dan memang akan labih logis dan lebih baik seperti ini karena setiap kolom akan merepresentasikan hasil agregasi per satu tahun. Data di setiap sel (cell) merupakan hasil agregasi sehingga ini tidak perlu direpresentasikan sebagai `2005-06` (atau seterusnya), bisa direpresentasikan sebagai `2005` saja supaya lebih ringkas dan komputer bisa merekognisi angka ini sebagai tahun dengan lebih lancar ketimbang `2005-06`.

Di sini, saya menggunakan teknik "Autofill" ke kanan untuk mengubah kolom tahun.

1. Ubah `2004-05` menjadi `2004`
2. Ubah `2005-06` menjadi `2005`
3. Autofill ke kanan sampai `2015-16`

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/biaya_ukt_negara_bagian_us/data_transform1.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

# Tipe Data
 
Semua sel di kolom `B` sampai `M` (kecuali sel `B2`) memiliki format tipe data "Custom" (bawaan dari sumber file). Saya mengubah format sel B2 menjadi _Accounting_ untuk melihat apakah ada perubahan data. Biasanya notasi untuk _big mark_ atau kelipatan ribuan selalu berbeda dari satu tempat ke tempat lain. Sebagian orang ada yang menggunakan `.` tapi sebagian ada yang menggunakan `,` untuk memisahkan kelipatan ribuan. Dalam konteks kali ini, sel `B2` terlihat berbeda namun nilai aslinya tidak berubah (lihat Formula Bar).

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/biaya_ukt_negara_bagian_us/custom_data_type1.png" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/biaya_ukt_negara_bagian_us/custom_data_type2.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Data dengan tipe "Custom" (kiri) dan data dengan tipe "Accounting" (kanan) tidak ada perubahan pada nilai asli di Formula Bar.
</div>

Saya akan membiarkan data apa adanya, perubahan ke tipe data "Accounting" saya kembalikan ke "Custom" menggunakan "Undo".

# Summary Statistics

Tidak terdeteksi adanya nilai ekstrim dalam dataset ini. Saya lanjutkan ke tahap nomor 5.

# Visualisasi
 
Line chart akan sangat berguna untuk melihat tren yang muncul.

Pada tahap ini, saya membuat Line chart untuk melihat apakah ada tren unik yang muncul.

1. _Select_ semua kolom dan baris yang memiliki data.
2. Insert -> Chart -> Line -> 2-D Line.
3. Pada Line chart yang muncul, klik kanan lalu pilih `Select Data`.
4. Pilih `Switch Row/Column`.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/biaya_ukt_negara_bagian_us/data_viz_switch_rowcol.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

5. Perpanjang (vertikal) Line chart untuk visibilitas lebih baik.
6. Identifikasi tren secara visual.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/biaya_ukt_negara_bagian_us/visualization.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Kurang lebih ada 2 negara bagian Amerika Serikat dengan tren yang cenderung rata atau menaik sedikit.
</div>

# Validasi

Menggunakan statistika untuk memvalidasi temuan visual.

Saya membuat kolom baru bernama `korelasi` di samping kanan kolom `2015`. Setelah itu, saya menggunakan fungsi _correlation_ untuk melihat korelasi dan perubahan biaya UKT seiring berjalannya waktu.

```excel
=CORREL(B2:M2;$B$1:$M$1)
```

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/biaya_ukt_negara_bagian_us/validation_correl.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Argumen kedua menggunakan simbol `$` untuk mempatenkan lokasi sel sehingga tidak ikut berubah ketika melakukan Autofill ke bawah.
</div>

Setelah itu, saya menggunakan "Autofill" secara vertikal ke bawah untuk mempersingkat dan menyederhanakan proses kalkulasi.

Di kolom `N`, gunakan _Conditional Formatting_ lalu pilih Color Scale untuk mwengidentifikasi mana yang negatif, stagnan, atau positif. Spesifiknya, saya menggunakan Red-Yellow-Green Color Scale lalu mengambil keputusan berdasarkan warna. Pada kasus ini, saya tertarik pada kemunculan warna hijau (Green) karena ini menunjukkan pergerakan yang cenderung stagnan, dan ini merupakan sesuatu yang unik relatif dengan group negara bagian AS yang lain.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/biaya_ukt_negara_bagian_us/correlation.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Terdeteksi dua negara bagian AS yang cenderung stagnan.
</div>

> ##### **Tips**
> 
> Untuk mempermudah dan mempercepat proses identifikasi, bisa juga menggunakan _Filter_ pada kolom `korelasi` dan urutkan dari yang terkecil ke terbesar (_Sort A -> Z_ atau _Sort Smallest to Largest_).
{: .block-tip}

# Verifikasi
 
Periksa kembali seluruh alur yang telah dikerjakan. Pastikan tidak ada kesalahan atau miskalkulasi.

# Interpretasi

Tahap `Interpretasi` adalah tahap yang sangat bergantung pada audiens. Jika kita ingin memberikan _insight_ ini untuk calon mahasiswa, maka kita pandu audiens kita menggunakan narasi yang dilengkapi data hasil analisis. Jika audiens kita adalah pejabat negara atau pejabat pemerintah, maka kita harus mengubah dan menyesuaikan narasinya. Tentu kita tidak bisa membahas "negara bagian mana yang paling _worth it_ untuk kita lamar" jika audiens nya pejabat negara. Mereka tidak memiliki kepentingan untuk berkuliah. Akan tetapi, jika kita buat narasinya sedemikian rupa sehingga selaras dan sejalan dengan apa yang audiens inginkan, misal tentang pertumbuhan ekonomi atau GDP (_Gross Domestic Product_) sedang audiens kita pejabat pemerintah, maka hasil analisis kita akan lebih bermanfaat.

Singkatnya, interpretasi bisa berbeda-beda tergantung dari siapa audiens kita.
