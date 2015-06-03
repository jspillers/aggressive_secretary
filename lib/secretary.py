import sgc
from sgc.locals import *
import pygame
from pygame.locals import *
import logging
from background_images import *
from click_tracker import *
from incrementable_counter import *

log_format = '%(asctime)-6s: %(name)s - %(levelname)s - %(message)s'
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

pygame.display.init()
pygame.font.init()

screen = sgc.surface.Screen((800,480))

clock = pygame.time.Clock()

bg_image = BackgroundImages(pygame, screen, logger)
click_tracks = ClickTrackers(pygame, screen, sgc, logger)

corp_credits = IncrementableCounter(pygame, sgc, 'credits', 20, 200)
corp_handsize = IncrementableCounter(pygame, sgc, 'corp_handsize', 200, 200)
corp_bad_publicity = IncrementableCounter(pygame, sgc, 'bad_publicity', 20, 400, 0, 18)

runner_credits = IncrementableCounter(pygame, sgc, 'credits', 420, 200)
runner_handsize = IncrementableCounter(pygame, sgc, 'runner_handsize', 620, 200)
runner_brain_damage = IncrementableCounter(pygame, sgc, 'brain_damage', 420, 400, 0, 12)
runner_memory_units = IncrementableCounter(pygame, sgc, 'memory_units', 620, 400, 16, 25)
runner_tags = IncrementableCounter(pygame, sgc, 'tags', 620, 300, 0, 12)

while True:
    time = clock.tick(30)

    for e in pygame.event.get():
        sgc.event(e)
        if e.type == GUI:
            click_tracks.click_event(e)

        if e.type == QUIT:
            exit()

        # toggle fullscreen with alt + enter
        if (e.type is KEYDOWN and e.key == K_RETURN
                and (e.mod&(KMOD_LALT|KMOD_RALT)) != 0):
            if screen.get_flags() & FULLSCREEN:
                pygame.display.set_mode(screen.get_size())
            else:
                pygame.display.set_mode(screen.get_size(), pygame.FULLSCREEN)


    screen.fill((0,0,0))
    bg_image.cycle_images()
    click_tracks.update()
    sgc.update(time)
    pygame.display.flip()

