import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Public Health Priority Dashboard",
    layout="wide"
)

st.title("🏥 Public Health Priority Dashboard")

st.write("""
Upload hasil analisis TOPSIS untuk ditampilkan
dalam bentuk dashboard interaktif.
""")

# ==========================================
# Upload file
# ==========================================

ranking_file = st.file_uploader(
    "Upload Hasil_Ranking_TOPSIS.xlsx",
    type=["xlsx"]
)

ranking_png = st.file_uploader(
    "Upload Ranking_TOPSIS.png",
    type=["png"]
)

heatmap_png = st.file_uploader(
    "Upload Heatmap.png",
    type=["png"]
)

pie_png = st.file_uploader(
    "Upload Pie_Kategori.png",
    type=["png"]
)

dashboard_png = st.file_uploader(
    "Upload Dashboard.png",
    type=["png"]
)

laporan_docx = st.file_uploader(
    "Upload Laporan_Hasil.docx",
    type=["docx"]
)

# ==========================================
# Ranking Excel
# ==========================================

if ranking_file:

    st.header("📊 Ranking Prioritas Desa")

    df = pd.read_excel(ranking_file)

    st.dataframe(
        df,
        use_container_width=True
    )

    st.metric(
        "Jumlah Desa",
        len(df)
    )

    st.metric(
        "Desa Prioritas Utama",
        df.iloc[0]["Desa"]
    )

# ==========================================
# Ranking Chart
# ==========================================

if ranking_png:

    st.header("📈 Ranking TOPSIS")

    st.image(
        ranking_png,
        use_container_width=True
    )

# ==========================================
# Heatmap
# ==========================================

if heatmap_png:

    st.header("🔥 Heatmap Korelasi")

    st.image(
        heatmap_png,
        use_container_width=True
    )

# ==========================================
# Pie Chart
# ==========================================

if pie_png:

    st.header("🥧 Distribusi Risiko")

    st.image(
        pie_png,
        use_container_width=True
    )

# ==========================================
# Dashboard Summary
# ==========================================

if dashboard_png:

    st.header("📋 Dashboard Keseluruhan")

    st.image(
        dashboard_png,
        use_container_width=True
    )

# ==========================================
# Download Laporan
# ==========================================

if laporan_docx:

    st.header("📄 Laporan")

    st.download_button(
        label="Download Laporan DOCX",
        data=laporan_docx,
        file_name="Laporan_Hasil.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
