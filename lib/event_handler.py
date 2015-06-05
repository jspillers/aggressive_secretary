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
    for pin_num in list(range(2,24)):
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
        self.runner_agendas = kwargs['runner_agendas']
        self.corp_agendas = kwargs['corp_agendas']
        self.buttons_pressed = {}

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
            _btn_press = self.buttons_pressed.get(str(pin_num), 'NotFound')
            if _btn_press == False or _btn_press == 'NotFound':
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
        self.__handle_gpio_press(2, incr_corp_credits)
        self.__handle_gpio_press(3, decr_corp_credits)
        self.__handle_gpio_press(4, incr_corp_handsize)
        self.__handle_gpio_press(5, decr_corp_handsize)
        self.__handle_gpio_press(6, incr_corp_bad_pub)
        self.__handle_gpio_press(7, decr_corp_bad_pub)
        self.__handle_gpio_press(8, incr_runner_credits)
        self.__handle_gpio_press(9, decr_runner_credits)
        self.__handle_gpio_press(10, incr_runner_handsize)
        self.__handle_gpio_press(11, decr_runner_handsize)
        self.__handle_gpio_press(12, incr_runner_tags)
        self.__handle_gpio_press(13, decr_runner_tags)
        self.__handle_gpio_press(14, incr_runner_brain_dmg)
        self.__handle_gpio_press(15, decr_runner_brain_dmg)
        self.__handle_gpio_press(16, incr_runner_mem_units)
        self.__handle_gpio_press(17, decr_runner_mem_units)
        self.__handle_gpio_press(18, incr_runner_agenda_pnt)
        self.__handle_gpio_press(19, decr_runner_agenda_pnt)
        self.__handle_gpio_press(20, incr_corp_agenda_pnt)
        self.__handle_gpio_press(21, decr_corp_agenda_pnt)
        self.__handle_gpio_press(22, runner_click_track)
        self.__handle_gpio_press(23, corp_click_track)

    def incr_corp_credits(self):
        self.logger.info('press 2')
        self.counters['corp_credits'].increment_counter()

    def decr_corp_credits(self):
        self.logger.info('press 3')
        self.counters['corp_credits'].decrement_counter()

    def incr_corp_handsize(self):
        self.logger.info('press 4')
        self.counters['corp_handsize'].increment_counter()

    def decr_corp_handsize(self):
        self.logger.info('press 5')
        self.counters['corp_handsize'].decrement_counter()

    def incr_corp_bad_pub(self):
        self.logger.info('press 6')
        self.counters['corp_bad_publicity'].increment_counter()

    def decr_corp_bad_pub(self):
        self.logger.info('press 7')
        self.counters['corp_bad_publicity'].decrement_counter()

    def incr_runner_credits(self):
        self.logger.info('press 8')
        self.counters['runner_credits'].increment_counter()

    def decr_runner_credits(self):
        self.logger.info('press 9')
        self.counters['runner_credits'].decrement_counter()

    def incr_runner_handsize(self):
        self.logger.info('press 10')
        self.counters['runner_handsize'].increment_counter()

    def decr_runner_handsize(self):
        self.logger.info('press 11')
        self.counters['runner_handsize'].decrement_counter()

    def incr_runner_tags(self):
        self.logger.info('press 12')
        self.counters['runner_tags'].increment_counter()

    def decr_runner_tags(self):
        self.logger.info('press 13')
        self.counters['runner_tags'].decrement_counter()

    def incr_runner_brain_dmg(self):
        self.logger.info('press 14')
        self.counters['runner_brain_damage'].increment_counter()

    def decr_runner_brain_dmg(self):
        self.logger.info('press 15')
        self.counters['runner_brain_damage'].decrement_counter()

    def incr_runner_mem_units(self):
        self.logger.info('press 16')
        self.counters['runner_memory_units'].increment_counter()

    def decr_runner_mem_units(self):
        self.logger.info('press 17')
        self.counters['runner_memory_units'].decrement_counter()

    def incr_runner_agenda_pnt(self):
        self.logger.info('press 18')
        self.runner_agendas.add_point()

    def decr_runner_agenda_pnt(self):
        self.logger.info('press 19')
        self.runner_agendas.remove_point()

    def incr_corp_agenda_pnt(self):
        self.logger.info('press 20')
        self.corp_agendas.add_point()

    def decr_corp_agenda_pnt(self):
        self.logger.info('press 21')
        self.corp_agendas.remove_point()

    def runner_click_track(self):
        self.logger.info('press 22')
        self.click_tracks.trackers['runner'].handle_click()
        self.click_tracks.click_event()

    def corp_click_track(self):
        self.logger.info('press 23')
        self.click_tracks.trackers['corp'].handle_click()
        self.click_tracks.click_event()

