#!/usr/bin/env python3
"""
🏆 HTC Cybersecurity Challenge Scoreboard
Akademi CyberSec HTC - Sistem Tracking Progress Mahasiswa

Author: HTC Instructor  
Version: 1.0
Purpose: Monitor progress dan motivasi mahasiswa HTC
"""

import json
import os
import datetime
from typing import Dict, List

class HTCScoreboard:
    def __init__(self):
        self.data_file = "htc_scores.json"
        self.challenges = {
            # Web Challenges
            "HTC-WEB-001": {"name": "Portal Login Vulnerable", "points": 150, "category": "Web Security"},
            "HTC-WEB-002": {"name": "Comment Section XSS", "points": 175, "category": "Web Security"},
            "HTC-WEB-003": {"name": "Admin Panel Bypass", "points": 350, "category": "Web Security"},
            "HTC-WEB-004": {"name": "File Upload Fiasco", "points": 400, "category": "Web Security"},
            "HTC-WEB-005": {"name": "Session Hijacking", "points": 650, "category": "Web Security"},
            
            # Crypto Challenges  
            "HTC-CRYPTO-001": {"name": "Pesan Rahasia Profesor", "points": 125, "category": "Cryptography"},
            "HTC-CRYPTO-002": {"name": "Tugas Teracak", "points": 150, "category": "Cryptography"},
            "HTC-CRYPTO-003": {"name": "Password Lab Tersembunyi", "points": 300, "category": "Cryptography"},
            "HTC-CRYPTO-004": {"name": "Kebocoran Database", "points": 400, "category": "Cryptography"},
            "HTC-CRYPTO-005": {"name": "RSA Key Exchange", "points": 650, "category": "Cryptography"},
            
            # Forensics Challenges
            "HTC-FORENSIC-001": {"name": "Rahasia di Balik Logo HTC", "points": 200, "category": "Digital Forensics"},
            "HTC-FORENSIC-002": {"name": "Foto Wisuda Mencurigakan", "points": 350, "category": "Digital Forensics"},
            "HTC-FORENSIC-003": {"name": "Hard Drive Corruption Mystery", "points": 500, "category": "Digital Forensics"},
        }
        
        self.badges = {
            "first_blood": {"name": "🥇 First Blood HTC", "desc": "Selesaikan challenge pertama"},
            "web_novice": {"name": "🌐 Web Novice HTC", "desc": "Selesaikan challenge web pertama"},
            "crypto_apprentice": {"name": "🔐 Crypto Apprentice HTC", "desc": "Selesaikan challenge crypto pertama"},
            "forensic_detective": {"name": "🔍 Forensic Detective HTC", "desc": "Selesaikan challenge forensik pertama"},
            "speed_demon": {"name": "🚀 Speed Demon", "desc": "Selesaikan challenge mudah < 10 menit"},
            "perfectionist": {"name": "🎯 Perfectionist HTC", "desc": "Selesaikan tanpa hint"},
            "htc_legend": {"name": "👑 HTC Legend", "desc": "Top 3 leaderboard bulanan"}
        }
        
        self.load_data()
    
    def load_data(self):
        """Load data scoreboard dari file JSON"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.data = json.load(f)
            except:
                self.data = {"students": {}, "submissions": []}
        else:
            self.data = {"students": {}, "submissions": []}
    
    def save_data(self):
        """Save data scoreboard ke file JSON"""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
    
    def add_student(self, nim: str, nama: str):
        """Tambah mahasiswa baru"""
        if nim not in self.data["students"]:
            self.data["students"][nim] = {
                "nama": nama,
                "total_points": 0,
                "challenges_completed": [],
                "badges": [],
                "join_date": datetime.datetime.now().isoformat()
            }
            self.save_data()
            print(f"✅ Mahasiswa {nama} ({nim}) berhasil ditambahkan!")
        else:
            print(f"⚠️ Mahasiswa dengan NIM {nim} sudah ada!")
    
    def submit_flag(self, nim: str, challenge_id: str, flag: str, time_taken: int = None):
        """Submit flag untuk challenge tertentu"""
        if nim not in self.data["students"]:
            print(f"❌ NIM {nim} tidak ditemukan! Daftar dulu dengan add_student.")
            return False
        
        if challenge_id not in self.challenges:
            print(f"❌ Challenge {challenge_id} tidak valid!")
            return False
        
        # Simulasi validasi flag (dalam implementasi nyata, ini lebih kompleks)
        correct_flags = {
            "HTC-WEB-001": "HTC{sql_injection_master_indonesia_2024}",
            "HTC-CRYPTO-001": "HTC{caesar_cipher_master_indonesia}",
            "HTC-FORENSIC-001": "HTC{stegsolve_master_forensics_2024}",
            # Tambah flag lainnya...
        }
        
        if challenge_id in correct_flags and flag == correct_flags[challenge_id]:
            student = self.data["students"][nim]
            
            if challenge_id not in student["challenges_completed"]:
                # Tambah poin
                points = self.challenges[challenge_id]["points"]
                student["total_points"] += points
                student["challenges_completed"].append(challenge_id)
                
                # Record submission
                submission = {
                    "nim": nim,
                    "challenge_id": challenge_id,
                    "timestamp": datetime.datetime.now().isoformat(),
                    "points_earned": points,
                    "time_taken": time_taken
                }
                self.data["submissions"].append(submission)
                
                # Check for badges
                self.check_badges(nim)
                
                self.save_data()
                print(f"🎉 Benar! {student['nama']} mendapat {points} poin!")
                print(f"🏆 Total poin: {student['total_points']}")
                return True
            else:
                print(f"⚠️ Challenge {challenge_id} sudah diselesaikan sebelumnya!")
                return False
        else:
            print(f"❌ Flag salah untuk challenge {challenge_id}!")
            return False
    
    def check_badges(self, nim: str):
        """Check dan berikan badge yang layak"""
        student = self.data["students"][nim]
        new_badges = []
        
        # First Blood badge
        if len(student["challenges_completed"]) == 1 and "first_blood" not in student["badges"]:
            student["badges"].append("first_blood")
            new_badges.append("first_blood")
        
        # Category-specific badges
        web_challenges = [c for c in student["challenges_completed"] if c.startswith("HTC-WEB")]
        crypto_challenges = [c for c in student["challenges_completed"] if c.startswith("HTC-CRYPTO")]
        forensic_challenges = [c for c in student["challenges_completed"] if c.startswith("HTC-FORENSIC")]
        
        if len(web_challenges) >= 1 and "web_novice" not in student["badges"]:
            student["badges"].append("web_novice")
            new_badges.append("web_novice")
            
        if len(crypto_challenges) >= 1 and "crypto_apprentice" not in student["badges"]:
            student["badges"].append("crypto_apprentice")
            new_badges.append("crypto_apprentice")
            
        if len(forensic_challenges) >= 1 and "forensic_detective" not in student["badges"]:
            student["badges"].append("forensic_detective")
            new_badges.append("forensic_detective")
        
        # Announce new badges
        for badge in new_badges:
            print(f"🏅 Badge baru: {self.badges[badge]['name']} - {self.badges[badge]['desc']}")
    
    def show_leaderboard(self, top_n: int = 10):
        """Tampilkan leaderboard top N"""
        students = list(self.data["students"].items())
        students.sort(key=lambda x: x[1]["total_points"], reverse=True)
        
        print("🏆 LEADERBOARD HTC CYBERSECURITY ACADEMY 🏆")
        print("=" * 60)
        
        for i, (nim, student) in enumerate(students[:top_n], 1):
            badges_str = " ".join([self.badges[b]["name"] for b in student["badges"][:3]])
            print(f"{i:2d}. {student['nama']:<20} | {student['total_points']:4d} poin | {badges_str}")
        
        print("=" * 60)
    
    def show_student_progress(self, nim: str):
        """Tampilkan progress individual mahasiswa"""
        if nim not in self.data["students"]:
            print(f"❌ NIM {nim} tidak ditemukan!")
            return
        
        student = self.data["students"][nim]
        print(f"📊 PROGRESS MAHASISWA HTC: {student['nama']} ({nim})")
        print("=" * 50)
        print(f"🏆 Total Poin: {student['total_points']}")
        print(f"✅ Challenge Selesai: {len(student['challenges_completed'])}")
        print(f"🏅 Badge: {len(student['badges'])}")
        
        print("\n🎯 Challenge yang Diselesaikan:")
        for challenge_id in student["challenges_completed"]:
            challenge_info = self.challenges[challenge_id]
            print(f"  • {challenge_id}: {challenge_info['name']} (+{challenge_info['points']} poin)")
        
        print("\n🏅 Badge yang Diraih:")
        for badge in student["badges"]:
            badge_info = self.badges[badge]
            print(f"  • {badge_info['name']}: {badge_info['desc']}")
        
        print("=" * 50)

def main():
    scoreboard = HTCScoreboard()
    
    print("🛡️ Selamat Datang di HTC Cybersecurity Scoreboard!")
    print("🎓 Akademi CyberSec HTC - Track Progress Anda\n")
    
    while True:
        print("\n" + "=" * 40)
        print("Menu Scoreboard HTC:")
        print("1. Daftar sebagai mahasiswa baru")
        print("2. Submit flag challenge")
        print("3. Lihat leaderboard")
        print("4. Lihat progress individual")
        print("5. Keluar")
        
        choice = input("\nPilih menu (1-5): ").strip()
        
        if choice == '1':
            nim = input("Masukkan NIM: ").strip()
            nama = input("Masukkan Nama: ").strip()
            scoreboard.add_student(nim, nama)
            
        elif choice == '2':
            nim = input("Masukkan NIM: ").strip()
            challenge_id = input("Masukkan Challenge ID (e.g., HTC-WEB-001): ").strip().upper()
            flag = input("Masukkan Flag: ").strip()
            scoreboard.submit_flag(nim, challenge_id, flag)
            
        elif choice == '3':
            scoreboard.show_leaderboard()
            
        elif choice == '4':
            nim = input("Masukkan NIM: ").strip()
            scoreboard.show_student_progress(nim)
            
        elif choice == '5':
            print("\n👋 Terima kasih! Semangat belajar cybersecurity!")
            print("🇮🇩 Mari bersama amankan Indonesia digital!")
            break
            
        else:
            print("❌ Pilihan tidak valid!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program dihentikan. Tetap semangat belajar!")
    except Exception as e:
        print(f"\n❌ Terjadi error: {e}")
