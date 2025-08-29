# Python Project Template

Clean Python project template with best practices and development tools.

## Features

- 📦 Virtual environment setup
- 🔧 Environment variable configuration
- 📝 Type hints and modern Python features
- 🧪 pytest for testing
- 🖤 Black for code formatting
- 📏 Flake8 for linting
- 🔍 MyPy for type checking
- 📋 Comprehensive logging

## Getting Started

1. Copy this template to your project directory
2. Run the setup script:
   ```bash
   ./setup.sh
   ```
3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
4. Run the application:
   ```bash
   python src/main.py
   ```

## Manual Setup

If you prefer to set up manually:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env
```

## Available Commands

- `python src/main.py` - Run the application
- `pytest` - Run tests
- `black .` - Format code
- `flake8` - Check code style
- `mypy src/` - Type checking

## Project Structure

```
src/                 # Source code
tests/               # Test files
docs/                # Documentation
scripts/             # Utility scripts
requirements.txt     # Dependencies
.env.example         # Environment template
```