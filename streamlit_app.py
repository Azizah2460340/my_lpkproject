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
    reviews = compounds[compound_name].get("reviews", [])
    if not reviews:
        return 0
    return sum(review['rating'] for review in reviews) / len(reviews)

# Layout utama
def main():
    st.set_page_config(page_title="O-Kimiaku", page_icon="🧪", layout="wide")
    
    # Inisialisasi session state untuk halaman aktif
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "Beranda"
    
    # Sidebar untuk navigasi minimalis
    with st.sidebar:
        st.title("O-Kimiaku")
        
        # Membuat navigasi tanpa radio button
        if st.button("Beranda", use_container_width=True):
            st.session_state.current_page = "Beranda"
        if st.button("Rating", use_container_width=True):
            st.session_state.current_page = "Rating"
        if st.button("ChatBot", use_container_width=True):
            st.session_state.current_page = "ChatBot"
    
    # Render halaman berdasarkan state
    if st.session_state.current_page == "Beranda":
        show_home()
    elif st.session_state.current_page == "Rating":
        show_ratings()
    elif st.session_state.current_page == "ChatBot":
        show_chatbot()

# Halaman Beranda
def show_home():
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.image("https://placehold.co/300x200?text=O-Kimiaku+Logo", width=200)
    
    with col2:
        st.title("O-Kimiaku - Explorer Senyawa Organik")
        st.write("""
        Aplikasi ini membantu Anda mempelajari sifat-sifat senyawa organik seperti:
        - Titik didih dan titik leleh
        - Kepolaran
        - Rumus kimia
        - Fakta menarik
        - Ikatan kimia
        """)
    
    # Bagian senyawa organik yang bisa diklik
    st.subheader("Senyawa Organik Tersedia")
    
    # Menampilkan senyawa dalam bentuk card yang bisa diklik
    cols = st.columns(2)
    for i, (compound_name, compound_info) in enumerate(compounds.items()):
        with cols[i % 2]:
            with st.container(border=True):
                st.subheader(compound_name)
                st.write(f"*Rumus Kimia:* {compound_info['rumus_kimia']}")
                st.write(f"*Titik Didih:* {compound_info['titik_didih']}")
                
                if st.button(f"Lihat detail {compound_name}", key=f"btn_{compound_name}"):
                    show_compound_detail(compound_name)

# Fungsi untuk menampilkan detail senyawa
def show_compound_detail(compound_name):
    st.session_state.current_page = "CompoundDetail"
    compound_info = compounds[compound_name]
    
    st.title(compound_name)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(f"https://placehold.co/400x300?text=Struktur+{compound_name}", 
                caption=f"Struktur {compound_name}")
    
    with col2:
        st.write("*Titik Didih:*", compound_info["titik_didih"])
        st.write("*Titik Leleh:*", compound_info["titik_leleh"])
        st.write("*Kepolaran:*", compound_info["kepolaran"])
        st.write("*Rumus Kimia:*", compound_info["rumus_kimia"])
        st.write("*Fun Fact:*", compound_info["fun_fact"])
        st.write("*Ikatan Kimia:*", compound_info["ikatan_kimia"])
        
        if st.button("Tonton Video Penjelasan"):
            st.markdown(f"[Tonton Video di YouTube]({compound_info['link_youtube']})", 
                       unsafe_allow_html=True)
    
    if st.button("Kembali ke Beranda"):
        st.session_state.current_page = "Beranda"
        st.rerun()

# Halaman Rating
def show_ratings():
    st.title("Rating Senyawa")
    
    # Pilih senyawa
    compound_name = st.selectbox("Pilih Senyawa:", list(compounds.keys()))
    
    # Tampilkan rating saat ini
    avg_rating = calculate_average_rating(compound_name)
    st.subheader(f"Rating untuk {compound_name}")
    st.write(f"⭐ Rating Rata-rata: {avg_rating:.1f}/5 dari {len(compounds[compound_name].get('reviews', []))} ulasan")
    
    # Form rating sederhana
    st.subheader("Beri Rating")
    rating = st.slider("Pilih rating (1-5 bintang):", 1, 5, 3)
    
    if st.button("Submit Rating"):
        if "reviews" not in compounds[compound_name]:
            compounds[compound_name]["reviews"] = []
        
        compounds[compound_name]["reviews"].append({
            "rating": rating,
            "review": ""
        })
        st.success(f"Terima kasih! Anda memberi rating {rating} bintang untuk {compound_name}")
    
    if st.button("Kembali ke Beranda"):
        st.session_state.current_page = "Beranda"
        st.rerun()

# Halaman ChatBot
def show_chatbot():
    st.title("O-Kimiaku ChatBot")
    
    # Inisialisasi chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Input pengguna
    user_input = st.text_input("Tanya tentang senyawa organik:")
    
    if user_input:
        # Tambahkan pesan pengguna ke history
        st.session_state.chat_history.append(f"Anda: {user_input}")
        
        # Dapatkan respon chatbot
        bot_response = chatbot_response(user_input)
        
        # Simulasi delay
        with st.spinner("Mengetik..."):
            time.sleep(0.5)
            st.session_state.chat_history.append(f"Bot: {bot_response}")
    
    # Tampilkan chat history
    st.subheader("Percakapan")
    for msg in st.session_state.chat_history:
        st.write(msg)
    
    if st.button("Kembali ke Beranda"):
        st.session_state.current_page = "Beranda"
        st.rerun()

if _name_ == "_main_":
    main()
