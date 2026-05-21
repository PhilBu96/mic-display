# 🎤 Mic Mute Overlay

A lightweight Windows desktop overlay that shows your microphone mute status in real time.

Built with **Python**, **PySide6 (Qt)** and **pycaw**.

---

## ✨ Features

- Real-time microphone mute detection (system audio state via pycaw)
- Smooth fade-in / fade-out UI transitions
- Always-on-top transparent overlay
- Click-through window (does not block mouse input)
- Borderless, frameless HUD-style UI
- SVG-based icons (fully scalable, crisp on any resolution)
- Bottom-right screen positioning
- Low CPU usage via lightweight polling loop

---

## 🎬 UI Behavior

The overlay behaves like a minimal HUD element:

- Appears instantly when microphone state changes
- Smooth fade-in animation on activation
- Automatically fades out after inactivity
- No abrupt show/hide transitions

---

## 🧠 How it works

The application continuously monitors the microphone state and updates the overlay only when a change occurs.

Flow:

QTimer (polling loop)
↓
check_mute()
↓
get system mic state (pycaw)
↓
state changed?
↓
update SVG icon
↓
trigger fade-in animation
↓
start auto-hide timer
↓
fade-out animation → hide widget

Only state changes trigger UI updates and animations.

---

## 🖥️ Requirements

- Python 3.10+
- Windows (uses Windows Core Audio APIs via pycaw)

---

## 📦 Dependencies

Install required packages:

pip install PySide6 pycaw comtypes

---

## 🚀 How to run

python main.py

---

## 📁 Project structure

mic-display/
│
├── main.py
│
└── app/
    ├── overlay.py
    ├── audio_monitor.py
    └── assets/
        ├── mute_icon.svg
        └── unmute_icon.svg

---

## 🛠️ Planned improvements

- Multi-monitor support improvements
- Startup autostart integration
- State machine refactor (for cleaner animation handling)
- Optional voice level visualization (future idea)

---

## 🧪 Project status

Stable early-stage prototype with working overlay system and smooth UI transitions.

---

## 📜 License

Free to use and modify.