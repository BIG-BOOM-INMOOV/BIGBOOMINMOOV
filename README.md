# Big Boom InMoov

Code for DBHS InMoov's brain

## Features
- **Home Page:** Basic Information about the club and it's members
- **Head Manual:** Sliders which move all 3 motors in the head (vertical, horizontal, and mouth)
- **Hotdogs:** Uses robot's built-in camera to rotate head to look at objects

## Installation
Ensure you have Python 3.10+ installed. follow these steps to set up your local environment

### 1. Clone the Repository
```bash
git clone https://github.com
cd your-repo-name
```

### 2. Set Up a Virtual Environment
Always isolate your dependencies to prevent version conflicts.

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows (CMD/PowerShell):**
```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

### Running as a CLI Script
```bash
python main.py
```
