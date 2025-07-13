import streamlit as st
import webbrowser

# Data senyawa organik (hanya Ethanol)
compounds = {
    "Ethanol": {
        "titik_didih": "78.37 °C",
        "titik_leleh": "-114.1 °C",
        "kepolaran": "Polar",
        "rumus_kimia": "C2H5OH",
        "fun_fact": "Ethanol is the type of alcohol found in alcoholic beverages.",
        "ikatan_kimia": "Terdapat ikatan tunggal C-C dan C-O.",
        "link_youtube": "https://www.youtube.com/watch?v=3g1g1g1g1g1",
        "detail_page": "https://ethanoldetail.streamlit.app"  # URL untuk tab baru
    }
}

def show_home():
    st.set_page_config(page_title="O-Kimiaku", page_icon="🧪", layout="centered")
    
    # Logo dan judul minimalis
    st.image("https://placehold.co/200x100?text=O-Kimiaku", width=200)
    st.title("Explorer Senyawa Organik")
    
    # Card Ethanol saja
    with st.container(border=True):
        st.subheader("Ethanol")
        st.write(f"**Rumus Kimia:** {compounds['Ethanol']['rumus_kimia']}")
        st.write(f"**Titik Didih:** {compounds['Ethanol']['titik_didih']}")
        
        # Tombol yang akan membuka tab baru
        if st.button("Lihat Detail Ethanol", type="primary"):
            webbrowser.open_new_tab(compounds['Ethanol']['detail_page'])

def show_compound_detail():
    # Halaman detail yang terpisah (diakses via URL berbeda)
    st.set_page_config(page_title="Detail Ethanol", page_icon="🧪")
    
    st.title("Detail Ethanol")
    compound_info = compounds["Ethanol"]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://placehold.co/400x300?text=Struktur+Ethanol")
    
    with col2:
        st.write("**Titik Didih:**", compound_info["titik_didih"])
        st.write("**Titik Leleh:**", compound_info["titik_leleh"])
        st.write("**Kepolaran:**", compound_info["kepolaran"])
        st.write("**Rumus Kimia:**", compound_info["rumus_kimia"])
        st.write("**Fun Fact:**", compound_info["fun_fact"])
        st.write("**Ikatan Kimia:**", compound_info["ikatan_kimia"])
        
        if st.button("Tonton Video Penjelasan"):
            webbrowser.open_new_tab(compound_info["link_youtube"])

# Panggil fungsi berdasarkan URL
if "detail" in st.query_params:
    show_compound_detail()
else:
    show_home()
