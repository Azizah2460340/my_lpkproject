import streamlit as st
from PIL import Image
import time

# Konfigurasi halaman
st.set_page_config(
    page_title="O-Kimiaku",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)
    
# ------------- FUNGSI --------------
def show_home():
    st.title("Selamat Datang di O-KimiaKu 👩‍🔬🧪")

    st.markdown("""
    **O-KimiaKu** adalah aplikasi pembelajaran interaktif kimia yang memberikan informasi penting tentang senyawa kimia, seperti:
    - ✅ Tatanama Senyawa
    - 🌡️ Titik Didih dan Titik Leleh
    - 🤓 Fun Fact Kimia
    - ⚖️ Kepolaran
    - 🧬 Rumus Kimia

    Klik gambar senyawa untuk mengetahui detailnya lebih lanjut!
    """)

    st.subheader("🔍 Pilih Senyawa:")

    cols = st.columns(5)
    with cols[0]:
         if st.button("🍷 Alkohol"):
            st.session_state.page = 'alkohol'
         if st.button("🕸️ Benzena"):
            st.session_state.page = 'benzena'
         if st.button("🌿 Fenol"):
            st.session_state.page = 'fenol'
         if st.button("🧪 Amina"):
            st.session_state.page = 'amina'
    with cols[1]:
         if st.button("🔬 Amida"):
            st.session_state.page = 'amida'
         if st.button("🧫 Aldehida"):
            st.session_state.page = 'aldehida'
         if st.button("⚡ Nitro"):
            st.session_state.page = 'nitro'
         if st.button("🧭 Nitril"):
            st.session_state.page = 'nitril'
    with cols[2]:
         if st.button("🧬 Alkana"):
            st.session_state.page = 'alkana'
         if st.button("🌱 Alkena"):
            st.session_state.page = 'alkena'
         if st.button("🔥 Alkuna"):
            st.session_state.page = 'alkuna'
         if st.button("🍞 Karbohidrat"):
            st.session_state.page = 'karbohidrat'
    with cols[3]:
         if st.button("🎯 Keton"):
            st.session_state.page = 'keton'
         if st.button("🧴 Ester"):
            st.session_state.page = 'ester'
         if st.button("💧 Eter"):
            st.session_state.page = 'eter'
         if st.button("🍗 Protein"):
            st.session_state.page = 'protein'
    with cols[4]:
         if st.button("🧂 Asam Halida"):
            st.session_state.page = 'asam_halida'
         if st.button("🍋 Asam Karboksilat"):
            st.session_state.page = 'asam_karboksilat'
         if st.button("🔌 Alkil Halida"):
            st.session_state.page = 'alkil_halida'
         if st.button("🛢️ Lemak dan Minyak"):
            st.session_state.page = 'lemak_dan_minyak'
import streamlit as st

def show_alkana():
    st.title("Detail Senyawa: Alkana")

    st.markdown("""
    **Deskripsi:** Alkana adalah senyawa hidrokarbon jenuh yang hanya mengandung ikatan tunggal (σ) antar atom karbon (C–C) dan antara karbon dengan hidrogen (C–H). Rumus umumnya adalah CₙH₂ₙ₊₂. Alkana termasuk senyawa nonpolar dan merupakan komponen utama dalam gas alam dan minyak bumi.

    **Titik Didih:**
    - Titik didih alkana meningkat seiring bertambahnya jumlah atom karbon.
    - Bentuk rantai lurus memiliki titik didih lebih tinggi dibanding bentuk bercabang.
    - Contoh:
        - Metana (CH₄): −161,5 °C
        - Etana (C₂H₆): −88,6 °C
        - Butana (C₄H₁₀): −0,5 °C

    **Kepolaran:** Nonpolar, tidak larut dalam air.

    **Ikatan Kimia:** Hanya memiliki ikatan tunggal kovalen (σ).

    **Tata Nama (IUPAC):** Berdasarkan jumlah atom karbon dan akhiran -ana.
    """)

def show_alkena():
    st.title("Detail Senyawa: Alkena")

    st.markdown("""
    **Deskripsi:** Alkena adalah senyawa hidrokarbon tak jenuh yang memiliki setidaknya satu ikatan rangkap dua (C=C) antar atom karbon. Rumus umumnya CₙH₂ₙ.

    **Titik Didih:**
    - Titik didih alkena meningkat seiring bertambahnya jumlah atom karbon.
    - Contoh:
        - Etena (C₂H₄): −103,7 °C
        - Propena (C₃H₆): −47,6 °C

    **Kepolaran:** Secara umum nonpolar, sedikit lebih polar dari alkana.

    **Ikatan Kimia:** Memiliki 1 ikatan sigma (σ) dan 1 ikatan pi (π).

    **Tata Nama (IUPAC):** Berdasarkan rantai terpanjang yang mengandung ikatan rangkap dua dan akhiran -ena.
    """)

def show_alkuna():
    st.title("Detail Senyawa: Alkuna")

    st.markdown("""
    **Deskripsi:** Alkuna adalah senyawa hidrokarbon tak jenuh yang memiliki setidaknya satu ikatan rangkap tiga (C≡C) antar atom karbon. Rumus umumnya CₙH₂ₙ₋₂.

    **Titik Didih:**
    - Titik didih alkuna meningkat seiring jumlah atom karbon.
    - Contoh:
        - Etuna (asetilena, C₂H₂): −84 °C
        - Butuna (C₄H₆): sekitar 0–4 °C

    **Kepolaran:** Sebagian besar alkuna adalah nonpolar.

    **Ikatan Kimia:** Memiliki 1 ikatan sigma (σ) dan 2 ikatan pi (π).

    **Tata Nama (IUPAC):** Berdasarkan rantai terpanjang yang mengandung ikatan rangkap tiga dan akhiran -una.
    """)

def show_alkohol():
    st.title("Detail Senyawa: Alkohol")

    st.markdown("""
    **Deskripsi:** Alkohol adalah senyawa organik yang memiliki gugus hidroksil (–OH) yang terikat pada atom karbon jenuh (sp³). Rumus umum: R–OH.

    **Titik Didih:**
    - Tinggi dibanding alkana/alkena/alkuna dengan jumlah karbon yang sama.
    - Contoh:
        - Metanol (CH₃OH): 64,7 °C
        - Etanol (CH₃CH₂OH): 78,4 °C
        - 1-Butanol: 117,7 °C

    **Kepolaran:** Polar, dapat larut dalam air.

    **Ikatan Kimia:** Gugus –OH terdiri dari ikatan kovalen polar O–H dan C–O.

    **Tata Nama (IUPAC):** Berdasarkan rantai utama yang mengandung gugus –OH dan akhiran -ol.
    """)

def show_fenol():
    st.title("Detail Senyawa: Fenol")

    st.markdown("""
    **Deskripsi:** Fenol (C₆H₅OH) adalah senyawa aromatik yang terdiri dari cincin benzena yang terikat pada gugus hidroksil (-OH).

    **Titik Didih:**
    - Titik didih fenol: 181,7 °C
    - Titik leleh: 40,9 °C

    **Kepolaran:** Polar, karena mengandung gugus hidroksil (-OH).

    **Ikatan Kimia:** Ikatan kovalen antara atom karbon dan hidrogen dalam cincin benzena.

    **Tata Nama (IUPAC):** Nama umum: Fenol, Nama IUPAC: Benzenol.
    """)

def show_aldehid():
    st.title("Detail Senyawa: Aldehid")

    st.markdown("""
    **Deskripsi:** Aldehid adalah senyawa organik yang memiliki gugus karbonil (C=O) di ujung rantai karbon, dengan rumus umum R–CHO.

    **Titik Didih:**
    - Titik didih lebih tinggi daripada alkana/eter, tapi lebih rendah dari alkohol.
    - Contoh:
        - Formaldehida (HCHO): −19 °C
        - Asetaldehida (CH₃CHO): 20,2 °C
        - Butanal: 75 °C

    **Kepolaran:** Sangat polar, larut dalam air.

    **Ikatan Kimia:** Gugus karbonil terdiri dari satu ikatan sigma (σ) dan satu ikatan pi (π).

    **Tata Nama (IUPAC):** Berdasarkan rantai utama yang mengandung gugus –CHO dan akhiran -al.
    """)

def show_keton():
    st.title("Detail Senyawa: Keton")

    st.markdown("""
    **Deskripsi:** Keton adalah senyawa organik yang memiliki gugus karbonil (C=O) di tengah rantai karbon, dengan rumus umum R–CO–R′.

    **Titik Didih:**
    - Titik didih lebih tinggi dari alkana/eter, tetapi lebih rendah dari alkohol.
    - Contoh:
        - Aseton (CH₃COCH₃): 56,5 °C
        - 2-Butanon (CH₃COCH₂CH₃): 79,6 °C

    **Kepolaran:** Polar, larut dalam air untuk rantai pendek.

    **Ikatan Kimia:** Gugus karbonil mengandung 1 ikatan sigma (σ) dan 1 ikatan pi (π).

    **Tata Nama (IUPAC):** Berdasarkan rantai utama yang mengandung gugus karbonil dan akhiran -on.
    """)

def show_amina():
    st.title("Detail Senyawa: Amina")

    st.markdown("""
    **Deskripsi:** Amina adalah senyawa organik turunan amonia (NH₃) di mana satu atau lebih atom hidrogen diganti dengan gugus alkil atau aril.

    **Titik Didih:**
    - Amina primer dan sekunder dapat membentuk ikatan hidrogen, sehingga titik didihnya lebih tinggi dari senyawa nonpolar.
    - Contoh:
        - Metilamina (CH₃NH₂): −6.3 °C
        - Dimetilamina (CH₃)₂NH: 7 °C
        - Trimetilamina (CH₃)₃N: 3.5 °C

    **Kepolaran:** Polar, larut dalam air untuk rantai pendek.

    **Ikatan Kimia:** Amina memiliki ikatan sigma (σ) antara nitrogen dan karbon/hidrogen.

    **Tata Nama (IUPAC):** Berdasarkan nama gugus alkil + amina.
    """)

def show_asam_karboksilat():
    st.title("Detail Senyawa: Asam Karboksilat")

    st.markdown("""
    **Deskripsi:** Asam karboksilat adalah senyawa organik yang memiliki gugus karboksil (–COOH). Rumus umum: R–COOH.

    **Titik Didih:**
    - Sangat tinggi dibanding alkohol, karena asam karboksilat membentuk ikatan hidrogen ganda (dimer) yang kuat.
    - Contoh:
        - Asam format (HCOOH): 100,8 °C
        - Asam asetat (CH₃COOH): 118,1 °C
        - Asam butirat (CH₃CH₂CH₂COOH): 163,7 °C

    **Kepolaran:** Sangat polar, sangat larut dalam air.

    **Ikatan Kimia:** Mengandung ikatan sigma (σ) dan pi (π) pada C=O.

    **Tata Nama (IUPAC):** Berdasarkan rantai utama yang mengandung gugus –COOH dan akhiran -oat untuk garam/ester.
    """)

def show_amida():
    st.title("Detail Senyawa: Amida")

    st.markdown("""
    **Deskripsi:** Amida adalah turunan dari asam karboksilat di mana gugus –OH pada gugus karboksil (–COOH) digantikan oleh gugus amina.

    **Titik Didih:**
    - Titik didih tinggi, karena dapat membentuk ikatan hidrogen yang kuat.
    - Contoh:
        - Metanamida (formamida, HCONH₂): 210 °C
        - Etanamida (asetamida, CH₃CONH₂): 222 °C

    **Kepolaran:** Sangat polar, larut dalam air.

    **Ikatan Kimia:** Memiliki ikatan sigma dan pi dalam gugus karbonil (C=O).

    **Tata Nama (IUPAC):** Berdasarkan nama asam karboksilat asalnya, dengan akhiran -amida.
    """)

def show_protein():
    st.title("Detail Senyawa: Protein")

    st.markdown("""
    **Deskripsi:** Protein adalah polimer alami yang tersusun dari rantai panjang asam amino yang terhubung oleh ikatan peptida.

    **Titik Didih:** Tidak relevan untuk protein besar, karena panas menyebabkan denaturasi.

    **Kepolaran:** Amfipatik, mengandung bagian polar dan nonpolar.

    **Ikatan Kimia:** Ikatan peptida (amida) antara gugus –COOH dan –NH₂ antar asam amino.

    **Tata Nama:** Tidak dinamai secara IUPAC, nama protein berdasarkan fungsi, struktur, atau asal biologis.
    """)

def show_karbohidrat():
    st.title("Detail Senyawa: Karbohidrat")

    st.markdown("""
    **Deskripsi:** Karbohidrat adalah senyawa organik yang terdiri dari unsur C, H, dan O, dengan rumus umum (CH₂O)n.

    **Titik Didih:** Tidak memiliki titik didih pasti, karena terurai sebelum menguap.

    **Kepolaran:** Sangat polar, larut dalam air.

    **Ikatan Kimia:** Tersusun dari ikatan glikosidik (C–O–C) antara gugus –OH dari dua monosakarida.

    **Tata Nama:** Monosakarida dinamai berdasarkan jumlah atom karbon + tipe gugus karbonil.
    """)

def show_lemak_minyak():
    st.title("Detail Senyawa: Lemak dan Minyak")

    st.markdown("""
    **Deskripsi:** Lemak dan minyak adalah ester dari gliserol dan asam lemak (trigliserida).

    **Titik Didih:** Sangat tinggi (300 °C ke atas), tetapi mudah rusak saat dipanaskan berlebih.

    **Kepolaran:** Nonpolar, tidak larut dalam air.

    **Ikatan Kimia:** Ikatan ester (–COO–) antara gliserol dan asam lemak.

    **Tata Nama:** Asam lemak dinamai seperti asam karboksilat panjang.
    """)

def show_benzena():
    st.title("Detail Senyawa: Benzena")

    st.markdown("""
    **Deskripsi:** Benzena adalah senyawa hidrokarbon aromatik paling sederhana dengan rumus C₆H₆.

    **Titik Didih:** Titik didih benzena: 80,1 °C.

    **Kepolaran:** Nonpolar secara keseluruhan.

    **Ikatan Kimia:** Setiap atom C terhubung dengan dua C lain dan satu H, membentuk ikatan sigma (σ).

    **Tata Nama (IUPAC):** Dinamai benzena jika murni.
    """)

def show_alkil_halida():
    st.title("Detail Senyawa: Alkil Halida")

    st.markdown("""
    **Deskripsi:** Alkil halida atau haloalkana adalah senyawa organik yang terbentuk dari alkana dengan menggantikan satu atau lebih atom H dengan atom halogen.

    **Titik Didih:** Titik didih lebih tinggi dari alkana dengan jumlah karbon setara.

    **Kepolaran:** Polar, larut dalam pelarut organik.

    **Ikatan Kimia:** Mengandung ikatan sigma (σ) polar antara C–X.

    **Tata Nama (IUPAC):** Berdasarkan rantai utama dari alkana dan posisi halogen.
    """)

def show_nitro():
    st.title("Detail Senyawa: Nitro")

    st.markdown("""
    **Deskripsi:** Senyawa nitro adalah senyawa organik yang mengandung gugus nitro (–NO₂).

    **Titik Didih:** Umumnya memiliki titik didih tinggi.

    **Kepolaran:** Sangat polar, larut dalam pelarut polar aprotik.

    **Ikatan Kimia:** Gugus nitro memiliki 1 ikatan sigma dan 1 ikatan pi antara N=O.

    **Tata Nama (IUPAC):** Gugus –NO₂ dinamai sebagai “nitro-” dan dianggap substituen.
    """)

def show_nitril():
    st.title("Detail Senyawa: Nitril")

    st.markdown("""
    **Deskripsi:** Nitril adalah senyawa organik yang mengandung gugus –C≡N (gugus sianida).

    **Titik Didih:** Nitril memiliki titik didih sedang hingga tinggi.

    **Kepolaran:** Sangat polar, larut dalam pelarut polar.

    **Ikatan Kimia:** Mengandung ikatan rangkap tiga antara karbon dan nitrogen.

    **Tata Nama (IUPAC):** Menggunakan akhiran -nitril.
    """)

def show_ester():
    st.title("Detail Senyawa: Ester")

    st.markdown("""
    **Deskripsi:** Ester adalah senyawa turunan asam karboksilat di mana gugus –OH diganti dengan gugus alkoksi (–OR).

    **Titik Didih:** Titik didih lebih rendah daripada asam karboksilat dan alkohol.

    **Kepolaran:** Agak polar, larut dalam pelarut organik.

    **Ikatan Kimia:** Mengandung 1 ikatan σ dan 1 ikatan π dalam gugus karbonil (C=O).

    **Tata Nama (IUPAC):** Nama alkil dari bagian alkohol + nama rantai asam dengan akhiran -oat.
    """)

def show_asam_halida():
    st.title("Detail Senyawa: Asam Halida")

    st.markdown("""
    **Deskripsi:** Asam halida adalah turunan dari asam karboksilat di mana gugus –OH diganti oleh halogen.

    **Titik Didih:** Titik didih lebih rendah daripada asam karboksilat.

    **Kepolaran:** Sangat polar, tidak larut dalam air.

    **Ikatan Kimia:** Mengandung 1 ikatan σ dan 1 ikatan π dalam gugus karbonil (C=O).

    **Tata Nama (IUPAC):** Nama berasal dari nama asam karboksilat induk, ubah akhiran -oat menjadi -oyl halida.
    """)

def show_chatbot():
    st.title("💬 Chatbot O-KIMIAKU")

    question = st.text_input("Tanyakan sesuatu tentang senyawa kimia (misal: kepolaran ester):")

    if question:
        q = question.lower()

        # Benzena
        if "benzena" in q:
            if "kepolaran" in q:
                st.success("Benzena bersifat nonpolar dan tidak larut dalam air.")
            elif "rumus" in q or "gugus" in q:
                st.success("Rumus benzena: C₆H₆.")
            elif "titik" in q:
                st.success("Titik didih benzena: 80,1 °C.")
            elif "fakta" in q:
                st.success("Benzena adalah senyawa hidrokarbon aromatik paling sederhana.")
            elif "tata nama" in q:
                st.success("Tata nama benzena: Dinamai benzena jika murni.")
            elif "ikatan" in q:
                st.success("Ikatan kimia benzena: Setiap atom C terhubung dengan dua C lain dan satu H, membentuk ikatan sigma (σ).")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Benzena di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Benzena adalah senyawa aromatik dengan struktur cincin.")
        else:
            st.warning("Maaf, senyawa tersebut belum tersedia atau belum dikenali.")

def show_about():
    st.title("Tentang Kami 👨‍💻")
    st.markdown("""
**Developer:**  
KELOMPOK 11 KELAS 1C 
1. Nama : Azizah Putri Azzahra (2460340)  
2. Nama : Nadifah Adya Anggita (2460449)
3. Nama : Raudhatul Dahlia (2460493)
4. Nama : Zahira Dwi Safitri (2460542) 
   
Kami membuat aplikasi ini untuk mempermudah pembelajaran kimia dengan cara yang interaktif.
""")

def show_rating():
    st.title("Sebelum Keluar, Beri Rating Aplikasi Ini ⭐")
    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.feedback("stars")
    if selected is not None:
       st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

# ------------- UI & PAGE CONTROL --------------
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Sidebar Navigasi TANPA LINGKARAN
st.sidebar.title("📚 Navigasi")

if st.sidebar.button("🏠 Beranda"):
    st.session_state.page = 'home'

if st.sidebar.button("👥 About Us"):
    st.session_state.page = 'about'

if st.sidebar.button("💬 Chatbot"):
    st.session_state.page = 'chatbot'
    
if st.sidebar.button(" ⭐ Rating"):
    st.session_state.page = 'rating'
    
# Routing
if st.session_state.page == 'home':
    show_home()
elif st.session_state.page == 'alkohol':
    show_alkohol()
elif st.session_state.page == 'about':
    show_about()
elif st.session_state.page == 'chatbot':
    show_chatbot()
elif st.session_state.page == 'rating':
    show_rating()
elif st.session_state.page == 'amina':
    show_amina()
elif st.session_state.page == 'alkil halida':
    show_alkil_halida()
elif st.session_state.page == 'eter':
    show_eter()
elif st.session_state.page == 'amida':
    show_amida()
elif st.session_state.page == 'nitril':
    show_nitril()
elif st.session_state.page == 'aldehida':
    show_aldehida()
elif st.session_state.page == 'nitro':
    show_nitril()
elif st.session_state.page == 'keton':
    show_keton()
elif st.session_state.page == 'asam halida':
    show_nitro()
elif st.session_state.page == 'ester':
    show_ester()
elif st.session_state.page == 'tiol':
    show_tiol()
elif st.session_state.page == 'alkana':
    show_alkana()
elif st.session_state.page == 'alkena':
    show_alkena()
elif st.session_state.page == 'alkuna':
    show_alkuna()
elif st.session_state.page == 'fenol':
    show_fenol()
elif st.session_state.page == 'benzena':
    show_benzena()
