#!/bin/bash

# HTC CyberSec Academy - Web Portal Launcher
# Script untuk menjalankan platform web Streamlit

echo "🛡️ HTC CyberSec Academy - Web Portal Launcher"
echo "=============================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 tidak ditemukan! Silakan install Python 3 terlebih dahulu."
    exit 1
fi

echo "✅ Python 3 detected: $(python3 --version)"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 tidak ditemukan! Silakan install pip terlebih dahulu."
    exit 1
fi

echo "✅ pip3 detected"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install requirements if not already installed
echo "📦 Installing dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "⚠️  Some dependencies may not be installed properly. Continuing..."
fi

# Change to portal directory
cd "$(dirname "$0")"

echo ""
echo "🚀 Starting HTC CyberSec Academy Web Portal..."
echo "📱 Portal akan terbuka di: http://localhost:8501"
echo "🔗 Untuk akses dari device lain: http://$(hostname -I | awk '{print $1}'):8501"
echo ""
echo "💡 Tips:"
echo "   - Gunakan Ctrl+C untuk menghentikan portal"
echo "   - Refresh browser jika ada perubahan code"
echo "   - Check terminal untuk logs dan error"
echo ""

# Run Streamlit app
streamlit run app.py \
    --server.port=8501 \
    --server.address=0.0.0.0 \
    --browser.gatherUsageStats=false \
    --server.headless=true

echo ""
echo "👋 Portal HTC CyberSec Academy telah dihentikan."
echo "🙏 Terima kasih telah menggunakan platform kami!"
