# 🔍 HTC-FORENSIC-001: Rahasia di Balik Logo HTC

## 📋 Informasi Challenge
- **Kategori**: Digital Forensics & Steganografi
- **Tingkat**: HTC-MUDAH
- **Poin**: 200
- **Estimasi Waktu**: 30 menit
- **Flag Format**: HTC{...}

---

## 📖 Skenario

Seorang mahasiswa HTC mengirim logo kampus melalui email kepada dosen, tapi ada yang aneh dengan file tersebut. Tim IT menemukan bahwa gambar ini memiliki ukuran file yang tidak wajar - terlalu besar untuk gambar logo sederhana.

Investigasi awal menunjukkan kemungkinan penggunaan teknik steganografi untuk menyembunyikan pesan rahasia. Sebagai anggota tim cybersecurity HTC, Anda diminta untuk menganalisis gambar ini dan mengungkap pesan yang disembunyikan.

**File yang mencurigakan**: `htc-forensic-001-logo.png`

---

## 🎯 Tujuan Pembelajaran

Setelah menyelesaikan challenge ini, mahasiswa akan:
- ✅ Memahami konsep dasar steganografi
- ✅ Menguasai penggunaan Stegsolve untuk analisis visual
- ✅ Belajar teknik bit plane analysis
- ✅ Memahami LSB (Least Significant Bit) steganography
- ✅ Menggunakan tools forensik digital untuk investigasi

---

## 🛠️ Tools yang Dibutuhkan

### Wajib:
- **Stegsolve** - Tool utama untuk analisis steganografi
- **Java Runtime Environment** - Untuk menjalankan Stegsolve

### Opsional (untuk analisis lanjutan):
- **Hexeditor** - Untuk melihat raw bytes
- **ExifTool** - Untuk analisis metadata
- **Strings command** - Untuk mencari teks tersembunyi

---

## 🚀 Installation Guide

### Install Stegsolve:
```bash
# Download Stegsolve (jika belum ada)
wget http://www.caesum.com/handbook/Stegsolve.jar

# Jalankan Stegsolve
java -jar Stegsolve.jar
```

### Alternative Installation:
```bash
# Atau menggunakan apt (jika tersedia)
sudo apt install stegsolve

# Atau download dari GitHub
git clone https://github.com/zardus/ctf-tools
cd ctf-tools/stegsolve
./install
```

---

## 📋 Step-by-Step Solution Guide

### Langkah 1: Analisis Awal
1. **Lihat file gambar secara visual**
   - Apakah ada yang tampak aneh?
   - Perhatikan warna dan detail

2. **Check file properties**
   ```bash
   file htc-forensic-001-logo.png
   ls -la htc-forensic-001-logo.png
   ```

### Langkah 2: Buka dengan Stegsolve
1. **Launch Stegsolve**
   ```bash
   java -jar Stegsolve.jar
   ```

2. **Open Image**
   - File → Open
   - Pilih `htc-forensic-001-logo.png`

### Langkah 3: Bit Plane Analysis
1. **Coba berbagai filter secara sistematis**:
   - Red plane 0, 1, 2, 3, 4, 5, 6, 7
   - Green plane 0, 1, 2, 3, 4, 5, 6, 7  
   - Blue plane 0, 1, 2, 3, 4, 5, 6, 7

2. **Perhatikan perubahan visual**:
   - Apakah muncul teks atau pola aneh?
   - Screenshot hasil yang menarik

### Langkah 4: Data Extraction
1. **Gunakan Data Extract feature**
   - Analyse → Data Extract
   - Pilih channel dan bit plane yang tepat
   - Extract data sebagai text

2. **Save hasil extraction**
   - Simpan output untuk analisis lebih lanjut

---

## 💡 Hints (Progressive)

### Hint Level 1 (Gratis):
"Gambar normal biasanya tidak menyimpan informasi di bit terakhir setiap pixel. Coba lihat apa yang tersembunyi di sana..."

### Hint Level 2 (-10 poin):
"Ada dua pesan tersembunyi dalam gambar ini. Satu terlihat secara visual, satu lagi dalam bentuk data. Coba Blue plane 0 dulu!"

### Hint Level 3 (-20 poin):  
"Teks 'HIDDEN FLAG!' akan muncul jelas di Blue plane 0. Untuk flag lengkap, gunakan Data Extract pada Red channel."

### Hint Level 4 (-30 poin):
"Setting extract: Red channel, LSB first, pilih 'extract by pixel order'. Flag dimulai dengan HTC{"

---

## 🏆 Success Criteria

### Berhasil menemukan:
- ✅ Pesan visual yang tersembunyi: "HIDDEN FLAG!"
- ✅ Flag lengkap: `HTC{stegsolve_master_forensics_2024}`
- ✅ Memahami teknik yang digunakan
- ✅ Bisa menjelaskan proses kepada orang lain

### Bonus Points:
- 🌟 **+25 poin**: Selesai tanpa hint
- 🌟 **+15 poin**: Dokumentasi proses lengkap
- 🌟 **+10 poin**: Temukan kedua pesan dalam < 15 menit

---

## 📝 Write-up Template

Setelah menyelesaikan challenge, tuliskan laporan dengan format:

### 1. Executive Summary
"Dalam challenge ini saya menemukan..."

### 2. Tools Used
- Stegsolve v1.x
- Java Runtime Environment
- (tools tambahan jika ada)

### 3. Analysis Process
```
Step 1: Initial visual inspection
Step 2: File property analysis  
Step 3: Stegsolve bit plane analysis
Step 4: Data extraction
Step 5: Flag verification
```

### 4. Findings
- Visual message discovered: "HIDDEN FLAG!"
- Location: Blue plane 0 (LSB)
- Full flag extracted: `HTC{stegsolve_master_forensics_2024}`
- Location: Red channel LSB

### 5. Technical Details
"Steganografi menggunakan LSB insertion technique..."

### 6. Lessons Learned
"Dari challenge ini saya belajar..."

---

## 🔬 Advanced Analysis (Opsional)

Untuk mahasiswa yang ingin eksplorasi lebih dalam:

### Metadata Analysis:
```bash
exiftool htc-forensic-001-logo.png
```

### Hex Analysis:
```bash
hexdump -C htc-forensic-001-logo.png | head -20
strings htc-forensic-001-logo.png
```

### Statistical Analysis:
```python
# Analisis distribusi pixel values
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open('htc-forensic-001-logo.png')
data = np.array(img)

# Plot histogram untuk setiap channel
plt.figure(figsize=(12, 4))
for i, color in enumerate(['red', 'green', 'blue']):
    plt.subplot(1, 3, i+1)
    plt.hist(data[:,:,i].flatten(), bins=256, alpha=0.7)
    plt.title(f'{color.title()} Channel Histogram')
plt.show()
```

---

## 🛡️ Defense & Detection

### Cara mencegah serangan steganografi:
1. **File Integrity Monitoring**: Hash verification
2. **Statistical Analysis**: Deteksi anomali distribusi pixel
3. **Automated Scanning**: Tools seperti StegExpose
4. **Policy Enforcement**: Restrict file types di email

### Cara mendeteksi steganografi:
1. **Visual Inspection**: Cari anomali visual
2. **Statistical Tests**: Chi-square, histogram analysis
3. **Steganalysis Tools**: StegExpose, StegSecret
4. **File Size Analysis**: Compare dengan normal files

---

## 🎓 Career Connection

### Skill yang dipelajari berguna untuk:
- **Digital Forensic Investigator**: Analisis bukti digital
- **Incident Response Analyst**: Investigasi security incidents  
- **Malware Researcher**: Reverse engineering samples
- **Security Consultant**: Vulnerability assessment

### Industry Applications:
- **Law Enforcement**: Criminal investigation
- **Corporate Security**: Data loss prevention
- **Military/Government**: Intelligence analysis
- **Academia**: Research dan education

---

## 📞 Troubleshooting

### Stegsolve tidak jalan:
```bash
# Check Java version
java -version

# Install Java jika belum ada
sudo apt install default-jre

# Run dengan verbose
java -jar Stegsolve.jar -verbose
```

### Image tidak ter-load:
- Pastikan file path benar
- Check file permissions
- Coba copy file ke direktori yang sama dengan Stegsolve

### Extract tidak berhasil:
- Pastikan pilih channel dan bit plane yang benar
- Coba berbagai extraction options
- Periksa endianness settings

---

## 🎉 Congratulations!

Selamat! Anda telah berhasil menyelesaikan challenge steganografi pertama. Anda sekarang memahami:

✅ Dasar-dasar steganografi dan LSB technique  
✅ Penggunaan Stegsolve untuk analisis visual  
✅ Bit plane analysis dan data extraction  
✅ Investigasi forensik gambar digital  

**Next Steps**: Lanjut ke HTC-FORENSIC-002 untuk challenge yang lebih kompleks!

---

## 🇮🇩 Pesan Motivasi

*"Setiap pixel yang kalian analisis, setiap bit yang kalian investigasi, adalah langkah menuju menjadi digital detective yang handal. Steganografi adalah seni menyembunyikan rahasia - dan kalian baru saja belajar cara membongkarnya!"*

**Mari terus asah kemampuan forensik digital untuk keamanan siber Indonesia! 🔍🇮🇩**
