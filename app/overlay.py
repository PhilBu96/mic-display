import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QWidget, QGraphicsOpacityEffect
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtCore import Qt, QTimer, QPropertyAnimation

from app import audio_monitor

# DONE: implement always on top
# DONE: smooth animation

# Overlay initializing
print("Initializing overlay...")
app = QApplication(sys.argv)
widget = QWidget()
widget.setWindowFlags(
    Qt.WindowType.FramelessWindowHint |
    Qt.WindowType.Tool |
    Qt.WindowType.WindowStaysOnTopHint |
    Qt.WindowType.WindowTransparentForInput)
widget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

# Animation creation
print("Initializing animations...")
opacity_effect = QGraphicsOpacityEffect()
widget.setGraphicsEffect(opacity_effect)
opacity_effect.setOpacity(1.0)

# Fade in
fade_in_anim = QPropertyAnimation(opacity_effect, b"opacity")
fade_in_anim.setDuration(250)
fade_in_anim.setStartValue(0)
fade_in_anim.setEndValue(1)

# Fade out
fade_out_anim = QPropertyAnimation(opacity_effect, b"opacity")
fade_out_anim.setDuration(1000)
fade_out_anim.setStartValue(1)
fade_out_anim.setEndValue(0)

# Get the screen resolution
print("Get screen resolution...")
screen = QApplication.primaryScreen().availableGeometry()
screen_width = screen.width()
screen_height = screen.height()
print(f"Screen width: {screen_width}, Screen height: {screen_height}")

# We want 6% screen width and 10% screen height
print("Calculating relative size...")
relative_screen_width = round(screen_width * 0.06)
relative_screen_height = round(screen_height * 0.1)
print(f"Relative screen width: {relative_screen_width}, Relative screen height: {relative_screen_height}")
widget.setFixedSize(relative_screen_width, relative_screen_height)

# Translating the overlay to the lower right corner of the display
print("Translating overlay...")
margin_x = 10
margin_y = 10
print(f"Margin x: {margin_x}, y: {margin_y}")
pos_x = screen_width - relative_screen_width - margin_x
pos_y = screen_height - relative_screen_height - margin_y
print(f"Pos x: {pos_x}, Pos y: {pos_y}")
widget.move(pos_x, pos_y)

# Loading SVGs
print("Loading SVG files...")
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
mute_icon = ASSETS_DIR / "mute_icon.svg"
print(f"Mute icon path: {mute_icon}")
unmute_icon = ASSETS_DIR / "unmute_icon.svg"
print(f"Unmute icon path: {unmute_icon}")

# SVG creation
svg = QSvgWidget(parent=widget)
svg.setFixedSize(relative_screen_width, relative_screen_height)
svg.show()
last_state = None

def start_fade_out():
    fade_out_anim.start()

hide_timer = QTimer(widget)
hide_timer.setSingleShot(True)
fade_out_anim.finished.connect(widget.hide)
hide_timer.timeout.connect(start_fade_out)


def run():
    widget.show()
    fade_in_anim.start()

    timer = QTimer(widget)
    timer.setInterval(500)
    timer.timeout.connect(check_mute)
    timer.start()

    sys.exit(app.exec())


# Function for the mute check
def check_mute():
    # print("Checking mute...")
    global last_state
    state = audio_monitor.get_mute_state()
    if state == last_state:
        return
    last_state = state
    # print(f"Mute state: {state}")
    draw_svg(svg, state)

    widget.show()
    fade_in_anim.start()
    hide_timer.start(3000)


# Function for SVG drawing
def draw_svg(vector, mode):
    print(f"Drawing SVG mode: {mode}...")
    if mode == 1:
        vector.load(str(mute_icon))

    elif mode == 0:
        vector.load(str(unmute_icon))
