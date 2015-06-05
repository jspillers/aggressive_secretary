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
    # setup pins 2 through 19
    for pin_num in list(range(2,20)):
        GPIO.setup(pin_num, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class EventHandler():
    def __init__(self, **kwargs):
        self.pygame = kwargs['pygame']
        self.screen = kwargs['screen']
        self.sgc = kwargs['sgc']
        self.logger = kwargs['logger']
        self.click_tracks = kwargs['click_tracks']
        self.bg_images = kwargs['bg_images']
        self.counters = kwargs['counters']

        self.buttons_pressed = {}
        for pin_num in list(range(2,20)):
            self.buttons_pressed[str(pin_num)] = False

    def call(self, time):
        global GPIO

        if GPIO:
            self.__handle_gpio_events()

        for e in self.pygame.event.get():
            self.sgc.event(e)
            self.__handle_event(e)

    def __handle_gpio_press(self, pin_num, on_press):
        global GPIO
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

    def __handle_gpio_events(self):
        def on_press_2():
            self.logger.info('press 2')
            self.counters['corp_credits'].increment_counter()

        def on_press_3():
            self.logger.info('press 3')
            self.counters['corp_credits'].decrement_counter()

        def on_press_4():
            self.logger.info('press 4')
            self.counters['corp_handsize'].increment_counter()

        def on_press_5():
            self.logger.info('press 5')
            self.counters['corp_handsize'].decrement_counter()

        def on_press_6():
            self.logger.info('press 6')
            self.counters['corp_bad_publicity'].increment_counter()

        def on_press_7():
            self.logger.info('press 7')
            self.counters['corp_bad_publicity'].decrement_counter()

        def on_press_8():
            self.logger.info('press 8')
            self.counters['runner_credits'].increment_counter()

        def on_press_9():
            self.logger.info('press 9')
            self.counters['runner_credits'].decrement_counter()

        def on_press_10():
            self.logger.info('press 10')
            self.counters['runner_handsize'].increment_counter()

        def on_press_11():
            self.logger.info('press 11')
            self.counters['runner_handsize'].decrement_counter()

        def on_press_12():
            self.logger.info('press 12')
            self.counters['runner_tags'].increment_counter()

        def on_press_13():
            self.logger.info('press 13')
            self.counters['runner_tags'].decrement_counter()

        def on_press_14():
            self.logger.info('press 14')
            self.counters['runner_brain_damage'].increment_counter()

        def on_press_15():
            self.logger.info('press 15')
            self.counters['runner_brain_damage'].decrement_counter()

        def on_press_16():
            self.logger.info('press 16')
            self.counters['runner_memory_units'].increment_counter()

        def on_press_17():
            self.logger.info('press 17')
            self.counters['runner_memory_units'].decrement_counter()

        def on_press_18():
            self.logger.info('press 18')
            self.click_tracks.trackers['runner'].handle_click()
            self.click_tracks.click_event()

        def on_press_19():
            self.logger.info('press 19')
            self.click_tracks.trackers['corp'].handle_click()
            self.click_tracks.click_event()

        self.__handle_gpio_press(2, on_press_2)
        self.__handle_gpio_press(3, on_press_3)
        self.__handle_gpio_press(4, on_press_4)
        self.__handle_gpio_press(5, on_press_5)
        self.__handle_gpio_press(6, on_press_6)
        self.__handle_gpio_press(7, on_press_7)
        self.__handle_gpio_press(8, on_press_8)
        self.__handle_gpio_press(9, on_press_9)
        self.__handle_gpio_press(10, on_press_10)
        self.__handle_gpio_press(11, on_press_11)
        self.__handle_gpio_press(12, on_press_12)
        self.__handle_gpio_press(13, on_press_13)
        self.__handle_gpio_press(14, on_press_14)
        self.__handle_gpio_press(15, on_press_15)
        self.__handle_gpio_press(16, on_press_16)
        self.__handle_gpio_press(17, on_press_17)
        self.__handle_gpio_press(18, on_press_18)
        self.__handle_gpio_press(19, on_press_19)

