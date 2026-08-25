---
layout: distill
title: "Work Log: Teknisi Komputer untuk TKA 2026"
description: Catatan dan pengalaman kerja saat menjadi teknisi komputer di program TKA 2026
tags: [TKA 2026, System Administration, IT Support, BIOS, Exam Browser, Bahasa Indonesia]
categories: [Work]
date: 2026-03-9
authors:
  - name: Zelvy Fauzan
    affiliations:
     name: SMPN 1 Jalaksana
featured: false
mermaid:
  enabled: true
  zoomable: true
toc:
  - name: Tugas dan Tanggung Jawab Teknisi Komputer di Program TKA 2026
    subsections: 
    - name: Tugas Teknisi Komputer
    - name: Tanggung Jawab Teknisi Komputer
  - name: Temuan Kasus
  - name: Lesson Learned
---

## Program Tes Kemampuan Akademik (TKA) 2026

Kementerian Pendidikan Dasar dan Menengah (Kemendikdasmen) Indonesia mencetuskan program TKA untuk mendiagnosis kemampuan akademik siswa di Indonesia. Selain diagnosa, nilai yang didapat juga bisa dijadikan "tiket masuk" untuk mendaftar ke jenjang pendidikan selanjutnya. Walau begitu, TKA ini bersifat opsional sehingga satuan pendidikan boleh ikut serta atau tidak.

Dalam pelaksanaannya, TKA dibagi menjadi 3 moda:

1. Daring
2. Semi-daring
3. Luring

SMPN 1 Jalaksana, tempat saya bekerja pada saat tulisan ini dibuat, memilih untuk ikut serta dalam TKA moda daring. Oleh karena itu, sekolah membutuhkan Teknisi Komputer untuk memastikan kesuksesan berjalannya TKA ini. Karena di SMPN 1 Jalaksana kekurangan tenaga ahli atau guru di bidang teknisi komputer, Ketua Pelaksana TKA dan guru Informatika senior di sekolah merekomendasikan saya untuk peran Teknisi Komputer.

## Tugas dan Tanggung Jawab

Tugas Teknisi Komputer yang diberikan bisa dirangkum menjadi satu kalimat:

> Menyiapkan infrastruktur IT yang andal dan memberikan dukungan teknis responsif demi kelancaran ujian bagi seluruh siswa kelas 9 di setiap sesi.

Disamping itu, Teknisi Komputer juga memiliki tanggung jawab untuk:

1. Memeriksa dan memastikan seluruh unit komputer yang ada di lab komputer layak pakai.
2. Instalasi perangkat lunak (software) Exam Browser versi 2026 di setiap unit komputer yang ada.
3. Memeriksa dan memastikan stabilitas koneksi jaringan setiap klien ke router lokal masing-masing lab komputer.
4. Melakukan tindakan perbaikan atau menyiapkan unit cadangan secara cepat jika terjadi gangguan teknis sebelum maupun saat ujian berlangsung.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/tka2026/qc_komputer.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

## Temuan Kasus

### 1. Koneksi Internet Terputus

**Kendala:** Salah satu unit komputer sering terputus koneksi internet.

**Dampak:** Siswa tidak bisa melanjutkan sesi TKA.

**Hipotesis:** Kabel yang longgar.

**Solusi Temporer:** Mengubah posisi kabel LAN.

> ##### **SOLUSI PERMANEN**
> 
> Mengganti atau memperkuat konektor RJ45 ke socket.
{: .block-tip }

---

### 2. Keyboard Tidak Berfungsi

**Kendala:** Setiap siswa melakukan logout session dan pergantian sesi selanjutnya, separuh dari total unit komputer menjadi tidak bisa menginput tuts sama sekali.

**Dampak:** Siswa tidak bisa menginput data kredensial ketika login.

**Hipotesis:** Kabel longgar.

**Solusi Yang Ditawarkan:** Mengganti keyboard saat ini dengan keyboard cadangan.

**Investigasi:** 

- Mengganti dengan keyboard cadangan: `Persisten`
- Mencoba *hotkey* `CTRL` + `C` + `B` untuk keluar dari Exam Browser: `Berhasil`
- Kendala tetap selalu muncul kembali setiap pergantian sesi
- Saya menemukan bahwa menekan tombol `CTRL` saja bisa mengembalikan fungsi keyboard secara utuh.

> ##### **SOLUSI TEPAT**
> 
> Tekan `CTRL` pada keyboard.
{: .block-tip }

> ##### **SARAN**
> 
> **Untuk Pengembang Software:** 
> 
> Perbaiki *rules* konfigurasi hotkey supaya tidak "mematikan" fungsi keyboard ketika menekan hotkey tertentu.
{: .block-warning }

---

### 3. Komputer Mati Tiba-tiba

**Kendala:** Satu unit komputer selalu mati setelah beberapa waktu digunakan. Terdengar suara seperti listrik konslet dari kabel PSU. Terjadi di setiap sesi pada hari pertama dan kedua pelaksanaan TKA.

**Dampak:** Progres siswa terhambat, sisa waktu mengerjakan terbuang.

**Hipotesis:** Kabel PSU longgar.

**Investigasi:** 

- Mengganti kabel PSU: `Persisten`
- Mengecek ulang perangkat keras (RAM, CPU, PSU): `Persisten`
- Mengecek suhu komputer menggunakan HWMonitor: `Indikasi overheat`
- Mengecek CPU Fan: `Tidak nyala`

> ##### **SOLUSI**
> 
> Mengganti CPU Fan dengan cadangan.
{: .block-tip }

---

### 4. Boot up dari Network

**Kendala:** Komputer sama sekali tidak bisa *boot up* ke Windows.

**Dampak:** Siswa yang bisa mengerjakan TKA berkurang 1. 

**Hipotesis:** Primary boot order tertukar antara Network dan Storage.

**Investigasi:** 

- Restart komputer
- Masuk ke BIOS
- Cek menu Startup/Boot
- Primary Boot Order 1 = Network

> ##### **SOLUSI**
> 
> Mengganti Primary Boot urutan pertama menjadi `Storage` 
> 
> Exclude opsi Network dari Boot Order
> 
{: .block-tip }

---

### 5. Date and Time Komputer

**Kendala:** Date and Time dari 6 unit komputer (total 24) selalu kembali ke 2007, 2008, atau 2010 setiap mesin dimatikan atau di-restart.

**Hipotesis:** Baterai CMOS habis

**Solusi Temporer:** Mengubah Date and Time sesuai dengan tanggal saat ini.

### 6. Server Error

**Kendala:** Dalam interval acak, unit komputer mengalami eror koneksi ke server pusat TKA.

**Dampak:** Siswa tidak bisa lanjut mengerjakan TKA.

**Foto:**
<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/tka2026/server_error.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

**Hipotesis:** Server pusat tidak kuat menampung *request* yang sangat banyak.

> **SOLUSI**
> 
> `CTRL` + `C` + `B` (keluar aplikasi), lalu jalankan kembali.
{: .block-tip }

## Lesson Learned

Dari semua kasus yang saya temui dan alami pada saat persiapan maupun pelaksanaan TKA 2026, saya bersyukur dapat menuntaskan tugas saya sebagai Teknisi Komputer. Walau begitu, saya merasa kinerja saya sebagai teknisi komputer bisa ditingkatkan lebih tinggi lagi. Yang terbesit di dalam benak saya adalah: cara memperbaiki kabel LAN yang longgar (atau terputus) sehingga jaringan bisa normal kembali.

## Rencana Peningkatan Kinerja

Saya akan mempelajari teknik jaringan komputer (praktikal) dasar dan lanjutan. Pada saat saya menulis blog ini, saya memikirkan cara menggunakan Network Crimping, Cable Tester, dan lain-lain. 