---
layout: distill
title: "Work Log: Internet Labkom Sekolah Tidak Konek"
description: Kedua lab komputer di sekolah tiba tiba tidak bisa terhubung ke internet, indikator warning kuning
tags: [Network Infrastructure, Router, IT Support, Bahasa Indonesia]
categories: [Work]
date: 2026-04-15
authors:
  - name: Zelvy Fauzan
    affiliations:
     name: SMPN 1 Jalaksana
featured: false
mermaid:
  enabled: true
  zoomable: true
toc:
  - name: Keluhan
  - name: Investigasi
    subsections:
      - name: Pengecekan koneksi di jaringan lokal
      - name: Pengecekan koneksi ke jaringan luar
  - name: Hipotesis
  - name: Solusi
  - name: Saran
---

## Keluhan

| Waktu | User | Event |
| :---- | :---- | :---- |
| 2026-04-15 10:43:00 +07 | Guru Informatika senior | Internet tidak jalan di kedua lab komputer |


## Investigasi

Untuk mengidentifikasi sumber masalah, saya melakukan pengecekan koneksi ke jaringan lokal lalu luar:

### Pengecekan koneksi di jaringan lokal

Saya menggunakan (1) komputer guru yang ada di bagian depan ruang lab, (2) komputer siswa (terdekat dengan komputer guru), dan (3) HP pribadi saya yang terhubung dengan jaringan di lab komputer.

<aside>
  {% include figure.liquid loading="eager" path="assets/img/network_trouble_sekolah/ping_test_local_labkom.png" class="img-fluid rounded z-depth-1" zoomable=true %}
  <p>
  Ping ke router lokal menggunakan Termux di HP Android.
  </p>
</aside>

Saya menggunakan command berikut di kedua komputer dan HP saya (Termux)

```terminal
ping 192.168.123.254
```

Semua koneksi terlihat aman, tidak ada kendala.

Indikator: `<1 ms`

### Pengecekan koneksi ke jaringan luar

Kemudian saya coba melakukan tes koneksi ke jaringan luar menggunakan perintah berikut:

```terminal
ping 8.8.8.8
```
<aside>
  {% include figure.liquid loading="eager" path="assets/img/network_trouble_sekolah/ping_test_outside_labkom.png" class="img-fluid rounded z-depth-1" zoomable=true %}
  <p>
  Ping ke 8.8.8.8 menggunakan Termux di HP Android.</p>
</aside>

**Hasil:** `Tidak Aman`

Lalu saya coba menjalankan perintah `tracert` di komputer guru dan siswa di lab komputer untuk melakukan pelacakan `packet transmission`

```terminal
tracert 8.8.8.8
```
Kedua komputer yang saya tes menunjukkan tidak adanya koneksi keluar jaringan yang berhasil.

```terminal
1   *   *   *   *
2   *   *   *   *
3   *   *   *   *
...
```

Lalu saya cek koneksi internet di beberapa lokasi.

1. Pengecekan internet di ruang guru: `Aman`
2. Pengecekan internet di ruang auditorium: `Aman`
3. Pengecekan internet di ruang tata usaha: `Aman`

### Hipotesis

Router yang menjadi intermediasi (R1 pada diagram di bawah) antara jaringan lokal dan jaringan luar mendapat masalah.

```mermaid
flowchart LR
    ISP((ISP))
    E1[Listrik]
    R1[(R1)]
    R2[(R2)]
    R3[(R3)]
    R4[(R4)]
    R5[(R5)]
    R6[(R6)]
    R7[(R7)]
    Labkom1[Labkom 1]
    Labkom2[Labkom 2]
    RGuru[Ruang Guru]
    RAudit[Ruang Auditorium]
    RTU[Ruang Tata Usaha]

    R1 --- ISP
    R4 --- ISP
    R7 --- ISP
    E1 x--xR1
    R2-->R1
    R3-->R1
    R5-->R4
    R6-->R4
    Labkom1-->R2
    Labkom2-->R3
    RGuru-->R5
    RTU-->R6
    RAudit--->R7
```

## Solusi

Cek router intermediasi.

Bukti:
- Router intermediasi tidak menyala

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/network_trouble_sekolah/router_intermediari_sekolah.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

- Listrik mati

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/network_trouble_sekolah/listrik_sekolah.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
</div>


> ##### **Saran**
> 
> Cek router intermediasi apakah menyala atau tidak. Jika tidak menyala, cek status listrik yang ada di dekat koperasi sekolah.
{: .block-tip }