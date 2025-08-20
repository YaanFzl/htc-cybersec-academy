#!/usr/bin/env python3
"""
🎨 HTC Advanced Steganography Challenge Creator
Akademi CyberSec HTC - Tool untuk membuat challenge steganografi medium

Author: HTC Instructor
Version: 1.0
Purpose: Membuat gambar dengan multiple hidden messages untuk HTC-FORENSIC-002
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import random
import string

def create_graduation_photo():
    """Membuat foto simulasi wisuda HTC dengan multiple students"""
    width, height = 800, 600
    
    # Background kampus
    img = Image.new('RGB', (width, height), color=(135, 206, 235))  # Sky blue
    draw = ImageDraw.Draw(img)
    
    # Gambar background gedung kampus
    # Main building
    building_color = (220, 220, 220)
    draw.rectangle([50, 200, 750, 500], fill=building_color, outline=(100, 100, 100), width=3)
    
    # Windows
    window_color = (100, 150, 200)
    for row in range(3):
        for col in range(8):
            x1 = 80 + col * 80
            y1 = 230 + row * 80
            x2 = x1 + 40
            y2 = y1 + 50
            draw.rectangle([x1, y1, x2, y2], fill=window_color, outline=(50, 50, 50))
    
    # HTC Logo on building
    try:
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
    
    # HTC text on building
    htc_text = "HTC"
    bbox = draw.textbbox((0, 0), htc_text, font=font_large)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) // 2
    y = 250
    draw.text((x, y), htc_text, fill=(50, 50, 150), font=font_large)
    
    # Subtitle
    subtitle = "UNIVERSITAS TEKNOLOGI"
    bbox = draw.textbbox((0, 0), subtitle, font=font_medium)
    sub_width = bbox[2] - bbox[0]
    x_sub = (width - sub_width) // 2
    y_sub = y + 40
    draw.text((x_sub, y_sub), subtitle, fill=(70, 70, 170), font=font_medium)
    
    # Ground
    ground_color = (34, 139, 34)
    draw.rectangle([0, 500, width, height], fill=ground_color)
    
    # Path
    path_color = (160, 160, 160)
    draw.ellipse([300, 480, 500, 520], fill=path_color)
    
    # Trees (simple circles)
    tree_color = (0, 100, 0)
    tree_positions = [(100, 450), (200, 470), (600, 460), (700, 450)]
    for x, y in tree_positions:
        draw.ellipse([x-30, y-30, x+30, y+30], fill=tree_color)
    
    # Graduates (simple figures)
    graduate_positions = [(350, 400), (400, 400), (450, 400)]
    graduate_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue caps
    
    for i, (x, y) in enumerate(graduate_positions):
        # Body (black gown)
        draw.rectangle([x-15, y, x+15, y+60], fill=(50, 50, 50))
        # Head
        draw.ellipse([x-10, y-20, x+10, y], fill=(255, 220, 177))
        # Graduation cap
        cap_color = graduate_colors[i]
        draw.rectangle([x-12, y-25, x+12, y-15], fill=cap_color)
        draw.rectangle([x-8, y-30, x+8, y-25], fill=cap_color)
    
    # Add some decorative elements
    # Clouds
    cloud_color = (255, 255, 255)
    draw.ellipse([100, 50, 180, 100], fill=cloud_color)
    draw.ellipse([130, 40, 210, 90], fill=cloud_color)
    draw.ellipse([600, 60, 680, 110], fill=cloud_color)
    draw.ellipse([630, 50, 710, 100], fill=cloud_color)
    
    return img

def embed_text_in_channel(img, text, channel, method='lsb'):
    """Embed teks dalam specific color channel"""
    img_array = np.array(img)
    
    # Convert text to binary
    binary_text = ''.join([format(ord(char), '08b') for char in text])
    binary_text += '1111111111111110'  # End marker
    
    print(f"📝 Embedding '{text}' in {['Red', 'Green', 'Blue'][channel]} channel using {method}")
    print(f"📊 Binary length: {len(binary_text)} bits")
    
    bit_index = 0
    rows, cols, channels = img_array.shape
    
    if method == 'lsb':
        # LSB method
        for row in range(rows):
            for col in range(cols):
                if bit_index < len(binary_text):
                    pixel_value = img_array[row, col, channel]
                    bit = int(binary_text[bit_index])
                    
                    # Modify LSB
                    img_array[row, col, channel] = (pixel_value & 0xFE) | bit
                    bit_index += 1
                else:
                    break
            if bit_index >= len(binary_text):
                break
    
    elif method == 'msb':
        # MSB method (more obvious in Stegsolve)
        for row in range(rows):
            for col in range(cols):
                if bit_index < len(binary_text):
                    pixel_value = img_array[row, col, channel]
                    bit = int(binary_text[bit_index])
                    
                    # Modify MSB
                    if bit:
                        img_array[row, col, channel] = pixel_value | 0x80
                    else:
                        img_array[row, col, channel] = pixel_value & 0x7F
                    bit_index += 1
                else:
                    break
            if bit_index >= len(binary_text):
                break
    
    return Image.fromarray(img_array)

def create_visual_message(img, message, channel_bit=0):
    """Buat pesan yang terlihat visual di bit plane tertentu"""
    img_array = np.array(img)
    
    # Create text overlay
    overlay = Image.new('RGB', img.size, color=(0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
    except:
        font = ImageFont.load_default()
    
    # Position text in center
    bbox = draw.textbbox((0, 0), message, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (img.size[0] - text_width) // 2
    y = (img.size[1] - text_height) // 2 - 50  # Move up a bit
    
    # Draw text
    draw.text((x, y), message, fill=(255, 255, 255), font=font)
    
    # Add decorative border
    border_thickness = 5
    draw.rectangle([x-20, y-20, x+text_width+20, y+text_height+20], 
                  outline=(255, 255, 255), width=border_thickness)
    
    overlay_array = np.array(overlay)
    
    # Embed visual message in specific bit plane
    for row in range(img_array.shape[0]):
        for col in range(img_array.shape[1]):
            if overlay_array[row, col, 2] > 128:  # White pixels
                # Set bit in specific channel and bit position
                img_array[row, col, 2] = img_array[row, col, 2] | (1 << channel_bit)
            else:
                # Clear bit
                mask = ~(1 << channel_bit) & 0xFF
                img_array[row, col, 2] = img_array[row, col, 2] & mask
    
    return Image.fromarray(img_array)

def create_pattern_in_channel(img, channel, bit_plane):
    """Buat pola geometric yang terlihat di bit plane"""
    img_array = np.array(img)
    rows, cols, channels = img_array.shape
    
    # Create checkerboard pattern in specific areas
    for row in range(50, 150):  # Top area
        for col in range(50, 150):
            if (row + col) % 2 == 0:
                img_array[row, col, channel] = img_array[row, col, channel] | (1 << bit_plane)
            else:
                mask = ~(1 << bit_plane) & 0xFF
                img_array[row, col, channel] = img_array[row, col, channel] & mask
    
    # Create diagonal lines
    for i in range(min(rows, cols)):
        if i < rows and i < cols:
            img_array[i, i, channel] = img_array[i, i, channel] | (1 << bit_plane)
            if i + 100 < cols:
                img_array[i, i + 100, channel] = img_array[i, i + 100, channel] | (1 << bit_plane)
    
    return Image.fromarray(img_array)

def main():
    print("🎨 Membuat HTC-FORENSIC-002: Advanced Steganography Challenge...")
    
    # Create output directory
    output_dir = "/home/kali/htc_cybersecurity_challenges/htc_forensics_challenges/htc-forensic-002"
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Create base graduation photo
    print("📷 Membuat foto wisuda HTC...")
    base_img = create_graduation_photo()
    
    # 2. Multiple hidden messages with different techniques
    
    # Message 1: Visual message in Blue channel bit 0 (easy to spot)
    print("👁️ Menambah visual message...")
    visual_msg = "SELAMAT WISUDA!"
    img_with_visual = create_visual_message(base_img, visual_msg, 0)
    
    # Message 2: LSB in Red channel (main flag)
    print("🔐 Embedding main flag...")
    main_flag = "HTC{multi_layer_stego_master_2024}"
    img_with_flag = embed_text_in_channel(img_with_visual, main_flag, 0, 'lsb')
    
    # Message 3: MSB in Green channel (additional message)
    print("🎯 Adding secondary message...")
    secondary_msg = "CONGRATULATIONS_GRADUATES"
    img_with_secondary = embed_text_in_channel(img_with_flag, secondary_msg, 1, 'msb')
    
    # Message 4: Pattern in Green channel bit 2
    print("🔺 Creating geometric patterns...")
    final_img = create_pattern_in_channel(img_with_secondary, 1, 2)
    
    # 3. Save the final image
    output_path = os.path.join(output_dir, "htc-forensic-002-wisuda.jpg")
    final_img.save(output_path, "JPEG", quality=95)
    
    print(f"✅ Challenge image created: {output_path}")
    print(f"📊 Image size: {final_img.size}")
    print(f"🔍 Hidden messages:")
    print(f"   1. Visual: '{visual_msg}' - Blue plane 0")
    print(f"   2. Main flag: '{main_flag}' - Red LSB")
    print(f"   3. Secondary: '{secondary_msg}' - Green MSB") 
    print(f"   4. Patterns: Geometric shapes - Green plane 2")
    
    print("\n📋 Instructions for students:")
    print("1. Use Stegsolve to analyze different bit planes")
    print("2. Blue plane 0: Visual message")
    print("3. Green plane 2: Geometric patterns") 
    print("4. Data extract from Red LSB: Main flag")
    print("5. Data extract from Green MSB: Secondary message")
    
    print("\n🎯 Challenge is ready!")
    
    # Create a smaller version for faster analysis
    thumbnail = final_img.resize((400, 300), Image.Resampling.LANCZOS)
    thumb_path = os.path.join(output_dir, "htc-forensic-002-wisuda-small.jpg")
    thumbnail.save(thumb_path, "JPEG", quality=85)
    print(f"📱 Thumbnail created: {thumb_path}")

if __name__ == "__main__":
    main()
