#!/bin/bash

# Python Project Setup Script
echo "Setting up Python project..."

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Copy environment file
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
fi

echo "Setup complete!"
echo ""
echo "To activate the virtual environment:"
echo "  source venv/bin/activate"
echo ""
echo "To run the application:"
echo "  python src/main.py"
echo ""
echo "To run tests:"
echo "  pytest"