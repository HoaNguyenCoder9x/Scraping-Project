#!/bin/bash
# Python 3.10.12
# Check if a Python interpreter is provided, otherwise default to 'python3'
PYTHON=${1:-python3}

# Name of the virtual environment directory
VENV_DIR="venv"

# Create a virtual environment
$PYTHON -m venv $VENV_DIR

# Check if the virtual environment was created successfully
if [ ! -d "$VENV_DIR" ]; then
  echo "Failed to create virtual environment"
  exit 1
fi

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Check if a requirements file is provided
if [ -f "requirements.txt" ]; then
  # Install the dependencies
  pip install -r requirements.txt
else
  echo "requirements.txt not found. No dependencies installed."
fi

# Confirm the setup
echo "Virtual environment setup complete. To activate it, run:"
echo "source $VENV_DIR/bin/activate"
echo "To run the project"
echo "step 1: cd glamira/glamira "
echo "step 2: python3 spiders/production/glamira_dev.py"
echo "the data jsonl will be located at glamira/glamira/data"
echo "the image will be located at glamira/glamira/image"
