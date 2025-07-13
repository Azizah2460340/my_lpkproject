<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>O-Kimiaku - Aplikasi Pembelajaran Kimia</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
        
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f8fafc;
            transition: all 0.3s ease;
        }
        
        .sidebar {
            width: 300px;
            transform: translateX(-100%);
            transition: transform 0.3s ease;
        }
        
        .sidebar.active {
            transform: translateX(0);
        }
        
        .overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(0,0,0,0.5);
            z-index: 10;
        }
        
        .overlay.active {
            display: block;
        }
        
        .compound-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }
        
        .compound-info {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease;
        }
        
        .compound-info.active {
            max-height: 500px;
        }
        
        .rating-stars {
            direction: rtl;
            unicode-bidi: bidi-override;
        }
        
        .rating-stars input {
            display: none;
        }
        
        .rating-stars label {
            color: #d1d5db;
            font-size: 2rem;
            padding: 0 5px;
            cursor: pointer;
        }
        
        .rating-stars input:checked ~ label,
        .rating-stars label:hover,
        .rating-stars label:hover ~ label {
            color: #f59e0b;
        }
        
        .chat-message {
            max-width: 70%;
            padding: 0.75rem;
            border-radius: 1rem;
            margin-bottom: 0.5rem;
        }
        
        .user-message {
            background-color: #3b82f6;
            color: white;
            margin-left: auto;
            border-bottom-right-radius: 0.25rem;
        }
        
        .bot-message {
            background-color: #e5e7eb;
            margin-right: auto;
            border-bottom-left-radius: 0.25rem;
        }
        
        @media (max-width: 768px) {
            .sidebar {
                width: 280px;
            }
        }
    </style>
</head>
<body class="min-h-screen">
    <nav class="bg-indigo-600 text-white p-4 shadow-md flex justify-between items-center fixed w-full z-20">
        <button id="menuBtn" class="text-white focus:outline-none">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
        </button>
        <h1 class="text-xl font-bold">O-Kimiaku</h1>
        <div class="w-6"></div>
    </nav>

    <div class="overlay" id="overlay"></div>

    <aside class="sidebar bg-white fixed h-full shadow-lg z-30 p-4" id="sidebar">
        <div class="flex justify-between items-center mb-6">
            <h2 class="text-xl font-bold text-indigo-600">Menu</h2>
            <button id="closeMenuBtn" class="text-gray-500 focus:outline-none">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
            </button>
        </div>
        
        <nav>
            <ul class="space-y-2">
                <li>
                    <button id="homeBtn" class="w-full text-left px-4 py-2 rounded-lg bg-indigo-100 text-indigo-700 font-medium">
                        Beranda
                    </button>
                </li>
                <li>
                    <button id="chatbotBtn" class="w-full text-left px-4 py-2 rounded-lg hover:bg-gray-100">
                        Chatbot Kimia
                    </button>
                </li>
                <li>
                    <button id="aboutBtn" class="w-full text-left px-4 py-2 rounded-lg hover:bg-gray-100">
                        Tentang Kami
                    </button>
                </li>
            </ul>
        </nav>
    </aside>

    <main class="pt-16 pb-20 px-4" id="mainContent">
        <!-- Beranda Section -->
        <section id="homeSection">
            <div class="container mx-auto py-8">
                <div class="bg-white rounded-xl shadow-md overflow-hidden mb-8">
                    <div class="p-6 md:p-8">
                        <div class="flex flex-col items-center text-center mb-6">
                            <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/234f84c5-c840-4614-adf0-57fa840f39dd.png" alt="Ilustrasi laboratorium kimia modern dengan peralatan seperti tabung reaksi, gelas kimia, dan mikroskop" class="rounded-lg w-full md:w-2/3 mb-6" />
                            <h2 class="text-3xl font-bold text-indigo-600 mb-4">Selamat Datang di O-Kimiaku</h2>
                            <p class="text-gray-600 max-w-3xl">
                                O-Kimiaku adalah aplikasi pembelajaran kimia yang menyediakan informasi lengkap tentang berbagai senyawa kimia. Temukan tatanama, titik didih, titik leleh, kepolaran, rumus kimia, dan fakta menarik dari berbagai senyawa kimia dalam satu aplikasi.
                            </p>
                        </div>
                    </div>
                </div>

                <h2 class="text-2xl font-bold text-gray-800 mb-6">Pilih Senyawa Kimia</h2>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-10">
                    <!-- Alkohol Card -->
                    <div class="compound-card bg-white rounded-xl shadow-md overflow-hidden transition duration-300">
                        <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/7787b634-74f3-4a5e-ac26-eb382119a766.png" alt="Struktur molekul etanol dengan model bola-dan-tongkat menunjukkan atom karbon, hidrogen, dan gugus hidroksil" class="w-full h-48 object-cover" />
                        <div class="p-5">
                            <h3 class="text-xl font-bold text-gray-800 mb-2">Alkohol</h3>
                            <p class="text-gray-600 mb-4">Senyawa organik dengan gugus fungsi hidroksil (-OH) yang terikat pada atom karbon.</p>
                            <button class="show-info-btn w-full py-2 px-4 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg transition" data-compound="alcohol">
                                Pelajari Lebih Lanjut
                            </button>
                        </div>
                        <div class="compound-info px-5 pb-5">
                            <div class="border-t pt-4">
                                <h4 class="font-bold text-gray-800 mb-2">Informasi Lengkap:</h4>
                                <ul class="space-y-2">
                                    <li><span class="font-medium">Tatanama:</span> Nama alkohol diakhiri dengan -ol</li>
                                    <li><span class="font-medium">Titik Didih:</span> Relatif tinggi karena ikatan hidrogen antarmolekul</li>
                                    <li><span class="font-medium">Titik Leleh:</span> Bervariasi tergantung panjang rantai karbon</li>
                                    <li><span class="font-medium">Kepolaran:</span> Polar karena adanya gugus -OH</li>
                                    <li><span class="font-medium">Rumus Umum:</span> R-OH (R = gugus alkil)</li>
                                    <li><span class="font-medium">Contoh:</span> Etanol (C₂H₅OH) yang terdapat dalam minuman beralkohol</li>
                                </ul>
                                <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank" class="inline-block mt-4 text-indigo-600 hover:text-indigo-800 font-medium">
                                    Pelajari di YouTube →
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Asam Karboksilat Card -->
                    <div class="compound-card bg-white rounded-xl shadow-md overflow-hidden transition duration-300">
                        <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/af0cdf42-16c0-44db-a9ba-f4bfd0dde814.png" alt="Struktur molekul asam asetat dengan gugus karboksil yang ditonjolkan dalam warna berbeda" class="w-full h-48 object-cover" />
                        <div class="p-5">
                            <h3 class="text-xl font-bold text-gray-800 mb-2">Asam Karboksilat</h3>
                            <p class="text-gray-600 mb-4">Senyawa dengan gugus karboksil (-COOH) yang bersifat asam lemah.</p>
                            <button class="show-info-btn w-full py-2 px-4 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg transition" data-compound="carboxylic">
                                Pelajari Lebih Lanjut
                            </button>
                        </div>
                        <div class="compound-info px-5 pb-5">
                            <div class="border-t pt-4">
                                <h4 class="font-bold text-gray-800 mb-2">Informasi Lengkap:</h4>
                                <ul class="space-y-2">
                                    <li><span class="font-medium">Tatanama:</span> Nama diawali dengan 'asam' dan diakhiri dengan '-oat'</li>
                                    <li><span class="font-medium">Titik Didih:</span> Sangat tinggi karena ikatan hidrogen kuat</li>
                                    <li><span class="font-medium">Titik Leleh:</span> Meningkat seiring jumlah atom karbon</li>
                                    <li><span class="font-medium">Kepolaran:</span> Sangat polar</li>
                                    <li><span class="font-medium">Rumus Umum:</span> R-COOH</li>
                                    <li><span class="font-medium">Contoh:</span> Asam asetat (CH₃COOH) dalam cuka</li>
                                </ul>
                                <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank" class="inline-block mt-4 text-indigo-600 hover:text-indigo-800 font-medium">
                                    Pelajari di YouTube →
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Ester Card -->
                    <div class="compound-card bg-white rounded-xl shadow-md overflow-hidden transition duration-300">
                        <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/2ad2b1e8-636d-4d55-92fd-5d9c529ea955.png" alt="Ilustrasi molekul ester yang digunakan sebagai penyedap rasa buatan dalam makanan" class="w-full h-48 object-cover" />
                        <div class="p-5">
                            <h3 class="text-xl font-bold text-gray-800 mb-2">Ester</h3>
                            <p class="text-gray-600 mb-4">Senyawa dengan gugus -COOR yang memiliki aroma khas.</p>
                            <button class="show-info-btn w-full py-2 px-4 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg transition" data-compound="ester">
                                Pelajari Lebih Lanjut
                            </button>
                        </div>
                        <div class="compound-info px-5 pb-5">
                            <div class="border-t pt-4">
                                <h4 class="font-bold text-gray-800 mb-2">Informasi Lengkap:</h4>
                                <ul class="space-y-2">
                                    <li><span class="font-medium">Tatanama:</span> Nama alkil dari alkohol + nama akhiran asam dengan '-oat'</li>
                                    <li><span class="font-medium">Titik Didih:</span> Lebih rendah dari asam dengan berat molekul sebanding</li>
                                    <li><span class="font-medium">Titik Leleh:</span> Bervariasi tergantung panjang rantai</li>
                                    <li><span class="font-medium">Kepolaran:</span> Polar namun tidak dapat membentuk ikatan hidrogen sesamanya</li>
                                    <li><span class="font-medium">Rumus Umum:</span> R-COO-R'</li>
                                    <li><span class="font-medium">Contoh:</span> Etil asetat (CH₃COOC₂H₅) dengan aroma buah</li>
                                </ul>
                                <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank" class="inline-block mt-4 text-indigo-600 hover:text-indigo-800 font-medium">
                                    Pelajari di YouTube →
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Chatbot Section (hidden by default) -->
        <section id="chatbotSection" class="hidden">
            <div class="container mx-auto py-8 max-w-2xl">
                <div class="bg-white rounded-xl shadow-md overflow-hidden">
                    <div class="bg-indigo-600 text-white p-4">
                        <h2 class="text-xl font-bold">Chatbot Kimia O-Kimiaku</h2>
                        <p class="text-sm opacity-90">Tanya apapun tentang senyawa kimia di sini</p>
                    </div>
                    
                    <div class="p-4 bg-gray-50 h-96 overflow-y-auto" id="chatArea">
                        <div class="chat-message bot-message">
                            <p class="text-sm">Halo! Saya Kimi, asisten kimia di O-Kimiaku. Saya bisa membantu Anda memahami berbagai konsep tentang senyawa kimia. Apa yang ingin Anda ketahui?</p>
                        </div>
                    </div>
                    
                    <div class="p-4 bg-white border-t">
                        <div class="flex">
                            <input type="text" placeholder="Tulis pertanyaan Anda..." class="flex-grow px-4 py-2 rounded-l-lg border focus:outline-none focus:ring-2 focus:ring-indigo-500" id="userInput" />
                            <button class="bg-indigo-600 text-white px-4 py-2 rounded-r-lg hover:bg-indigo-700 transition" id="sendBtn">
                                Kirim
                            </button>
                        </div>
                        <div class="mt-3 flex items-center">
                            <span class="text-gray-500 text-sm mr-3">Coba tanya:</span>
                            <div class="space-x-2">
                                <button class="suggested-question text-xs px-3 py-1 bg-gray-200 text-gray-700 rounded-full hover:bg-gray-300">Apa itu alkohol?</button>
                                <button class="suggested-question text-xs px-3 py-1 bg-gray-200 text-gray-700 rounded-full hover:bg-gray-300">Bagaimana kepolaran ester?</button>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="mt-6 bg-white rounded-xl shadow-md overflow-hidden">
                    <div class="p-4 bg-indigo-600 text-white">
                        <h2 class="text-xl font-bold">Daftar Istilah Kimia</h2>
                    </div>
                    <div class="p-4">
                        <div class="space-y-3">
                            <div class="p-3 bg-indigo-50 rounded-lg">
                                <h3 class="font-bold text-indigo-700">Alkohol</h3>
                                <p class="text-sm text-gray-600">Senyawa organik dengan gugus hidroksil (-OH) yang terikat pada atom karbon jenuh.</p>
                            </div>
                            <div class="p-3 bg-indigo-50 rounded-lg">
                                <h3 class="font-bold text-indigo-700">Titik Didih</h3>
                                <p class="text-sm text-gray-600">Suhu ketika tekanan uap cairan sama dengan tekanan luar.</p>
                            </div>
                            <div class="p-3 bg-indigo-50 rounded-lg">
                                <h3 class="font-bold text-indigo-700">Kepolaran</h3>
                                <p class="text-sm text-gray-600">Distribusi muayan listrik yang tidak merata dalam molekul.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- About Section (hidden by default) -->
        <section id="aboutSection" class="hidden">
            <div class="container mx-auto py-8">
                <div class="bg-white rounded-xl shadow-md overflow-hidden">
                    <div class="p-6 md:p-8">
                        <div class="flex flex-col items-center text-center mb-8">
                            <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/2714e4c8-a83a-422b-b18f-e5851ed73028.png" alt="Foto tim pengembang O-Kimiaku yang terdiri dari 3 orang sedang berdiri bersama di laboratorium kimia" class="rounded-full w-32 h-32 object-cover mb-4" />
                            <h2 class="text-3xl font-bold text-indigo-600 mb-2">Tentang Kami</h2>
                            <p class="text-gray-600 max-w-2xl">
                                O-Kimiaku dikembangkan oleh tim yang berkomitmen untuk membuat pembelajaran kimia menjadi lebih mudah dan menyenangkan.
                            </p>
                        </div>
                        
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                            <div class="bg-indigo-50 rounded-xl p-6">
                                <div class="flex items-center mb-4">
                                    <div class="bg-indigo-100 p-3 rounded-full mr-4">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                                        </svg>
                                    </div>
                                    <h3 class="text-lg font-bold text-gray-800">Visi</h3>
                                </div>
                                <p class="text-gray-600 text-sm">
                                    Menjadikan kimia sebagai ilmu yang mudah dipahami dan menyenangkan untuk dipelajari oleh semua kalangan.
                                </p>
                            </div>
                            
                            <div class="bg-indigo-50 rounded-xl p-6">
                                <div class="flex items-center mb-4">
                                    <div class="bg-indigo-100 p-3 rounded-full mr-4">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                                        </svg>
                                    </div>
                                    <h3 class="text-lg font-bold text-gray-800">Misi</h3>
                                </div>
                                <p class="text-gray-600 text-sm">
                                    Memberikan akses pembelajaran kimia yang interaktif dan komprehensif melalui teknologi digital.
                                </p>
                            </div>
                            
                            <div class="bg-indigo-50 rounded-xl p-6">
                                <div class="flex items-center mb-4">
                                    <div class="bg-indigo-100 p-3 rounded-full mr-4">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                                        </svg>
                                    </div>
                                    <h3 class="text-lg font-bold text-gray-800">Tim</h3>
                                </div>
                                <p class="text-gray-600 text-sm">
                                    Dikembangkan oleh tim yang terdiri dari ahli kimia, pengembang perangkat lunak, dan desainer yang berpengalaman.
                                </p>
                            </div>
                        </div>
                        
                        <div class="bg-indigo-50 rounded-xl p-6">
                            <h3 class="text-lg font-bold text-gray-800 mb-4">Anggota Tim</h3>
                            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                                <div class="flex items-center space-x-4 p-3 rounded-lg hover:bg-indigo-100">
                                    <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/5c1b6432-7526-4c91-934c-d9ffa9e4be55.png" alt="Foto Profil Ketua Tim - Seorang pria berkacamata dengan background laboratorium kimia" class="w-12 h-12 rounded-full object-cover" />
                                    <div>
                                        <h4 class="font-medium text-gray-800">Dr. Adi Pratama</h4>
                                        <p class="text-xs text-gray-500">Ahli Kimia Organik</p>
                                    </div>
                                </div>
                                <div class="flex items-center space-x-4 p-3 rounded-lg hover:bg-indigo-100">
                                    <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/527ff112-7153-4077-8cf6-593bf6eb480f.png" alt="Foto Profil Anggota Tim - Wanita muda dengan jas lab sedang tersenyum" class="w-12 h-12 rounded-full object-cover" />
                                    <div>
                                        <h4 class="font-medium text-gray-800">Siti Rahayu</h4>
                                        <p class="text-xs text-gray-500">Pengembang Frontend</p>
                                    </div>
                                </div>
                                <div class="flex items-center space-x-4 p-3 rounded-lg hover:bg-indigo-100">
                                    <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/a8f6858d-b87b-45dc-8ed0-758c14f0e58f.png" alt="Foto Profil Anggota Tim - Pria muda asia memegang tablet dengan tampilan kode pemrograman" class="w-12 h-12 rounded-full object-cover" />
                                    <div>
                                        <h4 class="font-medium text-gray-800">Budi Santoso</h4>
                                        <p class="text-xs text-gray-500">Pengembang Backend</p>
                                    </div>
                                </div>
                                <div class="flex items-center space-x-4 p-3 rounded-lg hover:bg-indigo-100">
                                    <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/cd63f880-828e-4e46-a010-3874bf7b4cd8.png" alt="Foto Profil Anggota Tim - Desainer wanita dengan sketsa antarmuka aplikasi di latar belakang" class="w-12 h-12 rounded-full object-cover" />
                                    <div>
                                        <h4 class="font-medium text-gray-800">Dewi Anggraeni</h4>
                                        <p class="text-xs text-gray-500">UI/UX Designer</p>
                                    </div>
                                </div>
                                <div class="flex items-center space-x-4 p-3 rounded-lg hover:bg-indigo-100">
                                    <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/8d888091-fd3a-4cf1-9641-1f40b1ad8785.png" alt="Foto Profil Anggota Tim - Pria dewasa menunjuk ke diagram struktur molekul di papan tulis" class="w-12 h-12 rounded-full object-cover" />
                                    <div>
                                        <h4 class="font-medium text-gray-800">Prof. Bambang S.</h4>
                                        <p class="text-xs text-gray-500">Koordinator Konten</p>
                                    </div>
                                </div>
                                <div class="flex items-center space-x-4 p-3 rounded-lg hover:bg-indigo-100">
                                    <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/2af8c149-b62d-4982-9d6e-3d7238b63507.png" alt="Foto Profil Anggota Tim - Mahasiswa kimia sedang mengaduk larutan dalam gelas kimia" class="w-12 h-12 rounded-full object-cover" />
                                    <div>
                                        <h4 class="font-medium text-gray-800">Rina Wijaya</h4>
                                        <p class="text-xs text-gray-500">Asisten Penelitian</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Modal Rating -->
    <div id="ratingModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 hidden">
        <div class="bg-white rounded-xl p-6 max-w-md w-full mx-4">
            <div class="flex justify-between items-center mb-4">
                <h3 class="text-xl font-bold text-gray-800">Berikan Rating Anda</h3>
                <button id="closeRatingModal" class="text-gray-500 hover:text-gray-700 focus:outline-none">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>
            </div>
            <p class="text-gray-600 mb-6">Bagaimana pengalaman Anda menggunakan O-Kimiaku?</p>
            
            <div class="mb-6 flex justify-center">
                <div class="rating-stars">
                    <input type="radio" id="star5" name="rating" value="5" />
                    <label for="star5" title="Sangat Baik">★</label>
                    <input type="radio" id="star4" name="rating" value="4" />
                    <label for="star4" title="Baik">★</label>
                    <input type="radio" id="star3" name="rating" value="3" />
                    <label for="star3" title="Cukup">★</label>
                    <input type="radio" id="star2" name="rating" value="2" />
                    <label for="star2" title="Kurang">★</label>
                    <input type="radio" id="star1" name="rating" value="1" />
                    <label for="star1" title="Buruk">★</label>
                </div>
            </div>
            
            <div class="mb-4">
                <label for="feedback" class="block text-sm font-medium text-gray-700 mb-2">Masukan (opsional)</label>
                <textarea id="feedback" rows="3" class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500" placeholder="Apa yang bisa kami tingkatkan?"></textarea>
            </div>
            
            <div class="flex justify-end space-x-3">
                <button id="cancelRating" class="px-4 py-2 text-gray-600 font-medium rounded-lg hover:bg-gray-100">Nanti</button>
                <button id="submitRating" class="px-4 py-2 bg-indigo-600 text-white font-medium rounded-lg hover:bg-indigo-700 transition">Kirim</button>
            </div>
        </div>
    </div>

    <footer class="bg-indigo-600 text-white py-4 px-4 fixed bottom-0 w-full">
        <div class="container mx-auto flex justify-between items-center">
            <p class="text-sm">© 2023 O-Kimiaku. All rights reserved.</p>
            <button id="rateBtn" class="text-sm font-medium bg-white text-indigo-600 px-4 py-1 rounded-full hover:bg-indigo-50 transition">
                Beri Rating
            </button>
        </div>
    </footer>

    <script>
        // DOM Elements
        const menuBtn = document.getElementById('menuBtn');
        const closeMenuBtn = document.getElementById('closeMenuBtn');
        const overlay = document.getElementById('overlay');
        const sidebar = document.getElementById('sidebar');
        const homeBtn = document.getElementById('homeBtn');
        const chatbotBtn = document.getElementById('chatbotBtn');
        const aboutBtn = document.getElementById('aboutBtn');
        const homeSection = document.getElementById('homeSection');
        const chatbotSection = document.getElementById('chatbotSection');
        const aboutSection = document.getElementById('aboutSection');
        const rateBtn = document.getElementById('rateBtn');
        const ratingModal = document.getElementById('ratingModal');
        const closeRatingModal = document.getElementById('closeRatingModal');
        const cancelRating = document.getElementById('cancelRating');
        const submitRating = document.getElementById('submitRating');
        const showInfoBtns = document.querySelectorAll('.show-info-btn');
        const userInput = document.getElementById('userInput');
        const sendBtn = document.getElementById('sendBtn');
        const chatArea = document.getElementById('chatArea');
        const suggestedQuestions = document.querySelectorAll('.suggested-question');

        // Sidebar Toggle
        menuBtn.addEventListener('click', () => {
            sidebar.classList.add('active');
            overlay.classList.add('active');
        });

        closeMenuBtn.addEventListener('click', () => {
            sidebar.classList.remove('active');
            overlay.classList.remove('active');
        });

        overlay.addEventListener('click', () => {
            sidebar.classList.remove('active');
            overlay.classList.remove('active');
            ratingModal.classList.add('hidden');
        });

        // Navigation
        homeBtn.addEventListener('click', () => {
            homeSection.classList.remove('hidden');
            chatbotSection.classList.add('hidden');
            aboutSection.classList.add('hidden');
            sidebar.classList.remove('active');
            overlay.classList.remove('active');
            resetAllCompoundInfo();
        });

        chatbotBtn.addEventListener('click', () => {
            homeSection.classList.add('hidden');
            chatbotSection.classList.remove('hidden');
            aboutSection.classList.add('hidden');
            sidebar.classList.remove('active');
            overlay.classList.remove('active');
            resetAllCompoundInfo();
        });

        aboutBtn.addEventListener('click', () => {
            homeSection.classList.add('hidden');
            chatbotSection.classList.add('hidden');
            aboutSection.classList.remove('hidden');
            sidebar.classList.remove('active');
            overlay.classList.remove('active');
            resetAllCompoundInfo();
        });

        // Compound Info Toggle
        showInfoBtns.forEach(btn => {
            btn.addEventListener('click', function() {
                const infoSection = this.closest('.compound-card').querySelector('.compound-info');
                
                // Close all first
                resetAllCompoundInfo();
                
                // Toggle current
                infoSection.classList.toggle('active');
                
                // Change button text
                if (infoSection.classList.contains('active')) {
                    this.textContent = 'Sembunyikan';
                } else {
                    this.textContent = 'Pelajari Lebih Lanjut';
                }
            });
        });

        function resetAllCompoundInfo() {
            document.querySelectorAll('.compound-info').forEach(info => {
                info.classList.remove('active');
                const btn = info.closest('.compound-card').querySelector('.show-info-btn');
                btn.textContent = 'Pelajari Lebih Lanjut';
            });
        }

        // Rating Modal
        rateBtn.addEventListener('click', () => {
            ratingModal.classList.remove('hidden');
            overlay.classList.add('active');
        });

        closeRatingModal.addEventListener('click', () => {
            ratingModal.classList.add('hidden');
            overlay.classList.remove('active');
        });

        cancelRating.addEventListener('click', () => {
            ratingModal.classList.add('hidden');
            overlay.classList.remove('active');
        });

        submitRating.addEventListener('click', () => {
            const rating = document.querySelector('input[name="rating"]:checked');
            const feedback = document.getElementById('feedback').value;
            
            if (!rating) {
                alert('Silahkan berikan rating terlebih dahulu');
                return;
            }
            
            // In a real app, you would send this to a server
            console.log('Rating:', rating.value);
            console.log('Feedback:', feedback);
            
            alert('Terima kasih atas rating dan masukan Anda!');
            ratingModal.classList.add('hidden');
            overlay.classList.remove('active');
            
            // Reset form
            document.getElementById('feedback').value = '';
            rating.checked = false;
        });

        // Simple Chatbot
        sendBtn.addEventListener('click', sendMessage);
        userInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });

        // Suggested questions
        suggestedQuestions.forEach(question => {
            question.addEventListener('click', function() {
                userInput.value = this.textContent;
                sendMessage();
            });
        });

        function sendMessage() {
            const message = userInput.value.trim();
            if (!message) return;
            
            // Add user message
            const userMessageDiv = document.createElement('div');
            userMessageDiv.className = 'chat-message user-message';
            userMessageDiv.innerHTML = `<p class="text-sm">${message}</p>`;
            chatArea.appendChild(userMessageDiv);
            
            // Clear input
            userInput.value = '';
            
            // Scroll to bottom
            chatArea.scrollTop = chatArea.scrollHeight;
            
            // Bot response
            setTimeout(() => {
                let response = '';
                
                if (message.toLowerCase().includes('alkohol')) {
                    response = `Alkohol adalah senyawa organik yang mengandung gugus hidroksil (-OH) yang terikat pada atom karbon jenuh. Contoh paling umum adalah etanol (C₂H₅OH) yang terdapat dalam minuman beralkohol. Alkohol memiliki sifat fisik seperti titik didih yang relatif tinggi karena adanya ikatan hidrogen.`;
                } 
                else if (message.toLowerCase().includes('ester')) {
                    response = `Ester adalah senyawa organik dengan struktur R-COO-R' yang terbentuk dari reaksi esterifikasi antara asam karboksilat dan alkohol. Ester banyak digunakan sebagai penyedap rasa buatan karena memiliki aroma yang khas, misalnya etil butirat yang memiliki aroma buah nanas.`;
                } 
                else if (message.toLowerCase().includes('titik didih')) {
                    response = `Titik didih adalah suhu ketika tekanan uap suatu zat cair sama dengan tekanan eksternal yang mengenai permukaan zat cair tersebut. Dalam kimia organik, titik didih dipengaruhi oleh berat molekul dan kekuatan gaya antarmolekul seperti ikatan hidrogen. Sebagai contoh, alkohol memiliki titik didih yang lebih tinggi daripada alkana dengan berat molekul serupa karena mampu membentuk ikatan hidrogen.`;
                } 
                else if (message.toLowerCase().includes('kepolaran')) {
                    response = `Kepolaran senyawa kimia mengacu pada distribusi muatan listrik yang tidak merata dalam molekul. Molekul polar memiliki momen dipol karena perbedaan keelektronegatifan atom-atom yang berikatan. Contohnya, air (H₂O) sangat polar karena bentuknya yang bengkok dan perbedaan keelektronegatifan antara oksigen dan hidrogen.`;
                } 
                else {
                    response = `Maaf, saya tidak sepenuhnya memahami pertanyaan Anda. Bisakah Anda memperjelas pertanyaan tentang kimia yang ingin Anda ketahui? Sebagai contoh, Anda bisa menanyakan tentang sifat-sifat alkohol, tatanama senyawa, atau prinsip kesetimbangan kimia.`;
                }
                
                const botMessageDiv = document.createElement('div');
                botMessageDiv.className = 'chat-message bot-message';
                botMessageDiv.innerHTML = `<p class="text-sm">${response}</p>`;
                chatArea.appendChild(botMessageDiv);
                
                // Scroll to bottom
                chatArea.scrollTop = chatArea.scrollHeight;
            }, 500);
        }
    </script>
</body>
</html>


