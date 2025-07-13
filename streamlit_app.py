import streamlit as st
import random
import time

# Data senyawa organik
compounds = {
    "Ethanol": {
        "titik_didih": "78.37 °C",
        "titik_leleh": "-114.1 °C",
        "kepolaran": "Polar",
        "rumus_kimia": "C2H5OH",
        "fun_fact": "Ethanol is the type of alcohol found in alcoholic beverages.",
        "ikatan_kimia": "Terdapat ikatan tunggal C-C dan C-O.",
        "link_youtube": "https://www.youtube.com/watch?v=3g1g1g1g1g1",
        "rating": 0,
        "reviews": []
    },
    "Benzena": {
        "titik_didih": "80.1 °C",
        "titik_leleh": "5.5 °C",
        "kepolaran": "Non-polar",
        "rumus_kimia": "C6H6",
        "fun_fact": "Benzene is a natural constituent of crude oil.",
        "ikatan_kimia": "Terdapat ikatan rangkap C=C.",
        "link_youtube": "https://www.youtube.com/watch?v=4g4g4g4g4g4",
        "rating": 0,
        "reviews": []
    },
    "Metana": {
        "titik_didih": "-161.5 °C",
        "titik_leleh": "-182.5 °C",
        "kepolaran": "Non-polar",
        "rumus_kimia": "CH4",
        "fun_fact": "Metana adalah komponen utama gas alam.",
        "ikatan_kimia": "Terdapat ikatan tunggal C-H.",
        "link_youtube": "https://www.youtube.com/watch?v=5h5h5h5h5h5",
        "rating": 0,
        "reviews": []
    }
}

# Fungsi untuk chatbot sederhana
def chatbot_response(user_input):
    greetings = ["halo", "hai", "hi", "hello"]
    compound_keywords = ["senyawa", "compound", "kimia"]
    
    user_input = user_input.lower()
    
    if any(word in user_input for word in greetings):
        return "Halo! Selamat datang di O-Kimiaku. Ada yang bisa saya bantu?"
    elif any(word in user_input for word in compound_keywords):
        return f"Anda dapat melihat berbagai senyawa organik di menu utama. Saat ini tersedia: {', '.join(compounds.keys())}"
    elif "terima kasih" in user_input:
        return "Sama-sama! Senang bisa membantu."
    else:
        return "Maaf, saya tidak mengerti pertanyaan Anda. Silakan tanyakan tentang senyawa organik atau fitur aplikasi ini."

# Fungsi untuk menghitung rating rata-rata
def calculate_average_rating(compound_name):
    reviews = compounds[compound_name]["reviews"]
    if not reviews:
        return 0
    return sum(review['rating'] for review in reviews) / len(reviews)

# Layout utama
def main():
    st.set_page_config(page_title="O-Kimiaku", page_icon="🧪", layout="wide")
    
    # Sidebar untuk navigasi
    st.sidebar.title("Navigasi")
    app_mode = st.sidebar.radio("Pilih Menu:", ["Beranda", "Senyawa Organik", "Rating & Ulasan", "ChatBot"])
    
    if app_mode == "Beranda":
        show_home()
    elif app_mode == "Senyawa Organik":
        show_compounds()
    elif app_mode == "Rating & Ulasan":
        show_ratings()
    elif app_mode == "ChatBot":
        show_chatbot()

# Halaman Beranda
def show_home():
    st.title("Selamat Datang di O-Kimiaku 🧪")
    st.write("""
    Aplikasi ini membantu Anda mempelajari sifat-sifat senyawa organik seperti:
    - Titik didih dan titik leleh
    - Kepolaran
    - Rumus kimia
    - Fakta menarik
    - Ikatan kimia
    """)
    
    st.image("https://placehold.co/800x400?text=Ilustrasi+Senyawa+Organik", 
             caption="Berbagai senyawa organik dan strukturnya")
    
    st.subheader("Senyawa Tersedia")
    cols = st.columns(3)
    for i, compound in enumerate(compounds.keys()):
        with cols[i % 3]:
            st.image(f"https://placehold.co/200x100?text={compound}",
                    caption=f"{compound} - {compounds[compound]['rumus_kimia']}",
                    width=200)
            st.write(f"**Titik Didih:** {compounds[compound]['titik_didih']}")

# Halaman Senyawa Organik
def show_compounds():
    st.title("Senyawa Organik")
    
    # Pilih senyawa
    compound_name = st.selectbox("Pilih Senyawa Organik:", list(compounds.keys()))
    
    # Tampilkan informasi senyawa
    compound_info = compounds[compound_name]
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(f"https://placehold.co/400x200?text=Struktur+{compound_name}", 
                caption=f"Struktur {compound_name}")
    
    with col2:
        st.subheader(compound_name)
        st.write("**Titik Didih:**", compound_info["titik_didih"])
        st.write("**Titik Leleh:**", compound_info["titik_leleh"])
        st.write("**Kepolaran:**", compound_info["kepolaran"])
        st.write("**Rumus Kimia:**", compound_info["rumus_kimia"])
        st.write("**Fun Fact:**", compound_info["fun_fact"])
        st.write("**Ikatan Kimia:**", compound_info["ikatan_kimia"])
        
        if st.button("Tonton Video Penjelasan"):
            st.markdown(f"[Tonton Video di YouTube]({compound_info['link_youtube']})", 
                       unsafe_allow_html=True)

# Halaman Rating & Ulasan
def show_ratings():
    st.title("Rating & Ulasan")
    
    # Pilih senyawa untuk diulas
    compound_name = st.selectbox("Pilih Senyawa untuk Memberi Rating:", list(compounds.keys()))
    
    # Tampilkan rating saat ini
    avg_rating = calculate_average_rating(compound_name)
    st.subheader(f"Rating untuk {compound_name}")
    st.write(f"⭐ Rating Rata-rata: {avg_rating:.1f}/5")
    
    # Form untuk kirim ulasan
    with st.form(key='review_form'):
        st.write("Tambahkan Ulasan Anda")
        user_rating = st.slider("Rating (1-5)", 1, 5, 3)
        user_review = st.text_area("Ulasan Anda")
        submitted = st.form_submit_button("Kirim")
        
        if submitted:
            compounds[compound_name]["reviews"].append({
                "rating": user_rating,
                "review": user_review
            })
            st.success("Terima kasih atas ulasan Anda!")
    
    # Tampilkan ulasan yang ada
    st.subheader("Ulasan Pengguna")
    reviews = compounds[compound_name]["reviews"]
    
    if not reviews:
        st.write("Belum ada ulasan untuk senyawa ini.")
    else:
        for i, rev in enumerate(reviews):
            st.write(f"**Ulasan {i+1}**: ⭐ {rev['rating']}/5")
            st.write(rev["review"])
            st.divider()

# Halaman ChatBot
def show_chatbot():
    st.title("ChatBot O-Kimiaku")
    st.write("ChatBot sederhana untuk membantu Anda menjelajahi aplikasi ini.")
    
    # Inisialisasi chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Input pengguna
    user_input = st.text_input("Tulis pesan Anda:")
    
    if user_input:
        # Tambahkan pesan pengguna ke history
        st.session_state.chat_history.append({"sender": "user", "message": user_input})
        
        # Dapatkan respon chatbot
        bot_response = chatbot_response(user_input)
        
        # Simulasi delay untuk tampilan lebih natural
        with st.spinner("Mengetik..."):
            time.sleep(0.5)
            st.session_state.chat_history.append({"sender": "bot", "message": bot_response})
    
    # Tampilkan chat history
    for msg in st.session_state.chat_history:
        if msg["sender"] == "user":
            st.chat_message("user").write(msg["message"])
        else:
            st.chat_message("assistant").write(msg["message"])

if __name__ == "__main__":
    main()

   
