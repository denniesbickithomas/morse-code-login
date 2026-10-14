# Morse Code Gaze-Tracking Login System

A desktop authentication system that combines **face recognition**, **gaze-tracking**, and **Morse code input** to log users in instead of typing a password, users blink or look in patterns that are decoded into Morse code and matched against their credentials.

## Features

- **Face recognition login** — uses OpenCV's LBPH face recognizer to verify identity via webcam before granting access.
- **Gaze/eye-tracking Morse input** — uses `dlib`'s facial landmark detection to track eye movement and translate blink/gaze patterns into Morse code.
- **Mouse-click Morse input** — an alternative input mode using timed mouse clicks instead of gaze tracking.
- **User registration** — captures and stores face samples for new users, training the recognition model.
- **Telegram bot integration** — sends login notifications/alerts via a Telegram bot.
- **Tkinter-based GUI** — simple desktop interface for registration and login flows.

## Tech Stack

- Python 3.7
- OpenCV (`opencv-contrib-python`) — face detection & recognition
- dlib — facial landmark detection for gaze tracking
- Tkinter & PyQt5 — GUI
- pandas — user data handling
- telepot — Telegram bot integration
- Pillow — image handling

## Project Structure
```
├── Morse_login.py                       # Main entry point: login/register GUI
├── Register.py                          # User registration: captures face samples & trains the model
├── login.py                             # Standalone face-recognition login flow
├── gaze.py                              # Gaze/blink tracking demo
├── mouse-clicks-morse.py                # Mouse-click based Morse input
├── morse_converter.py                   # Morse code encoding/decoding logic
├── attachem.py                          # Email alert helper (snapshot attachment)
├── msg.py / sam.py                      # Post-login message screen / Telegram test script
├── haarcascade_frontalface_default.xml  # OpenCV face detection model
├── config.example.py                    # Template for your local secrets
├── requirements.txt                     # Python dependencies
└── *.jpg / *.png                        # GUI images
```

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/denniesbickithomas/morse-code-login.git
cd morse-code-login
```

### 2. Create a Python 3.7 virtual environment
This project was built and tested on **Python 3.7** — newer versions (3.9+) may hit dependency conflicts with `dlib` and `PyQt5`.
```bash
python -m venv venv37
venv37\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
> On Windows, `dlib` and `PyQt5-sip` often fail to build from source without Visual C++ Build Tools. Prebuilt wheels are recommended instead — see [dlib Windows wheels](https://github.com/sachadee/Dlib) and pin `PyQt5==5.15.4` with `PyQt5-sip==12.9.0` if you hit build errors.

### 4. Add your own `config.py`
This project sends alerts through a Telegram bot and, optionally, email and Twilio. Copy the template and fill in your own values. `config.py` is gitignored and never committed.
```bash
copy config.example.py config.py     # Windows
cp config.example.py config.py       # macOS / Linux
```
Keys: `BOT_TOKEN`, `TELEGRAM_CHAT_ID`, and optionally `EMAIL_USER`, `EMAIL_APP_PASSWORD`, `ALERT_EMAIL_TO`, `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`.

### 5. Run the app
```bash
python Morse_login.py
```

## Notes

- The `dataset/`, `trainer.yml`, `UserDetails.csv`, `frame.png` and per-user `*.txt` credential files are excluded from this repo since they contain personal face data and user records generated locally when you register. They'll be created automatically the first time you register a user.
- `shape_predictor_68_face_landmarks.dat` (the dlib facial landmark model) is also excluded due to its size — download it from [dlib's model repository](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) and place it in the project root.

## Team Project

Built as a team project exploring accessible, alternative authentication methods using computer vision and Morse code.

### Contributors

| Name | GitHub |
|---|---|
| **Dennies Bicki Thomas** | [@denniesbickithomas](https://github.com/denniesbickithomas) |
| **Abhishek Ravikumar** | [@abhir271](https://github.com/abhir271) |

> **Security note:** this is an academic prototype. User passwords are stored in plain-text files on the local machine, so don't use it to protect real accounts.
