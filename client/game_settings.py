import os


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
GAME_NAME = 'Snake'
MAX_FPS = 60
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(BASE_PATH, 'content', 'fonts', '8bit.otf')
RECORD_PATH = os.path.join(BASE_PATH, 'data', 'record.pickle')

CELL_WIDTH = 20
