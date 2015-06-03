import sys
import sgc
from sgc.locals import *
import pygame
from pygame.locals import *

TURN_ENDED = USEREVENT + 1

if sys.platform != 'darwin':
    import RPi.GPIO as GPIO

try:
    GPIO
except NameError:
    GPIO = False
else:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class EventHandler():
    def __init__(self, **kwargs):
        self.pygame = kwargs['pygame']
        self.screen = kwargs['screen']
        self.sgc = kwargs['sgc']
        self.logger = kwargs['logger']
        self.click_tracks = kwargs['click_tracks']
        self.bg_images = kwargs['bg_images']
        self.buttons_pressed = { '18': False, '23': False }

    def call(self, time):
        global GPIO

        for e in self.pygame.event.get():
            self.sgc.event(e)
            self.__handle_event(e)

        if GPIO:
            button_18_input_state = GPIO.input(18)
            if button_18_input_state == False:
                if self.buttons_pressed['18'] == False:
                    self.logger.info('18 button press')
                    self.buttons_pressed['18'] = True
            else:
                self.buttons_pressed['18'] = False

            button_23_input_state = GPIO.input(23)
            if button_23_input_state == False:
                if self.buttons_pressed['23'] == False:
                    self.logger.info('23 button press')
                    self.buttons_pressed['23'] = True
            else:
                self.buttons_pressed['23'] = False


    def __handle_event(self, e):
        if e.type == GUI:
            self.click_tracks.click_event(e)

        if e.type == TURN_ENDED:
            self.bg_images.display_next_bg_image()

        if e.type == QUIT:
            exit()

        # toggle fullscreen with alt + enter
        if (e.type is KEYDOWN and e.key == K_RETURN
                and (e.mod&(KMOD_LALT|KMOD_RALT)) != 0):
            if self.screen.get_flags() & FULLSCREEN:
                self.pygame.display.set_mode(self.screen.get_size())
            else:
                self.pygame.display.set_mode(self.screen.get_size(), self.pygame.FULLSCREEN)


