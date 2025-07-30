# Machine Learning Journey - Pandas Course

## Data Management with Kaggle CLI

This repository uses Kaggle CLI for efficient dataset management.

### Initial Setup

1. **Set up Python Environment**:

   **Option A: Using uv (recommended)**:
   ```bash
   # uv automatically manages virtual environments
   uv sync
   ```
   
   **Option B: Using pip with venv**:
   ```bash
   # Create virtual environment
   python -m venv .venv
   
   # Activate virtual environment
   # On Linux/Mac:
   source .venv/bin/activate
   # On Windows:
   # .venv\Scripts\activate
   
   # Install dependencies
   pip install -r pyproject.toml
   #or using uv
   uv add -r pyproject.toml
   # or install packages individually:
   # pip install pandas jupyter kaggle
   ```

2. **Install Kaggle CLI**:
   
   **Option A: Using uv (recommended)**:
   ```bash
   uv add kaggle 
   ```

   **Option B: Using pip**:
   ```bash
   pip install kaggle
   ```

3. **Setup Kaggle API credentials**:
   - Go to https://www.kaggle.com/account
   - Click "Create New API Token" to download `kaggle.json`
   - Place it in `~/.kaggle/kaggle.json`
   ```bash
   mkdir -p ~/.kaggle
   mv ~/Downloads/kaggle.json ~/.kaggle/
   chmod 600 ~/.kaggle/kaggle.json
   ```

### Directory Structure
```
input/
├── wine-reviews/
├── titanic/
├── house-prices/
└── ... (other kaggle datasets)
```

### Downloading Datasets

**General command format**:
```bash
kaggle datasets download -d <dataset-path> -p input/<folder-name> --unzip
```

**Example commands**:
```bash
# Wine reviews dataset
kaggle datasets download -d zynicide/wine-reviews -p input/wine-reviews --unzip

# Titanic dataset
kaggle datasets download -d c/titanic -p input/titanic --unzip

# House prices dataset
kaggle datasets download -d c/house-prices-advanced-regression-techniques -p input/house-prices --unzip
```

### Quick Dataset Setup Script

Run this to download commonly used datasets:
```bash
# Create directories
mkdir -p input/{wine-reviews,titanic,house-prices}

# Download datasets
kaggle datasets download -d zynicide/wine-reviews -p input/wine-reviews --unzip
kaggle datasets download -d c/titanic -p input/titanic --unzip
kaggle datasets download -d c/house-prices-advanced-regression-techniques -p input/house-prices --unzip
```

### Current Datasets

See `datasets.json` for the complete list of datasets and their Kaggle paths.

## Usage

Each notebook will specify which dataset it uses. Use the Kaggle CLI commands above to download required datasets before running.

## Getting Started

1. Clone this repository
2. Set up your Python environment and install dependencies:
   - **Option A (recommended)**: Use `uv sync` for automatic environment management
   - **Option B**: Create a virtual environment with `python -m venv .venv` and activate it
3. Install Kaggle CLI (see Initial Setup section above)
4. Set up Kaggle API credentials
5. Download datasets using `./download_datasets.sh` or individual commands
6. Start with the exercise notebooks