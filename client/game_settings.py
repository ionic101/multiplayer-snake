import os
import sys


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
GAME_NAME = 'Snake'
MAX_FPS = 60

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
EXE_PATH = os.path.abspath(os.path.dirname(__file__))
if getattr(sys, 'frozen', False):
    EXE_PATH = os.path.dirname(sys.executable)   # type: ignore
FONT_PATH = os.path.join(BASE_PATH, 'content', 'fonts', '8bit.otf')
ICON_PATH = os.path.join(BASE_PATH, 'content', 'icons', 'icon.ico')
RECORD_PATH = os.path.join(EXE_PATH, 'data', 'record.pickle')

CELL_WIDTH = 20
