# 🔍 Challenge Detektif Digital HTC
*Temukan Rahasia Tersembunyi dalam Data*

## 🎯 Selamat Datang di Lab Forensik HTC
Mahasiswa HTC, bersiaplah untuk menjadi detektif digital sejati! Challenge ini akan mengajarkan teknik forensik digital dan steganografi yang digunakan oleh profesional cybersecurity untuk mengungkap informasi tersembunyi.

---

## 🏆 Daftar Challenge Forensik HTC

### HTC-FORENSIC-001: Rahasia di Balik Logo HTC (HTC-MUDAH)
**Poin**: 200 | **Estimasi Waktu**: 30 menit

**📖 Skenario**:
Seorang mahasiswa HTC mengirim logo kampus melalui email, tapi dosen curiga ada pesan rahasia tersembunyi di dalamnya. Tim IT menemukan bahwa gambar ini tidak biasa - ukuran filenya terlalu besar untuk gambar logo sederhana.

Investigasi menunjukkan kemungkinan penggunaan teknik steganografi. Bisakah Anda mengungkap pesan yang disembunyikan?

**🎯 Tujuan Pembelajaran**:
- Memahami konsep steganografi
- Berlatih analisis visual menggunakan Stegsolve
- Mempelajari teknik penyembunyian data dalam gambar
- Menggunakan tools forensik digital

**🛠️ Tools yang Dibutuhkan**: 
- Stegsolve (Java tool)
- Hex editor (opsional)
- Image viewer

**📍 File**: `htc-forensic-001-logo.png`

**💡 Petunjuk**:
1. Download dan buka file gambar dengan Stegsolve
2. Coba berbagai color plane filter (Red 0, Green 0, Blue 0, dll)
3. Perhatikan perubahan visual pada setiap filter
4. Cari teks atau pola yang muncul saat filter tertentu
5. Flag akan terlihat jelas pada filter yang tepat

**🔍 Hint Tambahan**:
- Steganografi sering menyembunyikan data di LSB (Least Significant Bit)
- Coba filter bit plane yang berbeda-beda
- Pesan tersembunyi biasanya kontras dengan background
- Jika tidak terlihat di satu plane, coba plane lainnya

---

### HTC-FORENSIC-002: Foto Wisuda Mencurigakan (HTC-SEDANG)
**Poin**: 350 | **Estimasi Waktu**: 45 menit

**📖 Skenario**:
Saat wisuda HTC, seorang fotografer mengambil foto grup mahasiswa. Namun, salah satu mahasiswa melaporkan bahwa foto tersebut telah dimodifikasi dan ada informasi sensitif tersembunyi di dalamnya.

Security team HTC memerlukan bantuan untuk menganalisis foto ini dan mengungkap apa yang disembunyikan di dalamnya.

**🎯 Tujuan Pembelajaran**:
- Advanced steganografi techniques
- Multi-layer hidden data analysis
- Metadata forensics
- Image authentication

**🛠️ Tools yang Dibutuhkan**: 
- Stegsolve
- ExifTool
- Binwalk
- Strings command

**📍 File**: `htc-forensic-002-wisuda.jpg`

---

### HTC-FORENSIC-003: Hard Drive Corruption Mystery (HTC-SULIT)
**Poin**: 500 | **Estimasi Waktu**: 90 menit

**📖 Skenario**:
Server lab HTC mengalami kerusakan, dan backup terakhir dalam bentuk disk image. Tim IT perlu memulihkan file penting dari image yang corrupt ini, termasuk database nilai mahasiswa yang sangat krusial.

**🎯 Tujuan Pembelajaran**:
- Disk forensics basics
- File carving techniques
- Data recovery methods
- Digital evidence handling

**🛠️ Tools yang Dibutuhkan**: 
- Autopsy
- The Sleuth Kit
- PhotoRec
- Foremost

**📍 File**: `htc-forensic-003-server.dd`

---

## 🎮 Sistem Progres Forensik HTC

### Ranking Detektif:
- 🕵️ **Magang Detektif HTC**: Selesaikan challenge forensik pertama
- 🔍 **Investigator HTC**: Kuasai steganografi dan analisis gambar
- 🏅 **Forensic Expert HTC**: Selesaikan disk forensics
- 👑 **Digital Detective Master**: Selesaikan semua challenge forensik

### Prestasi Khusus:
- 🎨 **Visual Master**: Temukan hidden message tanpa hint
- ⚡ **Speed Investigator**: Selesaikan dalam waktu record
- 🔬 **Tool Expert**: Gunakan multiple tools dengan efektif
- 🧩 **Pattern Recognizer**: Identifikasi teknik steganografi yang digunakan

---

## 📚 Fundamental Forensik Digital HTC

### Konsep Penting:
1. **Steganografi**: Seni menyembunyikan informasi
2. **Bit Plane Analysis**: Analisis layer bit dalam gambar
3. **LSB Steganography**: Penyembunyian di bit terakhir
4. **Metadata Analysis**: Informasi tersembunyi dalam file properties
5. **File Carving**: Recovery file dari raw data

### Teknik Steganografi:
- **LSB Insertion**: Modifikasi bit terakhir
- **Masking & Filtering**: Penyembunyian visual
- **Redundant Pattern Encoding**: Menggunakan pola berulang
- **Spread Spectrum**: Distribusi data across frequency

### Tools Forensik:
- **Stegsolve**: Visual steganography analysis
- **Binwalk**: Firmware analysis dan file extraction
- **ExifTool**: Metadata viewer dan editor
- **Strings**: Text extraction dari binary files
- **Hex Editors**: Binary file analysis

---

## 🛠️ Tutorial Stegsolve untuk Mahasiswa HTC

### Installation:
```bash
# Download Stegsolve
wget http://www.caesum.com/handbook/Stegsolve.jar
java -jar Stegsolve.jar
```

### Basic Usage:
1. **File → Open**: Buka file gambar
2. **Analyse**: Pilih berbagai filter
3. **Data Extract**: Extract hidden data
4. **Frame Browser**: Untuk animated images

### Filter yang Berguna:
- **Red/Green/Blue plane 0-7**: Analisis per color channel
- **Gray bits**: Konversi grayscale dengan bit manipulation
- **Random colour map**: Highlight differences

### Pro Tips:
- Selalu coba semua bit plane (0-7) untuk setiap color
- Perhatikan pola atau teks yang muncul
- Screenshot hasil yang menarik untuk dokumentasi
- Combine dengan tools lain untuk analisis lengkap

---

## 🇮🇩 Aplikasi di Indonesia

### Kasus Nyata:
- **Digital Evidence**: Kasus cybercrime di pengadilan
- **Corporate Espionage**: Perlindungan data perusahaan
- **Academic Integrity**: Deteksi plagiarisme advanced
- **Government Security**: Analisis komunikasi tersembunyi

### Career Opportunities:
- **Digital Forensic Analyst**: Rp 8-15 juta/bulan
- **Incident Response Specialist**: Rp 12-20 juta/bulan
- **Cybersecurity Consultant**: Rp 15-30 juta/bulan
- **Law Enforcement Cyber Unit**: Karir di Polri/TNI

---

## 🎯 Challenge Walkthrough Template

### Pre-Analysis:
1. **File Info**: Check file size, format, creation date
2. **Visual Inspection**: Look for obvious anomalies  
3. **Metadata Check**: ExifTool analysis
4. **String Search**: Look for readable text

### Stegsolve Analysis:
1. **Open Image**: Load target file
2. **Systematic Check**: Go through all bit planes
3. **Document Findings**: Screenshot interesting results
4. **Data Extraction**: Use built-in tools if needed

### Post-Analysis:
1. **Verify Results**: Cross-check with other tools
2. **Document Process**: Write detailed methodology
3. **Learn from Technique**: Understand how it was hidden
4. **Practice Defense**: How to detect/prevent this

---

## 💡 Tips untuk Mahasiswa HTC

### Mindset Detektif:
- 🔍 **Be Curious**: Selalu pertanyakan hal aneh
- 🧪 **Methodical**: Ikuti prosedur sistematis  
- 📝 **Document Everything**: Catat semua langkah
- 🤝 **Collaborate**: Diskusi temuan dengan teman

### Technical Skills:
- **Tool Mastery**: Kuasai minimal 3-5 forensic tools
- **Pattern Recognition**: Latih mata untuk melihat anomali
- **Scripting**: Automate repetitive analysis tasks
- **Report Writing**: Komunikasi temuan dengan jelas

### Career Development:
- **Certification**: GCFA, GCFE, EnCE
- **Practice**: Participate in CTF competitions
- **Community**: Join forensic communities
- **Ethics**: Always follow legal procedures

---

## 🏃‍♂️ Quick Start Guide

1. **Install Stegsolve**: Download dan test dengan sample image
2. **Start dengan HTC-FORENSIC-001**: Challenge termudah
3. **Practice Systematic Analysis**: Jangan skip langkah
4. **Document Your Process**: Buat writeup detail
5. **Share Knowledge**: Diskusi teknik dengan teman

### Sample Workflow:
```
1. File Analysis (5 min)
2. Metadata Extraction (5 min)  
3. Stegsolve Bit Plane Analysis (15 min)
4. Documentation (5 min)
5. Flag Submission (1 min)
```

---

## 🇮🇩 Pesan untuk Detektif Digital HTC

Sebagai calon digital forensic expert Indonesia, kalian akan menjadi mata dan telinga dalam dunia cyber. Setiap pixel yang kalian analisis, setiap bit yang kalian investigasi, berkontribusi pada keadilan dan keamanan digital Indonesia.

**Ingat**: Digital forensics bukan hanya tentang teknologi, tapi juga tentang keadilan, integritas, dan perlindungan korban. Gunakan skill ini untuk kebaikan dan selalu ikuti prosedur legal yang benar.

---

*Ungkap rahasia, temukan kebenaran, jadilah Digital Detective Master HTC! 🔍🇮🇩*
