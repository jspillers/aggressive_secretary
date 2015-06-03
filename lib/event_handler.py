import sgc
from sgc.locals import *
import pygame
from pygame.locals import *

TURN_ENDED = USEREVENT + 1

class EventHandler():
    def __init__(self, **kwargs):
        self.gpio = kwargs['gpio'] if 'gpio' in kwargs else False
        self.pygame = kwargs['pygame']
        self.screen = kwargs['screen']
        self.sgc = kwargs['sgc']
        self.click_tracks = kwargs['click_tracks']
        self.bg_images = kwargs['bg_images']

    def call(self, time):
        for e in self.pygame.event.get():
            self.sgc.event(e)
            self.__handle_event(e)

    def __handle_event(self, e):
        if self.gpio:
            button_18_input_state = self.gpio.input(18)
            if button_18_input_state == False:
                print('Button Pressed')

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


