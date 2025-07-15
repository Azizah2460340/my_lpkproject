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

def show_alkana():
    st.title("Detail Senyawa: Alkana")

    st.markdown("""
    **Deskripsi:** Alkana adalah senyawa hidrokarbon jenuh yang hanya mengandung ikatan tunggal (σ) antar atom karbon (C–C) dan antara karbon dengan hidrogen (C–H). Rumus umumnya adalah CₙH₂ₙ₊₂. Alkana termasuk senyawa nonpolar dan merupakan komponen utama dalam gas alam dan minyak bumi.

    **Titik Didih:**
    - Titik didih alkana meningkat seiring bertambahnya jumlah atom karbon (massa molekul).
    - Bentuk rantai lurus memiliki titik didih lebih tinggi dibanding bentuk bercabang, karena permukaan kontak antar molekul lebih luas.
    - Contoh:
        - Metana (CH₄): −161,5 °C
        - Etana (C₂H₆): −88,6 °C
        - Butana (C₄H₁₀): −0,5 °C

    **Kepolaran:** Nonpolar, karena distribusi elektron seimbang dan tidak ada perbedaan keelektronegatifan yang signifikan antara C dan H. Tidak larut dalam air, tapi larut dalam pelarut organik nonpolar seperti eter dan kloroform.

    **Ikatan Kimia:** Hanya memiliki ikatan tunggal kovalen (σ). Semua atom C dalam alkana bersifat sp³ hibridisasi dengan bentuk geometri tetrahedral.

    **Tata Nama (IUPAC):** Tata nama alkana berdasarkan:
    1. Jumlah atom karbon → menentukan nama dasar:
        - 1: met-, 2: et-, 3: prop-, 4: but-, 5: pent-, dst.
    2. Akhiran -ana untuk menandakan alkana.
    3. Jika ada cabang, nama dimulai dengan nomor posisi dan nama gugus alkil (metil, etil, dll).

    **Contoh:**
    - CH₄ → Metana
    - CH₃–CH₃ → Etana
    - CH₃–CH₂–CH₃ → Propana
    - CH₃–CH(CH₃)–CH₃ → 2-Metilpropana (bentuk bercabang)
    """)

def show_alkena():
    st.title("Detail Senyawa: Alkena")

    st.markdown("""
    **Deskripsi:** Alkena adalah senyawa hidrokarbon tak jenuh yang memiliki setidaknya satu ikatan rangkap dua (C=C) antar atom karbon. Rumus umumnya CₙH₂ₙ. Alkena lebih reaktif dibanding alkana karena keberadaan ikatan π.

    **Titik Didih:**
    - Titik didih alkena meningkat seiring bertambahnya jumlah atom karbon.
    - Titik didihnya mirip alkana dengan jumlah C yang sama, tapi sedikit lebih rendah karena ikatan rangkap membuat bentuk molekul kurang simetris.
    - Contoh:
        - Etena (C₂H₄): −103,7 °C
        - Propena (C₃H₆): −47,6 °C

    **Kepolaran:** Secara umum nonpolar, tapi sedikit lebih polar dari alkana karena kerapatan elektron di ikatan rangkap dua. Tidak larut dalam air, larut dalam pelarut organik nonpolar.

    **Ikatan Kimia:** Memiliki 1 ikatan sigma (σ) dan 1 ikatan pi (π) pada ikatan rangkap dua. Atom karbon pada ikatan rangkap bersifat sp² hibridisasi, dengan geometri planar trigonal (sudut 120°).

    **Tata Nama (IUPAC):** Penamaan alkena mengikuti:
    1. Rantai terpanjang yang mengandung ikatan rangkap dua.
    2. Nomor posisi ikatan rangkap diberikan serendah mungkin.
    3. Akhiran -ena menunjukkan alkena.

    **Contoh:**
    - CH₂=CH₂ → Etena
    - CH₂=CH–CH₃ → Propena
    - CH₃–CH=CH–CH₃ → But-2-ena (atau but-1-ena tergantung posisi ikatan)
    """)

def show_alkuna():
    st.title("Detail Senyawa: Alkuna")

    st.markdown("""
    **Deskripsi:** Alkuna adalah senyawa hidrokarbon tak jenuh yang memiliki setidaknya satu ikatan rangkap tiga (C≡C) antar atom karbon. Rumus umumnya CₙH₂ₙ₋₂. Karena adanya ikatan rangkap tiga, alkuna sangat reaktif dan dapat mengalami reaksi adisi.

    **Titik Didih:**
    - Titik didih alkuna meningkat seiring jumlah atom karbon.
    - Hampir mirip dengan alkena dan alkana, tetapi sedikit lebih tinggi karena ikatan rangkap tiga memberikan bentuk molekul yang lebih linier dan polarizable.
    - Contoh:
        - Etuna (asetilena, C₂H₂): −84 °C
        - Butuna (C₄H₆): sekitar 0–4 °C

    **Kepolaran:** Sebagian besar alkuna adalah nonpolar. Tidak larut dalam air, tapi larut dalam pelarut organik nonpolar seperti eter atau benzena.

    **Ikatan Kimia:** Memiliki 1 ikatan sigma (σ) dan 2 ikatan pi (π) dalam ikatan rangkap tiga. Atom karbon pada ikatan rangkap tiga bersifat sp hibridisasi, dengan geometri linier (sudut ikatan 180°).

    **Tata Nama (IUPAC):** Penamaan alkuna mengikuti:
    1. Pilih rantai terpanjang yang mengandung ikatan rangkap tiga.
    2. Penomoran dari ujung terdekat ikatan rangkap tiga.
    3. Gunakan akhiran -una.

    **Contoh:**
    - CH≡CH → Etuna (asetilena)
    - CH≡C–CH₃ → Propuna
    - CH₃–C≡C–CH₃ → But-2-una
    """)

def show_alkohol():
    st.title("Detail Senyawa: Alkohol")

    st.markdown("""
    **Deskripsi:** Alkohol adalah senyawa organik yang memiliki gugus hidroksil (–OH) yang terikat pada atom karbon jenuh (sp³). Rumus umum: R–OH, di mana R adalah gugus alkil. Alkohol bersifat polar dan sering terlibat dalam pembentukan ikatan hidrogen.

    **Titik Didih:**
    - Tinggi dibanding alkana/alkena/alkuna dengan jumlah karbon yang sama, karena ada ikatan hidrogen antar molekul alkohol.
    - Semakin panjang rantai karbon → makin tinggi titik didih.
    - Contoh:
        - Metanol (CH₃OH): 64,7 °C
        - Etanol (CH₃CH₂OH): 78,4 °C
        - 1-Butanol: 117,7 °C

    **Kepolaran:** Polar, karena gugus –OH memiliki perbedaan keelektronegatifan besar antara O dan H. Dapat larut dalam air (terutama alkohol rantai pendek) karena membentuk ikatan hidrogen. Alkohol rantai panjang → kelarutan menurun karena sifat nonpolar dari rantai alkil mendominasi.

    **Ikatan Kimia:** Gugus –OH terdiri dari ikatan kovalen polar O–H dan C–O. Atom O pada –OH dapat membentuk ikatan hidrogen antar molekul atau dengan air. Atom C yang terikat –OH bersifat sp³ hibridisasi.

    **Tata Nama (IUPAC):** Penamaan alkohol:
    1. Pilih rantai utama yang mengandung gugus –OH.
    2. Nomor posisi –OH serendah mungkin.
    3. Akhiran diganti menjadi -ol.
    4. Jika lebih dari satu gugus –OH, gunakan akhiran -diol, -triol, dst.

    **Contoh:**
    - CH₃OH → Metanol
    - CH₃CH₂OH → Etanol
    - CH₃CH(OH)CH₃ → 2-Propanol
    - HO–CH₂–CH₂–OH → 1,2-Etanadiol (etilen glikol)
    """)
    
def show_protein():
    st.title("Detail Senyawa: Protein")

    st.markdown("""
    **Deskripsi Pengetahuan Singkat:** Protein adalah polimer alami yang tersusun dari rantai panjang asam amino yang terhubung oleh ikatan peptida (sejenis ikatan amida). Protein berperan vital dalam struktur sel, enzim, hormon, antibodi, dan transportasi molekul. Struktur protein dibedakan menjadi:
    - **Struktur primer:** urutan asam amino
    - **Struktur sekunder:** bentuk lokal (α-heliks, β-sheet)
    - **Struktur tersier:** bentuk tiga dimensi
    - **Struktur kuartener:** asosiasi beberapa rantai polipeptida

    **Titik Didih:**
    - Tidak relevan untuk protein besar, karena protein tidak memiliki titik didih yang pasti—panas menyebabkan denaturasi (struktur rusak) sebelum menguap.
    - Denaturasi biasanya terjadi di kisaran suhu 40–80 °C, tergantung jenis protein.

    **Kepolaran:**
    - Amfipatik (mengandung bagian polar dan nonpolar)
    - Beberapa bagian protein polar dan larut dalam air (berinteraksi dengan lingkungan sel), bagian lain nonpolar dan tersembunyi di dalam struktur 3D.

    **Ikatan Kimia:**
    - Ikatan peptida (amida) antara gugus –COOH dan –NH₂ antar asam amino
    - Ikatan non-kovalen: ikatan hidrogen, gaya van der Waals, interaksi hidrofobik
    - Ikatan disulfida (–S–S–) antara dua sistein → membantu struktur stabil

    **Tata Nama:**
    - Tidak dinamai secara IUPAC seperti senyawa organik kecil.
    - Nama protein berdasarkan fungsi, struktur, atau asal biologis, misalnya:
        - Insulin → hormon pengatur gula darah
        - Hemoglobin → pengangkut oksigen
        - Amilase → enzim pemecah pati
    """)

def show_fenol():
    st.title("Detail Senyawa: Fenol")

    st.markdown("""
    **Deskripsi:** Fenol (C₆H₅OH) adalah senyawa aromatik yang terdiri dari cincin benzena yang terikat pada gugus hidroksil (-OH). Fenol adalah padatan kristal putih yang mudah larut dalam pelarut organik dan sedikit larut dalam air. Berbau khas tajam dan bersifat korosif.

    **Titik Didih:**
    - Titik didih fenol: 181,7 °C
    - Titik leleh: 40,9 °C
    - Titik didihnya lebih tinggi dari benzena karena adanya ikatan hidrogen antar molekul fenol.

    **Kepolaran:** Polar, karena mengandung gugus hidroksil (-OH) yang bersifat polar. Meskipun cincin benzena bersifat nonpolar, gugus -OH membuat senyawa ini memiliki momen dipol.

    **Ikatan Kimia:** Ikatan kovalen antara atom karbon dan hidrogen dalam cincin benzena. Gugus -OH terikat secara kovalen ke cincin aromatik. Ikatan hidrogen dapat terbentuk antar molekul fenol karena adanya gugus -OH, menyebabkan titik didih tinggi. Interaksi resonansi juga terjadi antara cincin benzena dan gugus -OH, memengaruhi sifat keasaman fenol.

    **Tata Nama (IUPAC dan umum):**
    - Nama umum: Fenol
    - Nama IUPAC: Benzenol
    - Jika fenol memiliki substituen, penamaannya mengikuti posisi pada cincin, misalnya:
        - o-Kresol (2-metilfenol) → gugus metil di posisi orto
        - p-Nitrofenol (4-nitrobenzenol) → gugus nitro di posisi para
    """)
def show_eter():
    st.title("Detail Senyawa: Eter")

    st.markdown("""
    **Deskripsi:** Eter adalah senyawa organik yang memiliki dua gugus alkil atau aril yang terikat pada atom oksigen. Rumus umum untuk eter adalah R–O–R', di mana R dan R' adalah gugus alkil atau aril. Eter sering digunakan sebagai pelarut dalam reaksi kimia dan sebagai bahan bakar.

    **Titik Didih:**
    - Titik didih eter lebih rendah dibandingkan alkohol dengan massa molekul yang sama, karena eter tidak dapat membentuk ikatan hidrogen antar molekul.
    - Namun, titik didih eter lebih tinggi dibandingkan dengan hidrokarbon nonpolar seukuran.
    - Contoh:
        - Dietil eter (C₂H₅)₂O: 34,6 °C
        - Eter metil (CH₃)₂O: −24,9 °C

    **Kepolaran:** 
    - Eter bersifat polar, tetapi tidak sepolar alkohol. Eter dapat membentuk ikatan hidrogen dengan air, tetapi tidak dapat membentuk ikatan hidrogen antar molekul eter.
    - Eter rantai pendek larut dalam air, tetapi eter rantai panjang kurang larut.

    **Ikatan Kimia:**
    - Eter memiliki ikatan sigma (σ) antara atom karbon dan oksigen.
    - Struktur eter bersifat tetrahedral di sekitar atom oksigen, dengan sudut ikatan sekitar 110°.
    - Eter tidak memiliki ikatan pi (π) karena tidak ada ikatan rangkap.

    **Tata Nama (IUPAC):**
    - Penamaan eter dilakukan dengan menyebutkan nama gugus alkil yang terikat pada oksigen, diikuti dengan kata "eter".
    - Jika ada dua gugus alkil yang berbeda, nama yang lebih besar ditulis terlebih dahulu.

    **Contoh:**
    - CH₃OCH₃ → Dimetil eter
    - C₂H₅OCH₃ → Eter metil etil
    - C₃H₇OCH₂CH₃ → Eter etil propil
    """)

def show_aldehida():
    st.title("Detail Senyawa: Aldehid")

    st.markdown("""
    **Deskripsi:** Aldehid adalah senyawa organik yang memiliki gugus karbonil (C=O) di ujung rantai karbon, dengan rumus umum R–CHO. Gugus fungsionalnya disebut formil. Aldehid banyak ditemukan dalam zat aroma dan zat antara dalam sintesis organik.

    **Titik Didih:**
    - Titik didih lebih tinggi daripada alkana/eter, tapi lebih rendah dari alkohol.
    - Ini karena aldehid memiliki ikatan dipol-dipol, tetapi tidak bisa membentuk ikatan hidrogen antar sesamanya.
    - Contoh:
        - Formaldehida (HCHO): −19 °C
        - Asetaldehida (CH₃CHO): 20,2 °C
        - Butanal: 75 °C

    **Kepolaran:** Sangat polar, karena gugus karbonil (C=O) memiliki perbedaan keelektronegatifan besar antara C dan O. Larut dalam air (terutama rantai pendek) karena dapat membentuk ikatan hidrogen dengan air.

    **Ikatan Kimia:** Gugus karbonil terdiri dari satu ikatan sigma (σ) dan satu ikatan pi (π). Atom karbon pada C=O bersifat sp² hibridisasi dengan bentuk planar trigonal. Ujung gugus –CHO memberikan reaktivitas tinggi, terutama dalam reaksi oksidasi dan adisi nukleofilik.

    **Tata Nama (IUPAC):** Penamaan aldehid:
    1. Pilih rantai utama yang mengandung gugus –CHO.
    2. Beri nomor dari karbon aldehid (selalu nomor 1).
    3. Ganti akhiran -a pada nama alkana menjadi -al.

    **Contoh:**
    - HCHO → Metanal (formaldehida)
    - CH₃CHO → Etanal (asetaldehida)
    - CH₃CH₂CH₂CHO → Butanal
    """)

def show_keton():
    st.title("Detail Senyawa: Keton")

    st.markdown("""
    **Deskripsi:** Keton adalah senyawa organik yang memiliki gugus karbonil (C=O) di tengah rantai karbon, bukan di ujung seperti aldehid. Rumus umumnya R–CO–R′, di mana R dan R′ adalah gugus alkil atau aril. Keton sering ditemukan dalam pelarut dan zat aroma (misalnya: aseton).

    **Titik Didih:**
    - Titik didih lebih tinggi dari alkana/eter, tetapi lebih rendah dari alkohol.
    - Karena memiliki gaya dipol-dipol kuat, tetapi tidak membentuk ikatan hidrogen antar sesamanya.
    - Contoh:
        - Aseton (CH₃COCH₃): 56,5 °C
        - 2-Butanon (CH₃COCH₂CH₃): 79,6 °C

    **Kepolaran:** Polar, karena gugus karbonil bersifat polar. Keton rantai pendek larut dalam air karena bisa membentuk ikatan hidrogen dengan air, tapi rantai panjang → kelarutan berkurang. Umumnya larut baik dalam pelarut organik.

    **Ikatan Kimia:** Gugus karbonil mengandung 1 ikatan sigma (σ) dan 1 ikatan pi (π). Atom karbon dalam gugus C=O bersifat sp² hibridisasi dan memiliki bentuk planar trigonal. Karena karbonilnya di tengah, keton tidak mudah teroksidasi seperti aldehid.

    **Tata Nama (IUPAC):** Penamaan keton:
    1. Pilih rantai utama yang mengandung gugus karbonil.
    2. Penomoran dilakukan agar posisi karbonil mendapatkan nomor serendah mungkin.
    3. Ganti akhiran -a pada alkana menjadi -on.
    4. Sebutkan posisi gugus karbonil jika diperlukan.

    **Contoh:**
        - CH₃COCH₃ → Propanon (aseton)
        - CH₃CH₂COCH₃ → Butanon
        - CH₃COCH₂CH₂CH₃ → Pentan-2-on
    """)

def show_amina():
    st.title("Detail Senyawa: Amina")

    st.markdown("""
    **Deskripsi:** Amina adalah senyawa organik turunan amonia (NH₃) di mana satu atau lebih atom hidrogen diganti dengan gugus alkil atau aril. Dibagi menjadi:
    - Amina primer (1°): R–NH₂
    - Amina sekunder (2°): R–NH–R′
    - Amina tersier (3°): R–N(R′)–R″
    Amina banyak terdapat dalam senyawa biologis (seperti asam amino, neurotransmitter) dan obat-obatan.

    **Titik Didih:**
    - Amina primer dan sekunder dapat membentuk ikatan hidrogen, sehingga titik didihnya lebih tinggi dari senyawa nonpolar (seperti alkana), tetapi lebih rendah dari alkohol.
    - Amina tersier tidak dapat membentuk ikatan hidrogen antar sesama molekul → titik didihnya lebih rendah.
    - Contoh:
        - Metilamina (CH₃NH₂): −6.3 °C
        - Dimetilamina (CH₃)₂NH: 7 °C
        - Trimetilamina (CH₃)₃N: 3.5 °C

    **Kepolaran:** Polar, karena adanya pasangan elektron bebas pada atom nitrogen dan perbedaan keelektronegatifan antara N dan H/C. Amina rantai pendek larut dalam air karena bisa membentuk ikatan hidrogen dengan air. Amina rantai panjang → kelarutan menurun.

    **Ikatan Kimia:** Amina memiliki ikatan sigma (σ) antara nitrogen dan karbon/hidrogen. Nitrogen dalam amina biasanya bersifat sp³ hibridisasi, dengan bentuk piramida trigonal dan satu pasangan elektron bebas. Bersifat basa lemah, karena nitrogen dapat menerima proton (donor pasangan elektron).

    **Tata Nama (IUPAC):** Penamaan amina:
    - Amina primer: Nama gugus alkil + amina
        - CH₃NH₂ → Metilamina
        - CH₃CH₂NH₂ → Etilamina
    - Amina sekunder/tersier:
        - Jika sederhana → sebutkan semua gugus alkil + “amina”
            - (CH₃)₂NH → Dimetilamina
        - Untuk yang lebih kompleks → dianggap substituen: “amino-”
            - NH₂CH₂CH₃ → 2-Aminoetana
    """)
def show_asam_karboksilat():
    st.title("Detail Senyawa: Asam Karboksilat")

    st.markdown("""
    **Deskripsi:** Asam karboksilat adalah senyawa organik yang memiliki gugus karboksil (–COOH), yaitu gabungan dari gugus karbonil (C=O) dan hidroksil (–OH) pada karbon yang sama. Rumus umum: R–COOH. Senyawa ini bersifat asam lemah dan banyak ditemukan dalam alam, seperti dalam cuka (asam asetat) dan lemak (asam lemak).

    **Titik Didih:**
    - Sangat tinggi dibanding alkohol, karena asam karboksilat membentuk ikatan hidrogen ganda (dimer) yang kuat antar molekul.
    - Titik didih meningkat seiring bertambahnya jumlah atom karbon.
    - Contoh:
        - Asam format (HCOOH): 100,8 °C
        - Asam asetat (CH₃COOH): 118,1 °C
        - Asam butirat (CH₃CH₂CH₂COOH): 163,7 °C

    **Kepolaran:** Sangat polar, karena mengandung gugus karbonil dan hidroksil sekaligus. Sangat larut dalam air (terutama rantai pendek), karena dapat membentuk ikatan hidrogen dengan air. Rantai panjang → kelarutan menurun karena bagian hidrokarbon makin dominan.

    **Ikatan Kimia:**
    - Mengandung:
        - Ikatan sigma (σ) dan pi (π) pada C=O.
        - Ikatan sigma antara C–O dan O–H.
        - Atom karbon pada –COOH bersifat sp² hibridisasi, dengan bentuk planar trigonal.
        - Dapat melepaskan proton (H⁺) dari gugus –OH → bersifat asam lemah.

    **Tata Nama (IUPAC):** Penamaan asam karboksilat:
    1. Rantai utama mencakup gugus –COOH.
    2. Nomor 1 selalu diberikan pada karbon karboksilat.
    3. Nama alkana diganti akhiran -a menjadi -oat (untuk garam/ester) atau -oat ion (untuk ionik), tetapi untuk asam murni: -oat tetap disebut “asam -oat”.

    **Contoh:**
        - HCOOH → Asam metanoat (asam format)
        - CH₃COOH → Asam etanoat (asam asetat)
        - CH₃CH₂CH₂COOH → Asam butanoat (asam butirat)
    """)
    
def show_lemak_dan_minyak():
    st.title("Detail Senyawa: Lemak dan Minyak")

    st.markdown("""
    **Deskripsi:** Lemak dan minyak adalah bagian dari kelompok lipid yang terdiri dari ester dari gliserol dan asam lemak (disebut trigliserida).
    - **Lemak:** padat pada suhu ruang → biasanya berasal dari hewan.
    - **Minyak:** cair pada suhu ruang → biasanya berasal dari tumbuhan atau ikan.
    Perbedaan utama terletak pada tingkat kejenuhan:
    - Lemak jenuh → tidak ada ikatan rangkap (C–C)
    - Minyak tak jenuh → ada satu atau lebih ikatan rangkap (C=C)

    **Titik Didih:**
    - Titik didih trigliserida sangat tinggi (300 °C ke atas), tapi mudah rusak (terurai) saat dipanaskan berlebih.
    - Titik leleh:
        - Lemak jenuh → titik leleh tinggi (padat)
        - Minyak tak jenuh → titik leleh rendah (cair)

    **Kepolaran:** 
    - Nonpolar, karena struktur utamanya terdiri dari rantai hidrokarbon panjang.
    - Tidak larut dalam air, tapi larut dalam pelarut nonpolar seperti eter, kloroform, atau benzena.

    **Ikatan Kimia:**
    - Ikatan ester (–COO–) antara gugus –OH dari gliserol dan gugus –COOH dari asam lemak.
    - Asam lemak bisa:
        - Jenuh (tanpa ikatan rangkap) → lurus, mudah padat
        - Tak jenuh (mengandung ikatan rangkap) → bengkok, mencegah pemadatan
    - Dalam minyak nabati, sering mengandung asam lemak tak jenuh seperti asam oleat.

    **Tata Nama:**
    - Tidak dinamai secara sistem IUPAC penuh, tetapi:
        - Asam lemak dinamai seperti asam karboksilat panjang:
            - Asam stearat (C₁₇H₃₅COOH)
            - Asam oleat (C₁₇H₃₃COOH)
        - Trigliserida → dinamai berdasarkan kombinasi asam lemak dan gliserol.
        - Contoh:
            - Tristearin → dari 3 asam stearat + gliserol
            - Triolein → dari 3 asam oleat + gliserol
    """)

def show_benzena():
    st.title("Detail Senyawa: Benzena")

    st.markdown("""
    **Deskripsi:** Benzena adalah senyawa hidrokarbon aromatik paling sederhana dengan rumus C₆H₆. Strukturnya berupa cincin planar dengan 6 atom karbon dan 6 atom hidrogen, di mana ikatan antar karbon mengalami resonansi → menghasilkan delokalisasi elektron pada cincin aromatik. Benzena bersifat stabil, tapi tetap bisa mengalami reaksi substitusi.

    **Titik Didih:**
    - Titik didih benzena: 80,1 °C
    - Lebih tinggi dari senyawa nonpolar kecil lainnya karena bentuk simetris dan interaksi π-π antar cincin aromatik.
    - Titik leleh: 5,5 °C

    **Kepolaran:** 
    - Nonpolar secara keseluruhan, karena simetris dan tidak memiliki gugus polar.
    - Tidak larut dalam air, tapi larut dalam pelarut organik nonpolar seperti eter, kloroform, atau heksana.

    **Ikatan Kimia:**
    - Setiap atom C terhubung dengan dua C lain dan satu H → membentuk ikatan sigma (σ).
    - Terdapat delokalisasi elektron π di atas dan di bawah cincin → menghasilkan resonansi aromatik.
    - Semua ikatan C–C pada benzena setara dengan panjang ikatan antara ikatan tunggal dan rangkap.

    **Tata Nama (IUPAC):**
    - Senyawa ini dinamai benzena jika murni.
    - Jika bercabang, penamaan dilakukan dengan memberi nomor pada cincin:
        - C₆H₅CH₃ → metilbenzena (toluena)
        - C₆H₅OH → hidroksibenzena (fenol)
        - C₆H₅NO₂ → nitrobenzena
    - Jika ada dua substituen: orto (1,2), meta (1,3), para (1,4) digunakan untuk posisi relatifnya.
    """)
def show_amida():
    st.title("Detail Senyawa: Amida")

    st.markdown("""
    **Deskripsi:** Amida adalah turunan dari asam karboksilat di mana gugus –OH pada gugus karboksil (–COOH) digantikan oleh gugus amina (–NH₂, –NHR, atau –NR₂). Rumus umum: R–CONH₂ untuk amida primer. Amida banyak ditemukan dalam protein (ikatan peptida adalah amida).

    **Titik Didih:**
    - Titik didih tinggi, karena dapat membentuk ikatan hidrogen yang kuat (terutama amida primer dan sekunder).
    - Titik didih amida biasanya lebih tinggi dari asam karboksilat dengan massa molekul setara.
    - Contoh:
        - Metanamida (formamida, HCONH₂): 210 °C
        - Etanamida (asetamida, CH₃CONH₂): 222 °C

    **Kepolaran:** 
    - Sangat polar, karena adanya gugus karbonil (C=O) dan gugus amino (–NH₂) yang keduanya bersifat polar.
    - Larut dalam air (terutama amida rantai pendek) karena mampu membentuk ikatan hidrogen dengan air.

    **Ikatan Kimia:**
    - Memiliki:
        - Ikatan sigma dan pi dalam gugus karbonil (C=O)
        - Ikatan sigma antara C–N dan N–H
    - Atom karbon dalam gugus –CONH₂ bersifat sp² hibridisasi, struktur planar.
    - Ikatan C–N dalam amida memiliki karakter ganda sebagian (resonansi) → membuatnya stabil dan kurang reaktif dibanding amina biasa.

    **Tata Nama (IUPAC):**
    - Penamaan amida:
        1. Nama berasal dari asam karboksilat asalnya, dengan akhiran -amida.
        2. Jika gugus N disubstitusi (pada amida sekunder/tersier), gugus tambahan diberi awalan N-.

    **Contoh:**
    - CH₃CONH₂ → Etanamida (asetamida)
    - HCONH₂ → Metanamida (formamida)
    - CH₃CONHCH₃ → N-Metiletanamida
    - CH₃CON(CH₃)₂ → N,N-Dimetiletanamida
    """)
def show_alkil_halida():
    st.title("Detail Senyawa: Alkil Halida")

    st.markdown("""
    **Deskripsi:** Alkil halida atau haloalkana adalah senyawa organik yang terbentuk dari alkana dengan menggantikan satu atau lebih atom H dengan atom halogen (F, Cl, Br, I). Rumus umum: R–X, di mana R = gugus alkil, X = halogen. Digunakan luas dalam industri, pelarut, refrigeran, dan sebagai senyawa antara dalam sintesis organik.

    **Titik Didih:**
    - Titik didih lebih tinggi dari alkana dengan jumlah karbon setara, karena interaksi dipol–dipol dari gugus halogen.
    - Titik didih meningkat dengan:
        - Meningkatnya massa molekul (dari F ke I)
        - Meningkatnya panjang rantai karbon
    - Contoh:
        - CH₃Cl: −24,2 °C
        - CH₃Br: 3,6 °C
        - CH₃I: 42,4 °C

    **Kepolaran:** 
    - Polar, karena perbedaan keelektronegatifan antara karbon dan halogen → menciptakan ikatan polar C–X.
    - Larut dalam pelarut organik, tetapi tidak larut baik dalam air, kecuali untuk haloalkana kecil.

    **Ikatan Kimia:**
    - Mengandung ikatan sigma (σ) polar antara C–X.
    - Halogen bersifat elektronegatif → menarik elektron dari C → C menjadi elektrofilik (suka diserang nukleofil).
    - Atom karbon dalam alkil halida umumnya sp³ hibridisasi.
    - Reaktif dalam reaksi substitusi dan eliminasi, tergantung kondisi.

    **Tata Nama (IUPAC):**
    - Penamaan alkil halida:
        1. Pilih rantai utama dari alkana.
        2. Nomori rantai agar posisi halogen (F, Cl, Br, I) serendah mungkin.
        3. Gunakan awalan fluoro-, kloro-, bromo-, iodo- sesuai halogennya.

    **Contoh:**
    - CH₃Cl → Klorometana
    - CH₃CH₂Br → Bromometana
    - CH₃CH(Cl)CH₃ → 2-Kloropropana
    - CH₃CHBrCH₂CH₃ → 2-Bromobutana
    """)
def show_nitro():
    st.title("Detail Senyawa: Nitro")

    st.markdown("""
    **Deskripsi:** Senyawa nitro adalah senyawa organik yang mengandung gugus nitro (–NO₂), yaitu gugus nitrogen yang terikat pada dua atom oksigen: satu melalui ikatan rangkap (N=O), satu melalui ikatan tunggal (N–O⁻), membentuk struktur resonansi. Contoh umum: nitrobenzena (C₆H₅NO₂). Senyawa nitro penting dalam bahan peledak (seperti TNT), pelarut, dan sintesis kimia.

    **Titik Didih:**
    - Umumnya memiliki titik didih tinggi, karena:
        - Gugus nitro sangat polar
        - Terjadi gaya tarik dipol-dipol kuat antar molekul
    - Contoh:
        - Nitroetan: 114 °C
        - Nitrobenzena: 210,9 °C

    **Kepolaran:** 
    - Sangat polar, karena gugus –NO₂ memiliki distribusi muatan tidak merata (struktur resonansi dengan muatan parsial).
    - Larut dalam pelarut polar aprotik, tapi umumnya tidak larut dalam air (kecuali yang kecil seperti nitrometana).

    **Ikatan Kimia:**
    - Gugus nitro memiliki:
        - 1 ikatan sigma dan 1 ikatan pi antara N=O
        - 1 ikatan sigma antara N–O
    - Resonansi membuat muatan tersebar antara kedua oksigen → stabil.
    - Atom N dalam gugus –NO₂ bersifat sp² hibridisasi dan berbentuk planar.

    **Tata Nama (IUPAC):**
    - Gugus –NO₂ dinamai sebagai “nitro-” dan dianggap substituen.
    - Letaknya ditunjukkan dengan nomor posisi pada rantai utama atau cincin aromatik.

    **Contoh:**
    - CH₃NO₂ → Nitrometana
    - CH₃CH₂NO₂ → Nitroetana
    - C₆H₅NO₂ → Nitrobenzena
    - C₆H₄(NO₂)₂ → 1,3-Dinitrobenzena (atau meta-dinitrobenzena)
    """)

def show_nitril():
    st.title("Detail Senyawa: Nitril")

    st.markdown("""
    **Deskripsi:** Nitril adalah senyawa organik yang mengandung gugus –C≡N (gugus sianida), yaitu atom karbon yang berikatan rangkap tiga dengan atom nitrogen. Rumus umum: R–C≡N. Nitril sering digunakan sebagai bahan antara dalam sintesis senyawa farmasi, polimer (seperti akrilonitril), dan pelarut polar aprotik.

    **Titik Didih:**
    - Nitril memiliki titik didih sedang hingga tinggi, tergantung panjang rantai karbonnya.
    - Titik didih lebih tinggi dari alkana/alkil halida karena adanya interaksi dipol-dipol kuat dari gugus –C≡N.
    - Contoh:
        - Akrilonitril (CH₂=CH–CN): 77 °C
        - Propanonitril (CH₃CH₂–CN): 97 °C

    **Kepolaran:** 
    - Sangat polar, karena ikatan rangkap tiga C≡N menciptakan momen dipol yang besar.
    - Larut dalam pelarut polar (seperti air, alkohol) terutama untuk nitril rantai pendek.
    - Sering digunakan sebagai pelarut polar aprotik dalam kimia organik.

    **Ikatan Kimia:**
    - Mengandung ikatan rangkap tiga antara karbon dan nitrogen:
        - 1 ikatan sigma (σ)
        - 2 ikatan pi (π)
    - Atom karbon dalam gugus nitril bersifat sp hibridisasi, sehingga molekul bersifat linier di sekitar gugus –C≡N.
    - Gugus nitril bersifat elektrofilik → dapat mengalami reaksi adisi dan hidrolisis.

    **Tata Nama (IUPAC):**
    - Penamaan IUPAC menggunakan akhiran -nitril, dan rantai utama harus mencakup karbon dari gugus –C≡N.
    - Jika gugus –CN sebagai substituen → disebut “siano-”.

    **Contoh:**
    - CH₃–C≡N → Etanonitril (nama umum: asetonitril)
    - C₆H₅–C≡N → Benzenakarbonitril (nama umum: benzonitril)
    - CH₂=CH–C≡N → Akrilonitril
    - NC–CH₂–CH₂–COOH → Asam sianopropanoat
    """)

def show_ester():
    st.title("Detail Senyawa: Ester")

    st.markdown("""
    **Deskripsi:** Ester adalah senyawa turunan asam karboksilat di mana gugus –OH diganti dengan gugus alkoksi (–OR). Rumus umum: R–COOR′. Ester sering ditemukan dalam aroma buah, minyak esensial, dan sebagai pelarut organik atau bahan pembuatan plastik (poliester).

    **Titik Didih:**
    - Titik didih lebih rendah daripada asam karboksilat dan alkohol, karena ester tidak membentuk ikatan hidrogen antar molekulnya.
    - Namun, lebih tinggi dari eter atau alkana seukuran karena ada interaksi dipol-dipol.
    - Contoh:
        - Metil etanoat (CH₃COOCH₃): 57 °C
        - Etil etanoat (CH₃COOCH₂CH₃): 77 °C

    **Kepolaran:** 
    - Agak polar, karena mengandung gugus karbonil (C=O) dan gugus eter (C–O–C).
    - Ester rantai pendek larut dalam air (dapat membentuk ikatan hidrogen dengan air), namun rantai panjang tidak larut.
    - Larut dalam pelarut organik seperti eter dan alkohol.

    **Ikatan Kimia:**
    - Ester mengandung:
        - 1 ikatan σ dan 1 ikatan π dalam gugus karbonil (C=O)
        - Ikatan σ antara C–O dan C–C
    - Atom karbon dalam gugus karbonil bersifat sp² hibridisasi, membentuk struktur planar trigonal.
    - Ester mudah mengalami reaksi hidrolisis menjadi asam karboksilat dan alkohol, terutama dengan katalis asam atau basa.

    **Tata Nama (IUPAC):**
    - Penamaan ester terdiri dari dua bagian:
        1. Nama alkil dari bagian alkohol (yang terikat ke O)
        2. Nama rantai asam dengan akhiran diganti menjadi -oat

    **Contoh:**
    - CH₃COOCH₃ → Metil etanoat
    - CH₃COOCH₂CH₃ → Etil etanoat
    - CH₃CH₂COOCH₃ → Metil propanoat
    - CH₃CH₂COOCH₂CH₃ → Etil propanoat
    """)

def show_asam_halida():
    st.title("Detail Senyawa: Asam Halida")

    st.markdown("""
    **Deskripsi:** Asam halida (lebih tepatnya: asil halida) adalah turunan dari asam karboksilat di mana gugus –OH diganti oleh halogen (umumnya Cl atau Br). Rumus umum: R–COX, dengan X = halogen. Asetil klorida (CH₃COCl) adalah contoh paling umum. Senyawa ini sangat reaktif, digunakan sebagai bahan antara dalam sintesis ester, amida, dan senyawa organik lainnya.

    **Titik Didih:**
    - Titik didih lebih rendah daripada asam karboksilat karena tidak ada ikatan hidrogen antar molekul.
    - Namun tetap relatif tinggi karena adanya gugus karbonil polar dan halogen elektronegatif.
    - Contoh:
        - Asetil klorida (CH₃COCl): 51 °C
        - Benzoyl klorida (C₆H₅COCl): 198 °C

    **Kepolaran:** 
    - Sangat polar, karena gugus karbonil (C=O) dan C–X (X = halogen) bersifat polar.
    - Tidak larut dalam air, karena sangat reaktif → akan bereaksi dengan air (terhidrolisis) membentuk asam karboksilat dan asam halida (seperti HCl).
    - Dilarutkan dalam pelarut aprotik kering (misal: eter, diklorometana).

    **Ikatan Kimia:**
    - Mengandung:
        - 1 ikatan σ dan 1 ikatan π dalam gugus karbonil (C=O)
        - Ikatan σ pada C–Cl (atau C–Br)
    - Karbon karbonil bersifat sp² hibridisasi, dan molekulnya planar trigonal di sekitar karbon pusat.
    - Sangat elektrofilik karena kombinasi gugus karbonil dan halogen → sangat mudah diserang nukleofil.

    **Tata Nama (IUPAC):**
    - Nama berasal dari nama asam karboksilat induk, ubah akhiran -oat menjadi -oyl halida (atau -il halida dalam bentuk umum).
    - Gunakan nama halogen sebagai akhiran.

    **Contoh:**
    - CH₃COCl → Etanoil klorida (asetil klorida)
    - C₂H₅COBr → Propanoil bromida
    - C₆H₅COCl → Benzoil klorida
    """)
    
def show_karbohidrat():
    st.title("Detail Senyawa: Karbohidrat")

    st.markdown("""
    **Deskripsi Pengetahuan Singkat:** Karbohidrat adalah senyawa organik yang terdiri dari unsur C, H, dan O, dengan rumus umum (CH₂O)n. Fungsinya sebagai sumber energi utama, bahan struktural (seperti selulosa), dan penyimpan energi (seperti pati). Karbohidrat dibagi menjadi:
    - **Monosakarida:** (glukosa, fruktosa)
    - **Disakarida:** (sukrosa, laktosa)
    - **Polisakarida:** (pati, glikogen, selulosa)

    **Titik Didih:**
    - Tidak memiliki titik didih pasti, karena karbohidrat terurai atau terkarbonisasi sebelum menguap.
    - Monosakarida dan disakarida mudah larut dalam air dan bersifat padat kristalin pada suhu ruang.

    **Kepolaran:**
    - Sangat polar, karena banyak mengandung gugus hidroksil (–OH).
    - Larut dalam air (terutama monosakarida dan disakarida) karena bisa membentuk ikatan hidrogen dengan air.
    - Polisakarida besar (seperti pati dan selulosa) tidak larut, tapi bisa menyerap air.

    **Ikatan Kimia:**
    - Tersusun dari ikatan glikosidik (C–O–C) antara gugus –OH dari dua monosakarida.
    - Gugus fungsional penting: aldehid (–CHO) atau keton (–CO) pada monosakarida.
    - Ikatan hidrogen antargugus –OH penting untuk membentuk struktur tiga dimensi (misalnya heliks pada pati).

    **Tata Nama:**
    - Monosakarida dinamai berdasarkan jumlah atom karbon + tipe gugus karbonil:
        - Aldosa (gugus aldehid) → glukosa (aldoheksosa)
        - Ketosa (gugus keton) → fruktosa (ketoheksosa)
    - Disakarida/polisakarida dinamai berdasarkan jenis dan urutan monosakaridanya:
        - Glukosa + fruktosa → sukrosa
        - Glukosa + glukosa → maltosa
        - Polimer glukosa → amilosa (dalam pati), selulosa, glikogen
    """)

def show_chatbot():
    st.title("💬 Chatbot O-KIMIAKU")

    question = st.text_input("Tanyakan sesuatu tentang senyawa kimia (misal: kepolaran ester):")

    if question:
        q = question.lower()

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
        if "keton" in q:
            if "kepolaran" in q:
                st.success("Keton bersifat polar karena memiliki gugus karbonil (C=O).")
            elif "rumus" in q or "gugus" in q:
                st.success("Gugus fungsi keton: R–CO–R'.")
            elif "titik" in q:
                st.success("Titik didih keton lebih tinggi dari alkana, tetapi lebih rendah dari alkohol.")
            elif "fakta" in q:
                st.success("Keton sering ditemukan dalam pelarut dan zat aroma.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Keton di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Keton adalah senyawa organik dengan gugus karbonil di tengah rantai.")
        if "amina" in q:
            if "kepolaran" in q:
                st.success("Amina bersifat polar karena adanya pasangan elektron bebas pada nitrogen.")
            elif "rumus" in q or "gugus" in q:
                st.success("Gugus fungsi amina: R–NH₂, R–NH–R', R–N(R')–R''.")
            elif "titik" in q:
                st.success("Titik didih amina primer dan sekunder lebih tinggi dari senyawa nonpolar.")
            elif "fakta" in q:
                st.success("Amina banyak terdapat dalam senyawa biologis seperti asam amino.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Amina di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Amina adalah turunan amonia di mana satu atau lebih atom hidrogen diganti dengan gugus alkil.")
        if "asam karboksilat" in q:
            if "kepolaran" in q:
                st.success("Asam karboksilat sangat polar karena mengandung gugus karbonil dan hidroksil.")
            elif "rumus" in q or "gugus" in q:
                st.success("Gugus fungsi asam karboksilat: R–COOH.")
            elif "titik" in q:
                st.success("Titik didih asam karboksilat sangat tinggi karena ikatan hidrogen.")
            elif "fakta" in q:
                st.success("Asam karboksilat banyak ditemukan dalam alam, seperti dalam cuka.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Asam Karboksilat di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Asam karboksilat adalah senyawa organik dengan gugus karboksil.")
        if "amida" in q:
            if "kepolaran" in q:
                st.success("Amida sangat polar karena adanya gugus karbonil dan gugus amino.")
            elif "rumus" in q or "gugus" in q:
                st.success("Gugus fungsi amida: R–CONH₂.")
            elif "titik" in q:
                st.success("Titik didih amida tinggi karena dapat membentuk ikatan hidrogen.")
            elif "fakta" in q:
                st.success("Amida banyak ditemukan dalam protein.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Amida di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Amida adalah turunan dari asam karboksilat dengan gugus amina.")
        if "protein" in q:
            if "kepolaran" in q:
                st.success("Protein bersifat amfipatik, mengandung bagian polar dan nonpolar.")
            elif "rumus" in q or "gugus" in q:
                st.success("Protein tersusun dari rantai panjang asam amino.")
            elif "titik" in q:
                st.success("Titik didih protein tidak relevan karena denaturasi terjadi sebelum menguap.")
            elif "fakta" in q:
                st.success("Protein berperan vital dalam struktur sel dan fungsi biologis.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Protein di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Protein adalah polimer alami yang tersusun dari asam amino.")
        if "karbohidrat" in q:
            if "kepolaran" in q:
                st.success("Karbohidrat sangat polar karena banyak mengandung gugus hidroksil.")
            elif "rumus" in q or "gugus" in q:
                st.success("Rumus umum karbohidrat: (CH₂O)n.")
            elif "titik" in q:
                st.success("Karbohidrat tidak memiliki titik didih pasti karena terurai sebelum menguap.")
            elif "fakta" in q:
                st.success("Karbohidrat berfungsi sebagai sumber energi utama.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Karbohidrat di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Karbohidrat adalah senyawa organik yang terdiri dari C, H, dan O.")
        if "lemak" in q or "minyak" in q:
            if "kepolaran" in q:
                st.success("Lemak dan minyak bersifat nonpolar dan tidak larut dalam air.")
            elif "rumus" in q or "gugus" in q:
                st.success("Lemak dan minyak adalah ester dari gliserol dan asam lemak.")
            elif "titik" in q:
                st.success("Titik didih trigliserida sangat tinggi, tetapi mudah rusak saat dipanaskan.")
            elif "fakta" in q:
                st.success("Lemak jenuh biasanya padat pada suhu ruang, sedangkan minyak tak jenuh cair.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Lemak dan Minyak di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Lemak dan minyak adalah bagian dari kelompok lipid.")
        if "benzena" in q:
            if "kepolaran" in q:
                st.success("Benzena bersifat nonpolar dan tidak larut dalam air.")
            elif "rumus" in q or "gugus" in q:
                st.success("Rumus benzena: C₆H₆.")
            elif "titik" in q:
                st.success("Titik didih benzena: 80,1 °C.")
            elif "fakta" in q:
                st.success("Benzena adalah senyawa hidrokarbon aromatik paling sederhana.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Benzena di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Benzena adalah senyawa aromatik dengan struktur cincin.")
        if "alkil halida" in q:
            if "kepolaran" in q:
                st.success("Alkil halida bersifat polar karena perbedaan elektronegativitas antara C dan halogen.")
            elif "rumus" in q or "gugus" in q:
                st.success("Rumus umum alkil halida: R–X, di mana X adalah halogen.")
            elif "titik" in q:
                st.success("Titik didih alkil halida lebih tinggi dari alkana dengan jumlah karbon setara.")
            elif "fakta" in q:
                st.success("Alkil halida digunakan dalam industri dan sebagai pelarut.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Alkil Halida di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Alkil halida adalah senyawa organik yang terbentuk dari alkana dengan menggantikan atom H dengan halogen.")
        if "nitro" in q:
            if "kepolaran" in q:
                st.success("Senyawa nitro sangat polar karena gugus nitro (–NO₂).")
            elif "rumus" in q or "gugus" in q:
                st.success("Gugus fungsi nitro: –NO₂.")
            elif "titik" in q:
                st.success("Titik didih nitro umumnya tinggi karena gaya tarik dipol-dipol.")
            elif "fakta" in q:
                st.success("Senyawa nitro penting dalam bahan peledak dan sintesis kimia.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Nitro di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Senyawa nitro adalah senyawa organik yang mengandung gugus nitro.")
        if "nitril" in q:
            if "kepolaran" in q:
                st.success("Nitril sangat polar karena ikatan rangkap tiga C≡N.")
            elif "rumus" in q or "gugus" in q:
                st.success("Gugus fungsi nitril: –C≡N.")
            elif "titik" in q:
                st.success("Titik didih nitril lebih tinggi dari alkana karena interaksi dipol-dipol.")
            elif "fakta" in q:
                st.success("Nitril sering digunakan sebagai bahan antara dalam sintesis senyawa.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Nitril di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Nitril adalah senyawa organik yang mengandung gugus sianida.")
        if "ester" in q:
            if "kepolaran" in q:
                st.success("Ester agak polar, tetapi tidak membentuk ikatan hidrogen antar molekul.")
            elif "rumus" in q or "gugus" in q:
                st.success("Gugus fungsi ester: R–COOR'.")
            elif "titik" in q:
                st.success("Titik didih ester lebih rendah daripada asam karboksilat.")
            elif "fakta" in q:
                st.success("Ester sering ditemukan dalam aroma buah dan minyak esensial.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Ester di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Ester adalah senyawa turunan asam karboksilat.")
        if "asam halida" in q:
            if "kepolaran" in q:
                st.success("Asam halida sangat polar karena gugus karbonil dan halogen.")
            elif "rumus" in q or "gugus" in q:
                st.success("Rumus umum asam halida: R–COX, di mana X adalah halogen.")
            elif "titik" in q:
                st.success("Titik didih asam halida lebih rendah daripada asam karboksilat.")
            elif "fakta" in q:
                st.success("Asam halida sangat reaktif dan digunakan dalam sintesis.")
            elif "video" in q:
                st.success("🔗 [Tonton Penjelasan Asam Halida di YouTube](https://www.youtube.com/watch?v=2CK7zTJdXXo)")
            else:
                st.info("Asam halida adalah turunan dari asam karboksilat.")
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
elif st.session_state.page == 'nitril':
    show_nitril()
elif st.session_state.page == 'aldehida':
    show_aldehida()
elif st.session_state.page == 'nitro':
    show_nitro()
elif st.session_state.page == 'keton':
    show_keton()
elif st.session_state.page == 'asam halida':
    show_asam_halida()
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
elif st.session_state.page == 'asam karboksilat':
    show_asam_karboksilat()
elif st.session_state.page == 'amida':
    show_amida()
elif st.session_state.page == 'protein':
    show_protein()
elif st.session_state.page == 'lemak dan minyak':
    show_lemak_dan_minyak()
elif st.session_state.page == 'eter':
    show_eter()
elif st.session_state.page == 'karbohidrat':
    show_karbohidrat()
