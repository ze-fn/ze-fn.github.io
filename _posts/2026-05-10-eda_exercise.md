---
layout: distill
title: "Latihan ADE: Analisis Jawaban Soal dan Proporsi Pengumpulan Tugas Siswa"
description: "Data Otentik dari SMP Negeri Kelas 8 di Daerah Jalaksana"
tags: [Statistics, Excel, Bahasa Indonesia]
categories: [Journal]
date: 2026-05-10
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
  - name: Demografi
  - name: Soal
  - name: Challenge
  - name: Challenge tambahan (opsional)
---

# Dataset
Dataset ini diambil dari 5 kelas Informatika yang saya ampu. Satu kelas berisikan 36 siswa dan kelima kelas ini adalah kelas 8 SMP. Data yang ada dalam dataset ini bisa digolongkan menjadi 2 grup: Demografi dan Soal. Namun semua kolom di 2 grup ini sudah menyatu dalam satu tabel sehingga tidak perlu menggabungkan tabel.

[Unduh dataset](https://ze-fn.github.io/assets/json/ad_dt1_exercise.csv)

## Demografi
Terdiri dari kolom yang berisikan informasi dasar siswa.

|   Kolom       |   Deskripsi                       |
| :------------ | :-------------------------------- |
| `local_id`    | Nomor Induk Siswa Sekolah         |
| `pres_num`    | Nomor urut absen                  |
| `gender`      | Jenis kelamin siswa               |
| `class`       | Grup kelas siswa (8F sampai 8J)   |

## Soal
Berisikan jawaban siswa untuk setiap soal. Opsi jawan ada 4: k (kontinyu), d (diskrit), n (nominal), dan o (ordinal). Cell dengan isian kosong berarti siswa tersebut tidak mengumpulkan tugas.

|   Kolom       |   Deskripsi           |
| :------------ | :-------------------- |
| `1`	        | Soal pertama 		    |
| `2`       	| Soal kedua 		    |
| `3`	        | Soal ketiga 		    |
| `4`       	| Soal keempat 		    |   	
| `5`	        | Soal kelima 		    |
| `6`	        | Soal keenam 		    |
| `7`	        | Soal ketujuh 		    |
| `8`	        | Soal kedelapan 	    |
| `9`	        | Soal kesembilan 	    |
| `10`	        | Soal kesepuluh 	    |
| `11`      	| Soal kesebelas 	    |
| `12`      	| Soal kedua belas 	    |
| `13`	        | Soal ketiga belas 	|
| `14`	        | Soal keempat belas 	|
| `15`	        | Soal kelima belas 	|

# Challenge
1. Buat bar/column chart untuk setiap soal lalu cari tahu jawaban paling banyak dipilih untuk setiap soal (berarti harus ada 10 chart untuk soal ini. Simpan chart di satu sheet, penamaan sheet bebas).
2. Buat bar/column chart tentang proporsi siswa berdasarkan gender yang mengumpulkan tugas.

## Challenge tambahan (opsional)
1. Terapkan Chi-squared test pada Challenge nomor 2 di atas, lalu buat kesimpulannya.