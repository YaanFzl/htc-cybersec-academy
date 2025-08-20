#!/usr/bin/env python3
"""
🔐 HTC Caesar Cipher Decoder
Akademi CyberSec HTC - Tool untuk Challenge Kriptografi

Author: HTC Instructor
Version: 1.0
Purpose: Membantu mahasiswa HTC mempelajari Caesar cipher
"""

def caesar_decode(text, shift):
    """Decode Caesar cipher dengan shift tertentu"""
    result = ""
    for char in text:
        if char.isalpha():
            # Tentukan apakah huruf besar atau kecil
            is_upper = char.isupper()
            char = char.upper()
            
            # Geser huruf mundur
            shifted = ord(char) - shift
            if shifted < ord('A'):
                shifted += 26
            
            result_char = chr(shifted)
            if not is_upper:
                result_char = result_char.lower()
            
            result += result_char
        else:
            result += char
    return result

def brute_force_caesar(text):
    """Coba semua kemungkinan shift untuk Caesar cipher"""
    print("🔍 Brute Force Caesar Cipher - Semua Kemungkinan Shift:\n")
    print("="*60)
    
    for shift in range(1, 26):
        decoded = caesar_decode(text, shift)
        print(f"Shift {shift:2d}: {decoded}")
    
    print("="*60)

def analyze_text(text):
    """Analisis sederhana untuk membantu identifikasi bahasa"""
    # Kata-kata umum dalam bahasa Indonesia
    indonesian_words = ['dan', 'atau', 'yang', 'untuk', 'adalah', 'dengan', 
                       'dalam', 'dari', 'ini', 'itu', 'akan', 'pada']
    
    text_lower = text.lower()
    found_words = []
    
    for word in indonesian_words:
        if word in text_lower:
            found_words.append(word)
    
    return found_words

def main():
    print("🛡️ Selamat datang di HTC Caesar Decoder!")
    print("Akademi CyberSec HTC - Tool Pembelajaran Kriptografi\n")
    
    while True:
        print("\n" + "="*50)
        print("Pilihan Menu:")
        print("1. Decode dengan shift tertentu")
        print("2. Brute force semua shift (1-25)")
        print("3. Challenge HTC-CRYPTO-001")
        print("4. Keluar")
        
        choice = input("\nPilih opsi (1-4): ").strip()
        
        if choice == '1':
            text = input("\nMasukkan teks yang akan didecode: ")
            try:
                shift = int(input("Masukkan nilai shift (1-25): "))
                if 1 <= shift <= 25:
                    result = caesar_decode(text, shift)
                    print(f"\n🎯 Hasil decode dengan shift {shift}:")
                    print(f"'{result}'")
                    
                    # Analisis sederhana
                    found_words = analyze_text(result)
                    if found_words:
                        print(f"\n💡 Kata Indonesia yang terdeteksi: {', '.join(found_words)}")
                else:
                    print("❌ Shift harus antara 1-25!")
            except ValueError:
                print("❌ Masukkan angka yang valid!")
        
        elif choice == '2':
            text = input("\nMasukkan teks yang akan di-brute force: ")
            brute_force_caesar(text)
            
            print("\n💡 Tips: Cari hasil yang membentuk kata-kata bermakna!")
            print("🔍 Perhatikan hasil yang mengandung kata bahasa Indonesia umum.")
        
        elif choice == '3':
            print("\n🎓 Challenge HTC-CRYPTO-001: Pesan Rahasia Profesor")
            encrypted_msg = "Udkqhp xqwxn phqjlnxwl xmldq anklud dgdodk: KWF{fdhvdu_flskhu_pdvwhu_lqgrqhvld}"
            print(f"\nPesan terenkripsi: {encrypted_msg}")
            
            print("\n🔍 Mencoba semua kemungkinan shift...")
            brute_force_caesar(encrypted_msg)
            
            print("\n💡 Hint: Cari hasil yang membuat kalimat bermakna dalam bahasa Indonesia!")
            print("🚩 Flag akan dalam format HTC{...}")
        
        elif choice == '4':
            print("\n👋 Terima kasih sudah menggunakan HTC Caesar Decoder!")
            print("🎓 Semangat belajar cybersecurity, mahasiswa HTC!")
            print("🇮🇩 Mari bersama amankan Indonesia digital!")
            break
        
        else:
            print("❌ Pilihan tidak valid! Silakan pilih 1-4.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program dihentikan. Selamat belajar cybersecurity!")
    except Exception as e:
        print(f"\n❌ Terjadi error: {e}")
        print("🔧 Silakan hubungi instruktur HTC jika masalah berlanjut.")
