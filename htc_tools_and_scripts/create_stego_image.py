#!/usr/bin/env python3
"""
🎨 HTC Steganografi Image Creator
Akademi CyberSec HTC - Tool untuk membuat challenge steganografi

Author: HTC Instructor
Version: 1.0
Purpose: Membuat gambar dengan pesan tersembunyi untuk challenge HTC-FORENSIC-001
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

def create_base_logo():
    """Membuat logo HTC sederhana sebagai base image"""
    # Ukuran gambar
    width, height = 400, 300
    
    # Buat gambar dengan background biru muda
    img = Image.new('RGB', (width, height), color=(70, 130, 180))
    draw = ImageDraw.Draw(img)
    
    # Gambar kotak untuk logo
    logo_box = [50, 50, 350, 250]
    draw.rectangle(logo_box, fill=(255, 255, 255), outline=(0, 0, 0), width=3)
    
    # Coba load font, jika gagal gunakan default
    try:
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Text utama: HTC
    text = "HTC"
    bbox = draw.textbbox((0, 0), text, font=font_large)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = height // 2 - 40
    draw.text((x, y), text, fill=(0, 0, 0), font=font_large)
    
    # Subtitle
    subtitle = "CYBERSEC ACADEMY"
    bbox = draw.textbbox((0, 0), subtitle, font=font_small)
    sub_width = bbox[2] - bbox[0]
    x_sub = (width - sub_width) // 2
    y_sub = y + text_height + 10
    draw.text((x_sub, y_sub), subtitle, fill=(50, 50, 50), font=font_small)
    
    # Tambah beberapa dekorasi
    # Garis horizontal
    draw.line([(80, 120), (320, 120)], fill=(200, 200, 200), width=2)
    draw.line([(80, 180), (320, 180)], fill=(200, 200, 200), width=2)
    
    # Circle decorations
    for i in range(5):
        x_circle = 100 + i * 50
        draw.ellipse([x_circle-5, 220, x_circle+5, 230], fill=(100, 150, 200))
    
    return img

def embed_message_lsb(img, message, bit_plane=0):
    """Embed pesan di LSB dari color channel tertentu"""
    # Convert ke numpy array untuk manipulasi bit
    img_array = np.array(img)
    
    # Pesan yang akan disembunyikan (dalam binary)
    message_binary = ''.join([format(ord(char), '08b') for char in message])
    message_binary += '1111111111111110'  # End marker
    
    print(f"📝 Pesan: {message}")
    print(f"📊 Panjang pesan binary: {len(message_binary)} bits")
    
    # Embed di Red channel, bit plane 0 (LSB)
    bit_index = 0
    rows, cols, channels = img_array.shape
    
    for row in range(rows):
        for col in range(cols):
            if bit_index < len(message_binary):
                # Ambil pixel red channel
                red_value = img_array[row, col, 0]  # Red channel
                
                # Ubah LSB sesuai dengan bit pesan
                message_bit = int(message_binary[bit_index])
                
                # Clear LSB dan set dengan message bit
                red_value = (red_value & 0xFE) | message_bit
                img_array[row, col, 0] = red_value
                
                bit_index += 1
            else:
                break
        if bit_index >= len(message_binary):
            break
    
    return Image.fromarray(img_array)

def create_visible_text_overlay(img, message):
    """Buat overlay teks yang terlihat hanya di bit plane tertentu"""
    img_array = np.array(img)
    
    # Buat teks overlay yang akan terlihat di Blue channel LSB
    overlay_img = Image.new('RGB', img.size, color=(0, 0, 0))
    draw = ImageDraw.Draw(overlay_img)
    
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
    except:
        font = ImageFont.load_default()
    
    # Teks yang akan terlihat jelas di Stegsolve
    overlay_text = message
    
    # Posisikan teks di tengah
    bbox = draw.textbbox((0, 0), overlay_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (img.size[0] - text_width) // 2
    y = (img.size[1] - text_height) // 2
    
    # Gambar teks dengan warna yang akan terlihat di blue plane
    draw.text((x, y), overlay_text, fill=(255, 255, 255), font=font)
    
    overlay_array = np.array(overlay_img)
    
    # Embed teks ini ke blue channel LSB
    for row in range(img_array.shape[0]):
        for col in range(img_array.shape[1]):
            # Jika pixel overlay putih, set blue LSB = 1
            if overlay_array[row, col, 2] > 128:  # White pixel
                img_array[row, col, 2] = img_array[row, col, 2] | 1  # Set LSB
            else:
                img_array[row, col, 2] = img_array[row, col, 2] & 0xFE  # Clear LSB
    
    return Image.fromarray(img_array)

def main():
    print("🎨 Membuat Challenge Steganografi HTC...")
    
    # Buat direktori jika belum ada
    output_dir = "/home/kali/htc_cybersecurity_challenges/htc_forensics_challenges/htc-forensic-001"
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Buat base logo
    print("📷 Membuat base logo HTC...")
    base_img = create_base_logo()
    
    # 2. Embed pesan rahasia
    secret_message = "HTC{stegsolve_master_forensics_2024}"
    print("🔐 Embedding pesan rahasia...")
    stego_img = embed_message_lsb(base_img, secret_message)
    
    # 3. Tambah visual overlay yang terlihat di Stegsolve
    visual_message = "HIDDEN FLAG!"
    print("👁️ Menambah visual overlay...")
    final_img = create_visible_text_overlay(stego_img, visual_message)
    
    # 4. Save gambar
    output_path = os.path.join(output_dir, "htc-forensic-001-logo.png")
    final_img.save(output_path, "PNG")
    
    print(f"✅ Challenge image berhasil dibuat: {output_path}")
    print(f"🔍 Pesan tersembunyi: {secret_message}")
    print("\n📋 Instruksi untuk mahasiswa:")
    print("1. Buka gambar dengan Stegsolve")
    print("2. Coba filter Blue plane 0 untuk melihat 'HIDDEN FLAG!'")
    print("3. Extract data dari Red channel untuk mendapat flag lengkap")
    print("\n🎯 Challenge siap digunakan!")

if __name__ == "__main__":
    main()
