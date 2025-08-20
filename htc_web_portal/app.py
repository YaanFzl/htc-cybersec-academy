#!/usr/bin/env python3
"""
🛡️ HTC CyberSec Academy - Web Portal
Akademi CyberSec HTC - Portal Web untuk Challenge Cybersecurity

Author: HTC Instructor Team
Version: 1.0
Purpose: Web interface untuk framework challenge cybersecurity HTC
"""

import streamlit as st
import json
import os
import datetime
import pandas as pd
import base64
from PIL import Image
import hashlib
import time

# Page config
st.set_page_config(
    page_title="🛡️ HTC CyberSec Academy",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
def load_custom_css():
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    
    .challenge-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        margin-bottom: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .success-message {
        background: linear-gradient(135deg, #c6f6d5, #9ae6b4);
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #38a169;
        color: #2d5016;
        margin: 1rem 0;
    }
    
    .error-message {
        background: linear-gradient(135deg, #fed7d7, #feb2b2);
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #e53e3e;
        color: #742a2a;
        margin: 1rem 0;
    }
    
    .badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        margin: 0.2rem;
    }
    
    .badge-web { background: #bee3f8; color: #2c5282; }
    .badge-crypto { background: #fbb6ce; color: #97266d; }
    .badge-forensic { background: #c6f6d5; color: #276749; }
    
    .student-card {
        background: #f7fafc;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        border: 1px solid #e2e8f0;
    }
    
    .leaderboard-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem;
        margin-bottom: 0.5rem;
        background: linear-gradient(135deg, #f7fafc, #edf2f7);
        border-radius: 8px;
        border-left: 4px solid #667eea;
    }
    
    .stAlert > div {
        background-color: transparent !important;
    }
    </style>
    """, unsafe_allow_html=True)

class HTCDatabase:
    def __init__(self):
        # Use relative path for better deployment compatibility
        self.db_file = os.path.join(os.path.dirname(__file__), "htc_portal_data.json")
        self.challenges = {
            "HTC-WEB-001": {
                "name": "Portal Login Vulnerable", 
                "points": 150, 
                "category": "Web Security",
                "difficulty": "Mudah",
                "flag": "HTC{sql_injection_master_indonesia_2024}",
                "description": "Bypass login portal perusahaan menggunakan SQL injection",
                "hints": [
                    "Coba karakter khusus dalam input",
                    "Pikirkan tentang bagaimana query SQL dibentuk",
                    "Gunakan OR logic untuk membuat kondisi TRUE",
                    "Payload: admin' OR '1'='1'--"
                ]
            },
            "HTC-CRYPTO-001": {
                "name": "Pesan Rahasia Profesor", 
                "points": 125, 
                "category": "Cryptography",
                "difficulty": "Mudah", 
                "flag": "HTC{caesar_cipher_master_indonesia}",
                "description": "Decode pesan Caesar cipher dari profesor HTC",
                "hints": [
                    "Ini adalah Caesar cipher klasik",
                    "Coba shift 3 terlebih dahulu",
                    "Perhatikan pola kata dalam bahasa Indonesia",
                    "Gunakan brute force 1-25 jika perlu"
                ]
            },
            "HTC-FORENSIC-001": {
                "name": "Rahasia di Balik Logo HTC", 
                "points": 200, 
                "category": "Digital Forensics",
                "difficulty": "Mudah",
                "flag": "HTC{stegsolve_master_forensics_2024}",
                "description": "Temukan pesan tersembunyi dalam gambar logo menggunakan steganografi",
                "hints": [
                    "Gunakan Stegsolve untuk analisis bit plane",
                    "Coba Blue plane 0 untuk visual message",
                    "Data extract dari Red channel untuk flag lengkap",
                    "LSB steganography technique"
                ]
            },
            "HTC-FORENSIC-002": {
                "name": "Foto Wisuda yang Mencurigakan", 
                "points": 300, 
                "category": "Digital Forensics",
                "difficulty": "Medium",
                "flag": "HTC{multi_layer_stego_master_2024}",
                "description": "Foto wisuda HTC ini menyimpan beberapa pesan tersembunyi dengan teknik steganografi yang berbeda-beda. Analisis setiap bit plane dan channel untuk menemukan semua rahasia!",
                "hints": [
                    "Ada 4 pesan tersembunyi dengan teknik berbeda",
                    "Blue plane 0: Visual message dapat dilihat langsung",
                    "Green plane 2: Pattern geometris tersembunyi",
                    "Red LSB: Data extract untuk flag utama",
                    "Green MSB: Secondary message dengan teknik MSB"
                ]
            }
        }
        
        self.badges = {
            "first_blood": {"name": "🥇 First Blood HTC", "desc": "Selesaikan challenge pertama"},
            "web_novice": {"name": "🌐 Web Novice HTC", "desc": "Selesaikan challenge web pertama"},
            "crypto_apprentice": {"name": "🔐 Crypto Apprentice HTC", "desc": "Selesaikan challenge crypto pertama"},
            "forensic_detective": {"name": "🔍 Forensic Detective HTC", "desc": "Selesaikan challenge forensik pertama"},
            "speed_demon": {"name": "🚀 Speed Demon", "desc": "Selesaikan challenge dalam < 10 menit"},
            "perfectionist": {"name": "🎯 Perfectionist HTC", "desc": "Selesaikan tanpa hint"}
        }
        
        self.load_data()
    
    def load_data(self):
        if os.path.exists(self.db_file):
            try:
                with open(self.db_file, 'r', encoding='utf-8') as f:
                    self.data = json.load(f)
            except:
                self.data = {"students": {}, "submissions": []}
        else:
            self.data = {"students": {}, "submissions": []}
    
    def save_data(self):
        with open(self.db_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
    
    def register_student(self, nim, nama, email=""):
        if nim not in self.data["students"]:
            self.data["students"][nim] = {
                "nama": nama,
                "email": email,
                "total_points": 0,
                "challenges_completed": [],
                "badges": [],
                "hints_used": {},
                "join_date": datetime.datetime.now().isoformat(),
                "last_activity": datetime.datetime.now().isoformat()
            }
            self.save_data()
            return True
        return False
    
    def submit_flag(self, nim, challenge_id, flag, hints_used=0):
        if nim not in self.data["students"]:
            return False, "NIM tidak ditemukan! Silakan daftar terlebih dahulu."
        
        if challenge_id not in self.challenges:
            return False, "Challenge ID tidak valid!"
        
        student = self.data["students"][nim]
        challenge = self.challenges[challenge_id]
        
        if challenge_id in student["challenges_completed"]:
            return False, "Challenge sudah diselesaikan sebelumnya!"
        
        if flag.strip() == challenge["flag"]:
            # Calculate points (reduce for hints used)
            points = challenge["points"]
            hint_penalty = hints_used * 10
            final_points = max(points - hint_penalty, points // 2)  # Minimum 50% points
            
            # Add to student record
            student["total_points"] += final_points
            student["challenges_completed"].append(challenge_id)
            student["hints_used"][challenge_id] = hints_used
            student["last_activity"] = datetime.datetime.now().isoformat()
            
            # Record submission
            submission = {
                "nim": nim,
                "challenge_id": challenge_id,
                "points_earned": final_points,
                "hints_used": hints_used,
                "timestamp": datetime.datetime.now().isoformat()
            }
            self.data["submissions"].append(submission)
            
            # Check for new badges
            new_badges = self.check_badges(nim)
            
            self.save_data()
            return True, f"🎉 Benar! +{final_points} poin (Hint penalty: -{hint_penalty})", new_badges
        
        return False, "❌ Flag salah! Coba lagi."
    
    def check_badges(self, nim):
        student = self.data["students"][nim]
        new_badges = []
        
        # First Blood
        if len(student["challenges_completed"]) == 1 and "first_blood" not in student["badges"]:
            student["badges"].append("first_blood")
            new_badges.append("first_blood")
        
        # Category badges
        categories = {
            "web_novice": "HTC-WEB",
            "crypto_apprentice": "HTC-CRYPTO", 
            "forensic_detective": "HTC-FORENSIC"
        }
        
        for badge, prefix in categories.items():
            if any(c.startswith(prefix) for c in student["challenges_completed"]) and badge not in student["badges"]:
                student["badges"].append(badge)
                new_badges.append(badge)
        
        return new_badges
    
    def get_leaderboard(self, limit=10):
        students = list(self.data["students"].items())
        students.sort(key=lambda x: x[1]["total_points"], reverse=True)
        return students[:limit]
    
    def get_student_stats(self, nim):
        if nim in self.data["students"]:
            return self.data["students"][nim]
        return None

def main():
    load_custom_css()
    
    # Initialize database
    if 'db' not in st.session_state:
        st.session_state.db = HTCDatabase()
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🛡️ HTC CyberSec Academy</h1>
        <p><em>Hacking The Curriculum - Platform Challenge Cybersecurity Indonesia</em></p>
        <p>🇮🇩 Mari bersama membangun Indonesia yang lebih aman di era digital!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar Navigation
    st.sidebar.title("🧭 Navigasi")
    page = st.sidebar.radio("Pilih Halaman:", [
        "🏠 Beranda",
        "📝 Daftar/Login", 
        "🎯 Challenge",
        "🏆 Leaderboard",
        "👤 Profil Saya",
        "📚 Learning Resources",
        "ℹ️ About"
    ])
    
    if page == "🏠 Beranda":
        show_home()
    elif page == "📝 Daftar/Login":
        show_register()
    elif page == "🎯 Challenge": 
        show_challenges()
    elif page == "🏆 Leaderboard":
        show_leaderboard()
    elif page == "👤 Profil Saya":
        show_profile()
    elif page == "📚 Learning Resources":
        show_resources()
    elif page == "ℹ️ About":
        show_about()

def show_home():
    st.title("🏠 Selamat Datang di HTC CyberSec Academy!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="challenge-card">
            <h3>🌐 Web Security</h3>
            <p>Pelajari SQL injection, XSS, dan kerentanan web lainnya melalui hands-on challenges.</p>
            <p><strong>Available:</strong> 1 challenge</p>
            <p><strong>Total Points:</strong> 150</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="challenge-card">
            <h3>🔐 Cryptography</h3>
            <p>Pecahkan cipher klasik dan modern, mulai dari Caesar hingga RSA encryption.</p>
            <p><strong>Available:</strong> 1 challenge</p>
            <p><strong>Total Points:</strong> 125</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="challenge-card">
            <h3>🔍 Digital Forensics</h3>
            <p>Analisis steganografi dan investigasi digital menggunakan tools profesional.</p>
            <p><strong>Available:</strong> 2 challenges</p>
            <p><strong>Total Points:</strong> 500</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick Stats
    db = st.session_state.db
    total_students = len(db.data["students"])
    total_submissions = len(db.data["submissions"])
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("👨‍🎓 Total Mahasiswa", total_students)
    with col2:
        st.metric("✅ Total Submissions", total_submissions)
    with col3:
        st.metric("🎯 Total Challenges", len(db.challenges))
    with col4:
        st.metric("🏅 Total Badges", len(db.badges))
    
    # Recent Activity
    if total_submissions > 0:
        st.subheader("📊 Aktivitas Terbaru")
        recent_submissions = sorted(db.data["submissions"], key=lambda x: x["timestamp"], reverse=True)[:5]
        
        for sub in recent_submissions:
            student_name = db.data["students"][sub["nim"]]["nama"]
            challenge_name = db.challenges[sub["challenge_id"]]["name"]
            points = sub["points_earned"]
            
            st.write(f"🎉 **{student_name}** menyelesaikan **{challenge_name}** (+{points} poin)")

def show_register():
    st.title("📝 Daftar/Login Mahasiswa HTC")
    
    tab1, tab2 = st.tabs(["🆕 Daftar Baru", "🔑 Login"])
    
    with tab1:
        st.subheader("Daftar sebagai Mahasiswa HTC")
        
        with st.form("register_form"):
            nim = st.text_input("NIM:", placeholder="Contoh: 123456789")
            nama = st.text_input("Nama Lengkap:", placeholder="Contoh: Budi Santoso")
            email = st.text_input("Email (Opsional):", placeholder="budi@htc.ac.id")
            
            if st.form_submit_button("📝 Daftar"):
                if nim and nama:
                    db = st.session_state.db
                    if db.register_student(nim, nama, email):
                        st.success(f"🎉 Selamat datang {nama}! Pendaftaran berhasil.")
                        st.balloons()
                        st.session_state.current_nim = nim
                    else:
                        st.error("⚠️ NIM sudah terdaftar! Gunakan tab Login.")
                else:
                    st.error("❌ NIM dan Nama harus diisi!")
    
    with tab2:
        st.subheader("Login dengan NIM")
        
        nim = st.text_input("Masukkan NIM Anda:", key="login_nim")
        
        if st.button("🔑 Login"):
            db = st.session_state.db
            if nim in db.data["students"]:
                st.session_state.current_nim = nim
                student = db.data["students"][nim]
                st.success(f"👋 Selamat datang kembali, {student['nama']}!")
                st.balloons()
            else:
                st.error("❌ NIM tidak ditemukan! Silakan daftar terlebih dahulu.")

def show_challenges():
    st.title("🎯 Challenge Cybersecurity HTC")
    
    if 'current_nim' not in st.session_state:
        st.warning("⚠️ Silakan login terlebih dahulu di halaman Daftar/Login.")
        return
    
    db = st.session_state.db
    student = db.data["students"][st.session_state.current_nim]
    
    st.write(f"👋 Halo **{student['nama']}**! Total poin Anda: **{student['total_points']}**")
    
    # Filter challenges
    category_filter = st.selectbox("Filter berdasarkan kategori:", 
                                 ["Semua", "Web Security", "Cryptography", "Digital Forensics"])
    
    for challenge_id, challenge in db.challenges.items():
        if category_filter != "Semua" and challenge["category"] != category_filter:
            continue
        
        is_completed = challenge_id in student["challenges_completed"]
        
        with st.expander(f"{'✅' if is_completed else '🎯'} {challenge['name']} ({challenge['difficulty']}) - {challenge['points']} poin"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.write(f"**Kategori:** {challenge['category']}")
                st.write(f"**Deskripsi:** {challenge['description']}")
                
                if is_completed:
                    hints_used = student['hints_used'].get(challenge_id, 0)
                    st.success(f"✅ Challenge completed! Hints used: {hints_used}")
                else:
                    # Hints system
                    if f"hints_{challenge_id}" not in st.session_state:
                        st.session_state[f"hints_{challenge_id}"] = 0
                    
                    if st.button(f"💡 Hint ({st.session_state[f'hints_{challenge_id}']+1}/4)", key=f"hint_{challenge_id}"):
                        current_hint = st.session_state[f"hints_{challenge_id}"]
                        if current_hint < len(challenge['hints']):
                            st.info(f"💡 **Hint {current_hint+1}:** {challenge['hints'][current_hint]}")
                            st.session_state[f"hints_{challenge_id}"] += 1
                        else:
                            st.warning("Semua hint sudah digunakan!")
                    
                    # Show used hints
                    if st.session_state[f"hints_{challenge_id}"] > 0:
                        for i in range(st.session_state[f"hints_{challenge_id}"]):
                            st.info(f"💡 **Hint {i+1}:** {challenge['hints'][i]}")
            
            with col2:
                # Badge indicator
                category_badge = {
                    "Web Security": "badge-web",
                    "Cryptography": "badge-crypto", 
                    "Digital Forensics": "badge-forensic"
                }
                
                st.markdown(f"""
                <div class="badge {category_badge.get(challenge['category'], 'badge-web')}">
                    {challenge['category']}
                </div>
                """, unsafe_allow_html=True)
                
                if not is_completed:
                    flag_input = st.text_input("🚩 Enter Flag:", key=f"flag_{challenge_id}", 
                                             placeholder="HTC{...}")
                    
                    if st.button("Submit Flag", key=f"submit_{challenge_id}"):
                        hints_used = st.session_state[f"hints_{challenge_id}"]
                        success, message, new_badges = db.submit_flag(
                            st.session_state.current_nim, 
                            challenge_id, 
                            flag_input, 
                            hints_used
                        )
                        
                        if success:
                            st.success(message)
                            for badge in new_badges:
                                badge_info = db.badges[badge]
                                st.success(f"🏅 New Badge: {badge_info['name']} - {badge_info['desc']}")
                            st.balloons()
                            st.experimental_rerun()
                        else:
                            st.error(message)

def show_leaderboard():
    st.title("🏆 Leaderboard HTC CyberSec Academy")
    
    db = st.session_state.db
    leaderboard = db.get_leaderboard(20)
    
    if not leaderboard:
        st.info("Belum ada data leaderboard. Jadilah yang pertama!")
        return
    
    st.subheader("🥇 Top Performers")
    
    for rank, (nim, student) in enumerate(leaderboard, 1):
        # Medal emojis
        medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else f"{rank}."
        
        # Badge display
        badge_display = ""
        for badge in student.get('badges', []):
            if badge in db.badges:
                badge_display += db.badges[badge]['name'] + " "
        
        st.markdown(f"""
        <div class="leaderboard-item">
            <div>
                <strong>{medal} {student['nama']}</strong><br>
                <small>Challenges: {len(student.get('challenges_completed', []))} | {badge_display}</small>
            </div>
            <div>
                <h3 style="margin: 0; color: #667eea;">{student.get('total_points', 0)} poin</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Statistics
    st.markdown("---")
    st.subheader("📊 Statistik")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_points = sum(student['total_points'] for _, student in leaderboard)
        avg_points = total_points / len(leaderboard) if leaderboard else 0
        st.metric("📈 Rata-rata Poin", f"{avg_points:.1f}")
    
    with col2:
        total_completed = sum(len(student.get('challenges_completed', [])) for _, student in leaderboard)
        st.metric("✅ Total Challenges Completed", total_completed)
    
    with col3:
        active_students = len([s for _, s in leaderboard if s.get('total_points', 0) > 0])
        st.metric("👥 Active Students", active_students)

def show_profile():
    st.title("👤 Profil Mahasiswa")
    
    if 'current_nim' not in st.session_state:
        st.warning("⚠️ Silakan login terlebih dahulu di halaman Daftar/Login.")
        return
    
    db = st.session_state.db
    nim = st.session_state.current_nim
    student = db.data["students"][nim]
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("📋 Info Mahasiswa")
        st.write(f"**Nama:** {student['nama']}")
        st.write(f"**NIM:** {nim}")
        st.write(f"**Email:** {student.get('email', 'Tidak ada')}")
        st.write(f"**Total Poin:** {student['total_points']}")
        st.write(f"**Bergabung:** {student['join_date'][:10]}")
    
    with col2:
        st.subheader("🏅 Badge Collection")
        if student.get('badges'):
            for badge in student['badges']:
                if badge in db.badges:
                    badge_info = db.badges[badge]
                    st.markdown(f"""
                    <div class="badge badge-web" style="display: block; margin-bottom: 0.5rem;">
                        {badge_info['name']}<br>
                        <small>{badge_info['desc']}</small>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("Belum ada badge. Selesaikan challenge untuk mendapat badge!")
    
    st.markdown("---")
    st.subheader("📊 Progress Challenge")
    
    completed = student.get('challenges_completed', [])
    total_challenges = len(db.challenges)
    progress = len(completed) / total_challenges if total_challenges > 0 else 0
    
    st.progress(progress)
    st.write(f"Progress: {len(completed)}/{total_challenges} challenges ({progress*100:.1f}%)")
    
    # Challenge breakdown
    if completed:
        st.subheader("✅ Challenges Completed")
        for challenge_id in completed:
            if challenge_id in db.challenges:
                challenge = db.challenges[challenge_id]
                hints_used = student.get('hints_used', {}).get(challenge_id, 0)
                st.write(f"• **{challenge['name']}** - {challenge['points']} poin (Hints: {hints_used})")

def show_resources():
    st.title("📚 Learning Resources")
    
    st.markdown("""
    ## 🛠️ Tools & Software
    
    ### Web Security
    - **Burp Suite Community** - Web application security testing
    - **OWASP ZAP** - Open source web app scanner
    - **SQLMap** - Automatic SQL injection tool
    
    ### Cryptography
    - **CyberChef** - Multi-format data manipulation tool
    - **dCode** - Classical cipher decoder
    - **OpenSSL** - Cryptography toolkit
    
    ### Digital Forensics
    - **Stegsolve** - Steganography analysis tool
    - **Binwalk** - Firmware analysis tool
    - **Wireshark** - Network protocol analyzer
    
    ## 📖 Learning Materials
    
    ### Recommended Reading
    - **The Web Application Hacker's Handbook** - Dafydd Stuttard
    - **Cryptography Engineering** - Ferguson, Schneier, Kohno
    - **The Art of Memory Forensics** - Michael Ligh
    
    ### Online Courses
    - **OWASP Academy** - Free web security training
    - **Cybrary** - Free cybersecurity courses
    - **Coursera Cybersecurity** - University-level courses
    
    ### Practice Platforms
    - **TryHackMe** - Beginner-friendly cybersecurity challenges
    - **HackTheBox** - Advanced penetration testing labs
    - **PicoCTF** - Capture The Flag challenges
    
    ## 🎓 Career Guidance
    
    ### Entry Level Positions
    - **Junior SOC Analyst** - Rp 5-8 juta/bulan
    - **IT Security Analyst** - Rp 7-12 juta/bulan
    - **Cybersecurity Specialist** - Rp 10-15 juta/bulan
    
    ### Certifications
    - **CompTIA Security+** - Entry level
    - **CEH (Certified Ethical Hacker)** - Intermediate
    - **CISSP** - Advanced/Management
    """)

def show_about():
    st.title("ℹ️ Tentang HTC CyberSec Academy")
    
    st.markdown("""
    ## 🎯 Visi & Misi
    
    **Visi:** Menjadi platform pembelajaran cybersecurity terdepan di Indonesia yang menghasilkan talenta-talenta handal dalam bidang keamanan siber.
    
    **Misi:**
    - Memberikan pembelajaran cybersecurity yang praktis dan engaging
    - Membekali mahasiswa dengan skill yang relevan dengan industri
    - Membangun komunitas cybersecurity yang kuat di Indonesia
    - Berkontribusi pada keamanan siber nasional
    
    ## 🏗️ Framework Features
    
    ### 🎮 Gamifikasi Lengkap
    - Sistem poin dan ranking
    - Badge achievements
    - Leaderboard kompetitif
    - Progress tracking individual
    
    ### 🛠️ Tools Profesional
    - Stegsolve untuk digital forensics
    - Interactive web challenges
    - Caesar cipher decoder
    - Real-world scenario simulations
    
    ### 🇮🇩 Konteks Indonesia
    - Bahasa Indonesia native
    - Skenario relevan lokal
    - Cultural context yang familiar
    - Career guidance untuk market Indonesia
    
    ## 👥 Tim Developer
    
    **HTC Instructor Team** - Dosen dan praktisi cybersecurity berpengalaman yang berdedikasi untuk pendidikan keamanan siber di Indonesia.
    
    ## 📞 Kontak & Support
    
    - **Email:** cybersec@htc.ac.id
    - **Website:** https://cybersec.htc.ac.id
    - **Discord:** HTC CyberSec Community
    
    ## 🙏 Acknowledgments
    
    Terima kasih kepada:
    - Mahasiswa HTC yang menjadi beta tester
    - Komunitas cybersecurity Indonesia
    - Open source tools developers
    - Industry partners yang mendukung program ini
    
    ---
    
    ## 🇮🇩 **Mari bersama membangun Indonesia yang lebih aman di era digital!**
    
    *Version 1.0 - Developed with ❤️ for Indonesian cybersecurity education*
    """)

if __name__ == "__main__":
    main()
