# ⚡ GridLock F1

A futuristic Formula 1 dashboard for the **2026 season** — featuring all 11 teams, 22 drivers, and the biggest regulation overhaul in F1 history.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1-000000?logo=flask&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue)

## 🏎️ Features

- **Home** — Animated hero, season stats, featured teams, and 2026 regulation highlights
- **2026 Grid** — All 11 constructors and 22 drivers with team colour accents
- **About** — Project info, tech stack, regulation timeline, and F1 trivia
- Apple-style **dark mode** with glassmorphism, smooth scroll animations, and electric blue accents
- Fully **responsive** design (mobile, tablet, desktop)
- Custom **SVG favicon** (checkered flag)

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/gridlock-f1.git
cd gridlock-f1

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run the dev server
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## 📁 Project Structure

```
my-slushie-app/
├── app.py                 # Flask app & routes
├── requirements.txt       # Python dependencies
├── vercel.json            # Vercel deployment config
├── static/
│   ├── css/main.css       # Design system & styles
│   ├── js/main.js         # Animations & interactions
│   └── favicon.svg        # Checkered flag favicon
└── templates/
    ├── base.html          # Shared layout (nav, footer)
    ├── index.html         # Home page
    ├── grid.html          # 2026 F1 Grid
    └── about.html         # About page
```

## 🛠️ Tech Stack

| Layer    | Technology                 |
| -------- | -------------------------- |
| Backend  | Python 3.9+ / Flask 3.1    |
| Frontend | Vanilla HTML, CSS, JS      |
| Fonts    | Inter, Space Grotesk       |
| Deploy   | Vercel (serverless Python) |

## 🌐 Deployment

This project is configured for **Vercel** out of the box:

1. Push your code to GitHub
2. Import the repo on [vercel.com](https://vercel.com)
3. Vercel will auto-detect `vercel.json` and deploy

## 📄 License

MIT — built for [Hack Club Slushies](https://hackclub.com).
