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
    GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
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
        self.buttons_pressed = { 
            '2': False, '3': False, '18': False, '23': False 
        }

    def call(self, time):
        global GPIO

        if GPIO:
            def on_press_18():
                self.click_tracks.trackers['runner'].handle_click()
                self.click_tracks.click_event()

            self.__handle_gpio_press(18, on_press_18)

            def on_press_23():
                self.click_tracks.trackers['corp'].handle_click()
                self.click_tracks.click_event()

            self.__handle_gpio_press(23, on_press_23)

            def on_press_2():
                self.logger.info('press 2')

            self.__handle_gpio_press(2, on_press_2)

            def on_press_3():
                self.logger.info('press 3')

            self.__handle_gpio_press(3, on_press_3)

        for e in self.pygame.event.get():
            self.sgc.event(e)
            self.__handle_event(e)

    def __handle_gpio_press(self, pin_num, on_press):
        button_input_state = GPIO.input(pin_num)
        if button_input_state == False:
            if self.buttons_pressed[str(pin_num)] == False:
                self.logger.info('button press on pin ' + str(pin_num))
                self.buttons_pressed[str(pin_num)] = True
                on_press()
        else:
            self.buttons_pressed[str(pin_num)] = False
        

    def __handle_event(self, e):
        if e.type == GUI:
            self.logger.info(e)
            self.click_tracks.click_event()

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


