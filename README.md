# 🎤 Mic Mute Overlay

A lightweight Windows overlay that displays the current microphone mute status in real time.

Built with **Python**, **PySide6 (Qt)** and **pycaw**.

---

## ✨ Features

- Real-time microphone mute detection
- Always-on-top desktop overlay
- Transparent, borderless window
- Minimal CPU usage (event-based via QTimer)
- SVG-based icons (fully scalable)
- Positioned in bottom-right corner of the screen

---

## 🧠 How it works

The app periodically checks the system microphone state using `pycaw` and updates a Qt-based overlay accordingly.

Flow:

```
QTimer (300ms)
    ↓
check_mute()
    ↓
get system mic state (pycaw)
    ↓
detect state change
    ↓
update SVG icon (mute / unmute)
```

Only changes in state trigger UI updates.

---

## 🖥️ Requirements

- Python 3.10+
- Windows (uses Windows Core Audio APIs via pycaw)

---

## 📦 Dependencies

Install required packages:

```bash
pip install PySide6 pycaw comtypes
```

---

## 🚀 How to run

```bash
python main.py
```

Make sure your folder structure looks like this:

```
mic-display/
│
├── main.py
│
└── app/
    ├── overlay.py
    ├── audio_monitor.py
    │
    └── assets/
        ├── mute_icon.svg
        └── unmute_icon.svg
```
## 🎯 Current behavior

- Bottom-right overlay on screen
- Updates every 300ms
- Shows:
  - muted icon when microphone is muted
  - unmuted icon otherwise

---

## 🛠️ Planned improvements

- Fade-in / fade-out animation
- Better state handling & structure refactor
- Multi-monitor support improvements
- Startup autostart integration

---

## 🧪 Project status

Early prototype — but fully functional.

---

## 📜 License

Free to use and modify.