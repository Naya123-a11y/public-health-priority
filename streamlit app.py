# Public Health Priority Engine

## Deskripsi
Public Health Priority Engine adalah aplikasi berbasis Python dan Streamlit untuk membantu menentukan prioritas intervensi kesehatan masyarakat pada tingkat desa.

Aplikasi ini menggunakan beberapa indikator kesehatan masyarakat, yaitu:

- Prevalensi stunting (%)
- Cakupan imunisasi lengkap (%)
- Kasus DBD tahunan
- Akses air bersih (%)
- Sanitasi layak (%)
- Persentase kemiskinan (%)

Output yang dihasilkan berupa:

- Ranking desa prioritas
- Skor prioritas intervensi
- Visualisasi grafik
- File hasil yang dapat diunduh

---

## Struktur Folder

```text
PublicHealthWeb/
│
├── app.py
├── requirements.txt
├── README.md
└── Public_Health_Priority_25_Desa.xlsx
```

---

## Instalasi

Install seluruh library yang dibutuhkan:

```bash
pip install -r requirements.txt
```

atau

```bash
pip install streamlit pandas openpyxl matplotlib
```

---

## Menjalankan Aplikasi

Jalankan perintah berikut:

```bash
streamlit run app.py
```

Kemudian buka browser pada alamat:

```text
http://localhost:8501
```

---

## Cara Menggunakan

1. Jalankan aplikasi.
2. Upload file Excel dengan format yang sesuai.
3. Klik tombol **Analisis**.
4. Sistem akan menghasilkan:
   - Ranking prioritas desa
   - Grafik prioritas
   - File hasil yang dapat diunduh

---

## Metode Analisis

Aplikasi menggunakan metode:

- Simple Additive Weighting (SAW)

dengan pendekatan:

### Benefit Criteria
Semakin tinggi nilainya semakin baik:

- Imunisasi
- Air Bersih
- Sanitasi

### Cost Criteria
Semakin tinggi nilainya semakin membutuhkan intervensi:

- Stunting
- DBD
- Kemiskinan

---

## Teknologi yang Digunakan

- Python
- Pandas
- Matplotlib
- Streamlit
- OpenPyXL

---

## Pengembang

Nama: Neha Dyana Angelyta  
Program Studi: S1 Farmasi  
Universitas Islam Indonesia

---

## Lisensi

Proyek ini bersifat open-source dan dapat digunakan untuk tujuan pendidikan dan penelitian.