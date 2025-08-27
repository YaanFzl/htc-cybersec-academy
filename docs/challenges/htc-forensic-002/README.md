# 🎯 HTC-FORENSIC-002: Foto Wisuda yang Mencurigakan

**Kategori:** Digital Forensics  
**Tingkat:** Medium  
**Poin:** 300  

## 📝 Deskripsi Challenge

Selamat datang di tantangan steganografi tingkat menengah! Foto wisuda HTC ini terlihat normal di permukaan, tetapi menyimpan beberapa rahasia yang tersembunyi dengan berbagai teknik steganografi yang berbeda.

Tim keamanan HTC menemukan foto ini dalam investigasi dan mencurigai bahwa foto tersebut menyimpan informasi rahasia. Sebagai analis forensik digital, tugas Anda adalah mengungkap SEMUA pesan tersembunyi yang ada dalam gambar ini.

## 🎯 Objective

Temukan **flag utama** yang tersembunyi dalam foto wisuda menggunakan berbagai teknik analisis steganografi.

## 📁 File Challenge

- `htc-forensic-002-wisuda.jpg` - Foto wisuda HTC yang mencurigakan
- `htc-forensic-002-wisuda-small.jpg` - Versi kecil untuk preview

## 🔧 Tools yang Direkomendasikan

- **Stegsolve** - Tool utama untuk analisis bit plane
- **Binwalk** - Untuk analisis file embedded
- **Hexedit/xxd** - Untuk analisis hex
- **GIMP** - Untuk manipulasi gambar

## 💡 Hints

1. **Ada 4 pesan tersembunyi dengan teknik berbeda**
2. **Blue plane 0: Visual message dapat dilihat langsung**
3. **Green plane 2: Pattern geometris tersembunyi**
4. **Red LSB: Data extract untuk flag utama**
5. **Green MSB: Secondary message dengan teknik MSB**

## 🎯 Flag Format

Flag yang dicari mengikuti format: `HTC{...}`

## 📚 Learning Objectives

Setelah menyelesaikan challenge ini, Anda akan memahami:

1. **Multiple Layer Steganography** - Bagaimana berbagai teknik dapat dikombinasikan
2. **Bit Plane Analysis** - Analisis setiap bit plane dalam gambar
3. **LSB vs MSB Techniques** - Perbedaan antara LSB dan MSB steganography
4. **Visual Steganography** - Pesan yang dapat dilihat secara visual
5. **Pattern Recognition** - Mengenali pola geometris dalam bit plane

## 🚀 Getting Started

1. Download file gambar
2. Buka menggunakan Stegsolve
3. Mulai dengan menganalisis setiap bit plane
4. Cari pesan visual pada Blue plane 0
5. Cari pattern pada Green plane 2
6. Ekstrak data dari Red LSB
7. Coba ekstraksi dari Green MSB

## 🔍 Investigation Steps

### Step 1: Visual Inspection
- Buka gambar dengan image viewer biasa
- Perhatikan detail foto wisuda

### Step 2: Bit Plane Analysis
- Gunakan Stegsolve untuk menganalisis setiap bit plane
- Blue plane 0 → Visual message
- Green plane 2 → Geometric patterns

### Step 3: Data Extraction
- Red LSB → Main flag
- Green MSB → Secondary message

### Step 4: Cross-reference
- Kombinasikan informasi dari semua layer
- Verifikasi dengan hint yang diberikan

## 📊 Scoring

- **Base Points:** 300
- **Hint Penalty:** -10 poin per hint
- **Minimum Points:** 150 (50% dari base)

## ⚠️ Troubleshooting

**Stegsolve tidak menunjukkan pesan?**
- Pastikan Anda menganalisis bit plane yang tepat
- Coba adjust contrast/brightness

**Data extraction gagal?**
- Pastikan format extraction yang benar
- Coba berbagai encoding (ASCII, hex, etc.)

**Tidak bisa melihat pattern?**
- Zoom in/out pada gambar
- Coba invert colors

## 🎓 Educational Notes

Challenge ini mendemonstrasikan teknik steganografi real-world yang sering digunakan dalam:

- **Corporate espionage** - Menyembunyikan data dalam dokumen
- **Malware communication** - C&C communication
- **Data exfiltration** - Menyelundupkan data keluar
- **Digital watermarking** - Proof of ownership

## 🏆 Success Criteria

Challenge dianggap selesai ketika Anda berhasil:
1. ✅ Menemukan visual message di Blue plane 0
2. ✅ Mengenali pattern di Green plane 2  
3. ✅ Mengekstrak flag utama dari Red LSB
4. ✅ Submit flag yang benar

---

**Good luck, cyber detectives! 🕵️‍♂️**

*Remember: Real forensic investigations require patience, attention to detail, and systematic approach.*
