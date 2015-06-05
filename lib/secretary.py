import sys
import sgc
from sgc.locals import *
import pygame
from pygame.locals import *
import logging
from background_images import *
from click_tracker import *
from incrementable_counter import *
from event_handler import *

log_format = '%(asctime)-6s: %(name)s - %(levelname)s - %(message)s'
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

if sys.platform != 'darwin':
    USE_GUI = False
    logger.info('GPIO is present, system is ' + sys.platform)    
else:
    USE_GUI = True
    logger.info('GPIO is NOT present, system is ' + sys.platform)    

pygame.display.init()
pygame.font.init()

screen = sgc.surface.Screen((800,480))

clock = pygame.time.Clock()

# setup background and click trackers
bg_images = BackgroundImages(pygame, screen, logger)
click_tracks = ClickTrackers(pygame=pygame, screen=screen, sgc=sgc, use_gui=USE_GUI, logger=logger)

counters = {}

# ----- Corporation counters
counters['corp_credits'] = IncrementableCounter(
    pygame=pygame, sgc=sgc, counter_type='credits', 
    x_pos=20, y_pos=200, counter=5
)

counters['corp_handsize'] = IncrementableCounter(
    pygame=pygame, sgc=sgc, counter_type='corp_handsize', 
    x_pos=200, y_pos=200, counter=5
)

counters['corp_bad_publicity'] = IncrementableCounter(
    pygame=pygame, sgc=sgc, counter_type='bad_publicity', 
    x_pos=20, y_pos=400, x_adjust=0, y_adjust=18
)

# ----- Runner counters
counters['runner_credits'] = IncrementableCounter(
    pygame=pygame, sgc=sgc, counter_type='credits', 
    x_pos=420, y_pos=200, counter=5
)

counters['runner_handsize'] = IncrementableCounter(
    pygame=pygame, sgc=sgc, counter_type='runner_handsize', 
    x_pos=620, y_pos=200, counter=5
)

counters['runner_tags'] = IncrementableCounter(
    pygame=pygame, sgc=sgc, counter_type='tags', 
    x_pos=620, y_pos=300, x_adjust=0, y_adjust=12
)

counters['runner_brain_damage'] = IncrementableCounter(
    pygame=pygame, sgc=sgc, counter_type='brain_damage', 
    x_pos=420, y_pos=400, x_adjust=0, y_adjust=12
)

counters['runner_memory_units'] = IncrementableCounter(
    pygame=pygame, sgc=sgc, counter_type='memory_units', 
    x_pos=620, y_pos=400, x_adjust=16, y_adjust=25, counter=4
)

event_handler = EventHandler(
    pygame=pygame, sgc=sgc, screen=screen, 
    click_tracks=click_tracks, bg_images=bg_images, 
    counters=counters, logger=logger
)

while True:
    time = clock.tick(30)
    event_handler.call(time)
    screen.fill((0,0,0))

    bg_images.update()
    click_tracks.update()
    sgc.update(time)

    pygame.display.flip()

