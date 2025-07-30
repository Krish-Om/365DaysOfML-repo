#!/bin/bash

# Download common ML datasets using Kaggle CLI
# Make sure you have kaggle CLI installed and configured

echo "🚀 Starting dataset downloads..."

# Create dataset directories
echo "📁 Creating dataset directories..."
mkdir -p input/{wine-reviews,titanic,house-prices}

# Check if kaggle is installed
if ! command -v kaggle &> /dev/null; then
    echo "❌ Kaggle CLI not found. Please install it first:"
    echo "   uv add kaggle  # or pip install kaggle"
    exit 1
fi

# Download datasets
echo "📥 Downloading wine reviews dataset..."
kaggle datasets download -d zynicide/wine-reviews -p input/wine-reviews --unzip

echo "📥 Downloading titanic dataset..."
kaggle datasets download -d c/titanic -p input/titanic --unzip

echo "📥 Downloading house prices dataset..."
kaggle datasets download -d c/house-prices-advanced-regression-techniques -p input/house-prices --unzip

echo "✅ All datasets downloaded successfully!"
echo "📋 Check datasets.json for more information about each dataset."
