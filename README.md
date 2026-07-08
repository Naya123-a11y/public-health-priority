# 🏥 Public Health Priority Engine

## Deskripsi
Public Health Priority Engine adalah aplikasi berbasis Python dan Streamlit untuk membantu menentukan prioritas intervensi kesehatan masyarakat pada tingkat desa menggunakan metode TOPSIS (Technique for Order Preference by Similarity to Ideal Solution).

Aplikasi ini dapat membantu Puskesmas, Dinas Kesehatan, maupun peneliti dalam menentukan desa yang memerlukan intervensi kesehatan lebih dahulu berdasarkan beberapa indikator kesehatan masyarakat.

---

## Indikator yang Digunakan

- Prevalensi Stunting (%)
- Cakupan Imunisasi Lengkap (%)
- Jumlah Kasus DBD Tahunan
- Akses Air Bersih (%)
- Sanitasi Layak (%)
- Tingkat Kemiskinan (%)

---

## Fitur

✅ Upload file Excel  
✅ Analisis otomatis menggunakan metode TOPSIS  
✅ Ranking prioritas desa  
✅ Heatmap korelasi indikator  
✅ Visualisasi kategori risiko  
✅ Download hasil analisis Excel  
✅ Download laporan Word otomatis  

---

## Struktur File Excel

File Excel harus memiliki sheet:

```text
Data_25_Desa
```

Dengan kolom:

```text
Desa
Stunting_%
Imunisasi_Lengkap_%
Kasus_DBD_Tahunan
Akses_Air_Bersih_%
Sanitasi_Layak_%
Kemiskinan_%
```

Contoh:

| Desa | Stunting_% | Imunisasi_Lengkap_% | Kasus_DBD_Tahunan | Akses_Air_Bersih_% | Sanitasi_Layak_% | Kemiskinan_% |
|------|------------|---------------------|-------------------|--------------------|------------------|-------------|
| Desa A | 32 | 78 | 15 | 65 | 70 | 25 |
| Desa B | 18 | 92 | 4 | 88 | 90 | 10 |

---

## Teknologi yang Digunakan

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- OpenPyXL
- Python-Docx

---

## Cara Menjalankan Secara Lokal

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Deploy Online

Aplikasi dapat dipublikasikan menggunakan:

- GitHub
- Streamlit Community Cloud

---

## Pengembang

Nafidhatul Afina & Neha Dyana Angelyta  
Program Studi Magister Farmasi  
Universitas Islam Indonesia

---

## Lisensi

Proyek ini dibuat untuk tujuan pendidikan, penelitian, dan pengembangan sistem pendukung keputusan di bidang kesehatan masyarakat.
