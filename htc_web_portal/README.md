# 🛡️ HTC CyberSec Academy - Web Portal

## 🌟 Platform Challenge Cybersecurity Berbasis Web

Web portal ini merupakan interface modern untuk framework HTC CyberSec Academy, memungkinkan mahasiswa mengakses challenge cybersecurity melalui web browser dengan pengalaman yang interactive dan engaging.

---

## ✨ Features

### 🎯 **Core Features**
- ✅ **Interactive Challenge System** - Submit flags dan dapat feedback real-time
- ✅ **Progressive Hint System** - Hint bertahap dengan penalty system
- ✅ **Real-time Leaderboard** - Kompetisi sehat antar mahasiswa
- ✅ **Badge Achievement System** - Gamifikasi untuk motivasi
- ✅ **Progress Tracking** - Monitor perkembangan individual

### 🎨 **User Experience**
- 🌐 **Responsive Design** - Bekerja di desktop, tablet, dan mobile
- 🇮🇩 **Full Indonesian Language** - Interface 100% Bahasa Indonesia
- 🎮 **Gamified Learning** - Poin, badge, ranking untuk engagement
- 📊 **Visual Analytics** - Charts dan statistik progress
- 🚀 **Modern UI/UX** - Clean dan professional interface

### 🔧 **Technical Features**
- ⚡ **Streamlit-based** - Fast, responsive web application
- 💾 **Persistent Data** - JSON-based database (dapat upgrade ke SQL)
- 🔐 **Session Management** - Login system untuk mahasiswa
- 📱 **Multi-device Access** - Akses dari berbagai device
- 🌐 **Network Accessible** - Dapat diakses melalui jaringan lokal

---

## 🚀 Quick Start

### Method 1: One-Click Launch
```bash
cd /home/kali/htc_cybersecurity_challenges/htc_web_portal
./run_portal.sh
```

### Method 2: Manual Setup
```bash
# Install dependencies
pip3 install -r requirements.txt

# Run application
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
```

### Method 3: Background Service
```bash
# Run in background
nohup streamlit run app.py --server.port=8501 --server.address=0.0.0.0 &

# Check process
ps aux | grep streamlit

# Kill process
pkill -f streamlit
```

---

## 📱 Akses Portal

### Local Access
- **URL**: http://localhost:8501
- **Description**: Akses dari komputer yang menjalankan portal

### Network Access
- **URL**: http://[IP-ADDRESS]:8501
- **Description**: Akses dari device lain dalam jaringan
- **Find IP**: `hostname -I | awk '{print $1}'`

### Example URLs
```
http://192.168.1.100:8501  # Dari device lain di jaringan
http://10.0.0.50:8501      # Dari jaringan kampus
http://kali.local:8501     # Menggunakan hostname
```

---

## 👥 User Flow

### 1. **Pendaftaran/Login** (2 menit)
- Akses halaman "📝 Daftar/Login"
- Pilih tab "🆕 Daftar Baru" untuk registrasi
- Input NIM, Nama, Email (opsional)
- Atau gunakan tab "🔑 Login" jika sudah terdaftar

### 2. **Explore Challenges** (5 menit)
- Kunjungi halaman "🎯 Challenge"
- Browse available challenges per kategori
- Baca deskripsi dan learning objectives
- Gunakan hint system jika diperlukan

### 3. **Submit Flags** (Variable)
- Solve challenge menggunakan tools/methods
- Input flag dalam format HTC{...}
- Submit dan dapat feedback instant
- Earn points dan badges

### 4. **Track Progress** (1 menit)
- Check "👤 Profil Saya" untuk personal stats
- Monitor "🏆 Leaderboard" untuk ranking
- Review badge collection dan progress

---

## 🎓 Untuk Instruktur

### Setup Kelas

1. **Pre-class Setup** (5 menit)
```bash
# Start portal
cd htc_web_portal
./run_portal.sh

# Share access URL with students
echo "Portal URL: http://$(hostname -I | awk '{print $1}'):8501"
```

2. **Student Registration** (10 menit)
- Students access portal via shared URL
- Mass registration: NIM + Nama
- Quick demo of interface

3. **Challenge Introduction** (15 menit)
- Demo hint system usage
- Show submission process  
- Explain point/penalty system
- Encourage healthy competition

### Monitoring Students

```python
# Quick stats check (dalam Python console)
import json
with open('htc_portal_data.json', 'r') as f:
    data = json.load(f)

print(f"Total students: {len(data['students'])}")
print(f"Total submissions: {len(data['submissions'])}")

# Top performers
students = sorted(data['students'].items(), 
                 key=lambda x: x[1]['total_points'], reverse=True)
for nim, student in students[:3]:
    print(f"{student['nama']}: {student['total_points']} points")
```

---

## 🔧 Configuration & Customization

### Port Configuration
```bash
# Change default port (8501)
streamlit run app.py --server.port=9000

# Multiple instances
streamlit run app.py --server.port=8502 &
streamlit run app.py --server.port=8503 &
```

### Adding New Challenges
```python
# Edit app.py - add to self.challenges dictionary
"HTC-WEB-002": {
    "name": "XSS Challenge", 
    "points": 200, 
    "category": "Web Security",
    "difficulty": "Sedang",
    "flag": "HTC{xss_master_2024}",
    "description": "Find XSS vulnerability in comment system",
    "hints": [
        "Look for input fields",
        "Try script injection",
        "Check for output encoding",
        "Payload: <script>alert('XSS')</script>"
    ]
}
```

### Custom Styling
```css
/* Edit CSS dalam load_custom_css() function */
.custom-theme {
    background: linear-gradient(135deg, #your-colors);
    color: #your-text-color;
}
```

---

## 📊 Analytics & Insights

### Built-in Analytics
- **Real-time leaderboard** - Top performers tracking
- **Challenge completion rates** - Popular/difficult challenges  
- **Hint usage statistics** - Learning pattern analysis
- **Activity timeline** - Peak usage times
- **Badge distribution** - Achievement analysis

### Export Data
```python
# Export student data
import json
import pandas as pd

with open('htc_portal_data.json', 'r') as f:
    data = json.load(f)

# Convert to DataFrame for analysis
students_df = pd.DataFrame.from_dict(data['students'], orient='index')
submissions_df = pd.DataFrame(data['submissions'])

# Export to CSV
students_df.to_csv('students_data.csv')
submissions_df.to_csv('submissions_data.csv')
```

---

## 🛡️ Security Considerations

### Current Security Level: **Educational**
- ✅ Basic input validation
- ✅ Session state management
- ✅ No sensitive data exposure
- ⚠️ Simple authentication (NIM-based)
- ⚠️ No encryption for stored data

### Production Security Upgrades
```python
# For production deployment, consider:
- Database encryption
- Proper authentication system
- HTTPS/SSL configuration  
- Input sanitization
- Rate limiting
- Audit logging
```

---

## 🐛 Troubleshooting

### Common Issues

**Portal tidak bisa diakses dari device lain:**
```bash
# Pastikan binding ke 0.0.0.0, bukan localhost
streamlit run app.py --server.address=0.0.0.0

# Check firewall
sudo ufw allow 8501
```

**Dependencies error:**
```bash
# Upgrade pip
pip3 install --upgrade pip

# Install specific versions
pip3 install streamlit==1.28.0 pandas==2.0.0
```

**JSON file corruption:**
```bash
# Backup dan reset database
cp htc_portal_data.json htc_portal_data.json.backup
echo '{"students": {}, "submissions": []}' > htc_portal_data.json
```

### Performance Tips
- **Large class (50+ students)**: Consider using external database
- **Network latency**: Deploy closer to students (local server)
- **Concurrent access**: Streamlit handles ~20 concurrent users well

---

## 🚀 Deployment Options

### 1. **Local Development** (Current)
- ✅ Quick setup dan testing
- ✅ Full control
- ❌ Limited to local network

### 2. **Cloud Deployment** (Streamlit Cloud)
```bash
# Push to GitHub repository
git add .
git commit -m "HTC CyberSec Academy Portal"
git push origin main

# Deploy via Streamlit Cloud
# https://share.streamlit.io/
```

### 3. **Docker Deployment**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
```

### 4. **University Server**
```bash
# Deploy to university server
scp -r htc_web_portal/ user@server.htc.ac.id:/var/www/
ssh user@server.htc.ac.id
cd /var/www/htc_web_portal
./run_portal.sh
```

---

## 📈 Roadmap & Future Enhancements

### Phase 1: Core Platform ✅
- [x] Basic challenge system
- [x] Student registration/login
- [x] Leaderboard dan badges
- [x] Progress tracking

### Phase 2: Enhanced Features 🚧
- [ ] Team-based challenges
- [ ] Time-limited competitions
- [ ] Advanced analytics dashboard
- [ ] Email notifications
- [ ] Export/import capabilities

### Phase 3: Professional Features 🔮
- [ ] Integration dengan LMS (Moodle, Canvas)
- [ ] Single Sign-On (SSO)
- [ ] Multi-tenant support
- [ ] Advanced security features
- [ ] Mobile app companion

---

## 🤝 Contributing

### Untuk Mahasiswa
- Report bugs via GitHub issues
- Suggest new challenge ideas
- Test pada different devices/browsers
- Provide UX/UI feedback

### Untuk Instruktur
- Contribute new challenges
- Share teaching methodologies
- Provide learning analytics insights
- Help dengan content creation

### Untuk Developer
- Code contributions via pull requests
- Performance optimizations
- Security enhancements
- New feature development

---

## 📞 Support & Community

### Technical Support
- **Email**: tech-support@htc.ac.id
- **Discord**: HTC CyberSec Community
- **Forum**: https://forum.cybersec.htc.ac.id

### Learning Support
- **Office Hours**: Senin-Jumat 09:00-17:00
- **Peer Study Groups**: Discord channels
- **Video Tutorials**: YouTube channel

---

## 🙏 Acknowledgments

Terima kasih kepada:
- **Streamlit Team** - Amazing framework
- **HTC Students** - Beta testing dan feedback
- **Open Source Community** - Dependencies dan inspiration
- **Cybersecurity Educators** - Pedagogical insights

---

## 🎉 **Web Portal HTC CyberSec Academy**
### *Making Cybersecurity Education Accessible, Engaging, and Fun!*

**🇮🇩 Mari bersama membangun generasi cybersecurity Indonesia yang kuat melalui teknologi dan inovasi! 🚀**

---

*Last updated: $(date)*
*Version: 1.0*
*Developed with ❤️ for Indonesian cybersecurity education*
