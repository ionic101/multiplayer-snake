import os
import sys


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
GAME_NAME = 'Snake'
MAX_FPS = 60
CELL_WIDTH = 20

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
EXE_PATH = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False)\
    else os.path.abspath(os.path.dirname(__file__))
FONT_PATH = os.path.join(BASE_PATH, 'content', 'fonts', '8bit.ttf')
ICON_PATH = os.path.join(BASE_PATH, 'content', 'icons', 'icon.ico')
RECORD_PATH = os.path.join(EXE_PATH, 'data', 'record.pickle')

SERVER_IP = '127.0.0.1'
SERVER_PORT = 7000
