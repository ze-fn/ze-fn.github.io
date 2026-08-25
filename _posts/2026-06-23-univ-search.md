---
layout: distill
title: Rekomendasi Jurusan Fisika Terapan
description: Penerapan OSINT dan Data Analysis
tags: [OSINT, Data Analysis]
categories: [Portfolio]
date: 2026-06-23
featured: false
mermaid:
  enabled: true
toc:
  - name: Pendahuluan
  - name: Metodologi
  - name: Step 1. OSINT Gathering Peringkat Universitas
  - name: Step 2. OSINT Gathering Daftar Program Studi
  - name: Step 3. OSINT Gathering Daftar Dosen
  - name: Hasil Analisis
giscus_comments: true
authors:
  - name: Zelvy Fauzan
    url: https://ze-fn.github.io/
    affiliations:
      name: Independent
      url: https://github.com/ze-fn/
pretty_table: true
---

# Pendahuluan

Berawal dari obrolan ringan melalui aplikasi pesan instan, teman saya bertanya tentang rekomendasi jurusan dan/atau universitas yang cocok untuknya. Teman saya berlatar belakang Fisika dan sekarang berniat untuk belajar kembali untuk nantinya menjadi peneliti di bidang yang ia minati. Sebagai catatan, teman saya ingin bergelut spesifik di bidang Fisika Terapan, sub bidang energi hibrida atau energi alternatif.

Dari situ, saya mencoba untuk membantu teman saya mencarikan informasi dan memberikan rekomendasi jurusan dan universitas untuknya.

## Problem Statement

> Jurusan di universitas dalam negeri (Indonesia) mana yang paling bagus untuk jurusan Fisika Terapan dengan konsentrasi Energi Hibrida dan/atau Energi Alternatif?

# Metodologi

Untuk menyelesaikan permasalahan ini, saya pikir penting sifatnya mendefinisikan variabel tolak ukur. Namun begitu, mengingat permintaan ini terbatas waktu, saya memilih untuk mempercayai satu sumber data yang fokus dalam perangkingan universitas. Untuk evaluasi lanjutan, dalam hal ini menentukan kualitas jurusan, saya menggunakan teknik OSINT (Open Source Intelligence) untuk mendapat infomrasi publik mengenai dosen/promotor dengan minat penelitian yang serupa dengan minat teman saya.

## Desain Database

Mengingat target teman saya yang ingin menjadi seorang peneliti yang terjun ke lapangan, dengan fokus tema penelitian Fisika Terapan, saya melakukan investigasi dengan fokus ke informasi dosen yang ada di tiap universitas dengan kriteria yang sesuai.

### Universitas

| Variabel  | Deskripsi |
| :-------- | :-------- |
| id        | Nomor identifikasi unik universitas |
| nama_univ | Nama universitas |
| rank_2025 | Peringkat universitas pada tahun 2025 |
| rank_2026 | Peringkat universitas pada tahun 2026 |
| country   | Negara dimana universitas berada |
| cpf_score | Sitasi per Fakultas |

### Fakultas

| Variabel  | Deskripsi |
| :-------  | :-------- |
| univ_id   | Nomor identifikasi unik universitas |
| fakult_id | Nomor identifikasi unik fakultas |
| nama_fa   | Nama fakultas |

### Dosen

| Variabel      | Deskripsi |
| :------------ | :-------- |
| dosen_id      | Nomor identifikasi unik dosen |
| nama_dosen    | Nama dosen |
| fakult_id     | Nomor identifikasi unik fakultas |
| minat_ris     | Minat bidang penelitian dosen |
| n_artikel     | Jumlah artikel terpublikasi oleh dosen |
| n_fauthor     | Jumlah artikel dosen sebagai penulis pertama |
| n_sauthor     | Jumlah artikel dosen sebagai penulis kedua |
| n_tauthor     | Jumlah artikel dosen sebagai penulis ketiga |


# Step 1. OSINT Gathering Peringkat Universitas

Search query:

``` text
world university rankings after:2026-01-01
```

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="/assets/img/univ-search/osint-gathering-11.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Gambar 1. Hasil pencarian peringkat universitas tingkat dunia pada tahun 2026.
</div>

Data peringkat universitas di tingkat dunia bisa diunduh.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/univ-search/osint-gathering-12.png" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/univ-search/osint-gathering-13.png" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
<div class="caption">
    Universitas top 3 dunia dan tautan daftar lengkap peringkat (gambar kiri) dan dataset lengkap (gambar kanan).
</div>

Saya menemukan ada banyak metrik di dalam dataset yang didapat namun hanya beberapa variabel yang akan saya gunakan dalam tahap analisis. Saya sajikan dalam format tabel berikut:

| Asal                  | Transformasi      |
| :-------------------- | :---------------- |
| `Rank`                | `rank_2026`       |
| `Previous Rank`       | `rank_2025`       |
| `Name`                | `nama_univ`       |
| `Country/Territory`   | `negara`          |
| `CPF Score`           | `cpf_score`       |

# Step 2. OSINT Gathering Daftar Program Studi

Search query:

``` text
pddikti kemdiktisaintek universitas fakultas
```

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="/assets/img/univ-search/osint-gathering-21.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Pada laman PDDIKTI, saya melakukan pencarian nama universitas yang masuk dalam daftar peringkat dunia. Karena setiap pencarian di laman ini diproteksi oleh captcha, saya melakukan pencarian satu demi satu untuk setiap universitas.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/univ-search/osint-gathering-22.png" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/univ-search/osint-gathering-23.png" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>

Ketika query pencarian berdasarkan nama universitas di PDDIKTI muncul, saya scroll ke bawah hingga menemukan bagian daftar universitas lalu melihat rincian dari universitas yang sedang dicari. Di dalamnya, saya menemukan daftar lengkap program studi dalam format tabel. Tabel ini kemudian saya salin dan tempel di file Google Sheets.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="/assets/img/univ-search/osint-gathering-24.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

> Data yang saya ambil bisa diakses secara publik [di sini](https://docs.google.com/spreadsheets/d/1qkrFVZ655DB2WeDLcIiM_aIh5lWyF801gOGDhDMWnd0/)

# Step 3. OSINT Gathering Daftar Dosen

Mengingat minat teman saya yang ingin menjadi peneliti lapangan di bidang Teknik Fisika yang berkaitan dengan Energi Hibrida, Alternatif, dan/atau Terbarukan, saya melakukan filtering kembali di laman PDDIKTI.

``` text
ITB Fisika
```

Setalah itu, saya mengulik rincian dari Program Studi terkait dengan catatan nama program studi harus berkaitan dengan "Fisika", jenjang S2 atau S3, dan nama lembaga sesuai dengan nama universitas yang ada pada search query. Di dalam tautan "Lihat Detail" pada kolom Aksi yang ada pada hasil pencarian PDDIKTI, ada daftar Tenaga Pendidik (Dosen). Data ini lah yang saya ambil untuk pencarian lebih lanjut di langkah selanjutnya (Step 4) tentang Kepakaran Dosen.

Minat teman saya dan Kepakaran Dosen penting untuk dipertimbangkan karena akan sangat berpengaruh dengan pengalaman dan karir kedepannya.

Data dosen yang memenuhi kriteria filterisasi bisa diakses secara publik di file Google Sheets yang sama dengan Step 2. [Cek disini](https://docs.google.com/spreadsheets/d/1qkrFVZ655DB2WeDLcIiM_aIh5lWyF801gOGDhDMWnd0/).

# Hasil Analisis

Setelah semua data terkumpul, saya lanjut melakukan analisis. Analisis yang dipakai tidaklah sulit, bahkan bisa dibilang sangat mudah dan sederhana. Saya menggunakan inclusion dan exclusion dengan batas ambang untuk variabel-variabel tertentu. 

Pertama, saya melihat dari level universitas terlebih dahulu. Aturan yang saya terapkan pada level ini adalah peringkat universitas sedunia.

1. `rank_2026` <= 500
2. `rank_2026` ORDER Z -> A
3. `cpf_score` ORDER Z -> A
4. Ambil baris 1 sampai 3

> Hasil: `ITB`, `UI`, dan `UGM`

Kemudian, saya melakukan filter di level program studi.

1. `universitas` = {ITB, UI, UGM}
2. `jenjang` = {S2, S2 Terapan, S3}
3. `akreditasi` = {A, Unggul}
4. `status` = Aktif
5. `nama_prodi` != Pengajaran
6. `nama_prodi` = {Fisika, Energi, Teknik Fisika}

Hasil: 

1. ITB:
    - `S2 Teknik Fisika`
    - `S3 Teknik Fisika`
    - S2 Fisika
    - S3 Fisika
2. UI:
    - `S2 Teknik Sistem Energi`
    - S2 Ilmu Fisika
    - S2 Fisika
    - S3 Fisika
3. UGM:
    - S2 Teknik Fisika
    - S3 Fisika
    - S2 Fisika