import streamlit as st

# Data senyawa organik
compounds = {
    "Metana (CH₄)": {
        "image": "https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/35722f84-d25c-4b0f-aff6-315b3489cb0f.png",
        "description": "Metana adalah senyawa organik paling sederhana dengan rumus CH₄. Gas ini tidak berwarna dan mudah terbakar.",
        "rating": 0
    },
    "Etanol (C₂H₅OH)": {
        "image": "https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/247d91ad-1469-4b69-998e-5ff78529746f.png",
        "description": "Etanol adalah alkohol yang biasa digunakan dalam minuman beralkohol dan sebagai disinfektan.",
        "rating": 0
    },
    "Glukosa (C₆H₁₂O₆)": {
        "image": "https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/a03a31cb-4a07-442e-af49-e7d029d75a4b.png",
        "description": "Glukosa adalah gula sederhana yang merupakan sumber energi utama bagi tubuh manusia.",
        "rating": 0
    }
}

# Layout utama
def main():
    st.set_page_config(page_title="O-Kimiaku", page_icon="🧪", layout="wide")

    # Sidebar untuk navigasi
    st.sidebar.title("Menu")
    menu_options = ["Beranda", "Rating", "Chatbot", "About Us"]
    choice = st.sidebar.selectbox("Pilih Menu", menu_options)

    if choice == "Beranda":
        show_home()
    elif choice == "Rating":
        show_rating()
    elif choice == "Chatbot":
        show_chatbot()
    elif choice == "About Us":
        show_about_us()

# Halaman Beranda
def show_home():
    st.markdown(
        """
        <style>
        .background {
            background-color: #f0f8ff;
            background-image: linear-gradient(to right, #ff7e5f, #feb47b);
            padding: 20px;
            border-radius: 10px;
        }
        </style>
        """, unsafe_allow_html=True
    )
    
    st.title("Selamat datang di Aplikasi O-Kimiaku")
    st.write("Mari eksplorasi dunia senyawa organik bersama kami!")

    for compound_name, compound_info in compounds.items():
        st.subheader(compound_name)
        st.image(compound_info["image"], use_column_width=True)
        st.write(compound_info["description"])

        # Star rating
        rating = st.radio(f"Beri rating untuk {compound_name}:", options=[1, 2, 3, 4, 5], index=0, key=compound_name)
        if st.button(f"Kirim rating untuk {compound_name}"):
            compound_info["rating"] = rating
            st.success(f"Terima kasih! Anda memberi rating {rating} bintang untuk {compound_name}.")

# Halaman Rating
def show_rating():
    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.selectbox("Pilih rating bintang:", options=[1, 2, 3, 4, 5])
    if selected is not None:
        st.markdown(f"You selected {sentiment_mapping[selected - 1]} star(s).")

# Halaman Chatbot
def show_chatbot():
    st.title("Chatbot O-Kimiaku")
    user_input = st.text_input("Tanya tentang senyawa organik:")
    if user_input:
        st.write(f"Anda bertanya: {user_input}")
        # Simulate a response
        st.write("Bot: Maaf, saya tidak mengerti pertanyaan Anda.")

# Halaman About Us
def show_about_us():
    st.title("Tentang Kami")
    st.write("""
    Aplikasi O-Kimiaku dikembangkan oleh tim pengembang yang berkomitmen untuk memberikan informasi yang akurat dan menarik tentang senyawa organik. 
    Kami percaya bahwa pemahaman tentang kimia sangat penting dalam kehidupan sehari-hari dan ingin membuatnya lebih mudah diakses oleh semua orang.
    
    **Tim Pengembang:**
    - Nama 1: Pengembang Utama
    - Nama 2: Desainer UI/UX
    - Nama 3: Analis Data
    """)

if __name__ == "__main__":
    main()
