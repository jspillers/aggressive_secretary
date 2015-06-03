import sgc
from sgc.locals import *
import pygame
from pygame.locals import *

TURN_ENDED = USEREVENT + 1

class ClickTrackers:

    def __init__(self, **kwargs):
        self.__configure(kwargs)

        self.corp_click_track = ClickTracker(
            pygame=self.pygame, screen=self.screen, sgc=self.sgc, use_gui=self.use_gui, 
            tracker_type='corp', x_pos=20, y_pos=20, logger=self.logger
        )

        self.runner_click_track = ClickTracker(
            pygame=self.pygame, screen=self.screen, sgc=self.sgc, use_gui=self.use_gui,
            tracker_type='runner', x_pos=420, y_pos=20, logger=self.logger
        )

        self.runner_click_track.clicks = 4

    def update(self):
        self.corp_click_track.update()
        self.runner_click_track.update()

    def click_event(self, event):
        self.logger.info(self.turn_num)
        if self.current_player == 'corp':
            if self.corp_click_track.clicks == self.corp_click_track.max_clicks:
                self.runner_click_track.reset()
                self.current_player = 'runner'
        else:
            if self.runner_click_track.clicks == self.runner_click_track.max_clicks:
                self.corp_click_track.reset()
                self.current_player = 'corp'
                self.__turn_ended()

    def __turn_ended(self):
        self.turn_num += 1
        end_turn_event = self.pygame.event.Event(TURN_ENDED, message="turn has ended")
        self.pygame.event.post(end_turn_event)

    def __configure(self, kwargs):
        self.pygame = kwargs['pygame']
        self.screen = kwargs['screen']
        self.sgc = kwargs['sgc']
        self.logger = kwargs['logger']
        self.current_player = kwargs['current_player'] if 'current_player' in kwargs else 'corp'
        self.turn_num = kwargs['turn_num'] if 'turn_num' in kwargs else 1
        self.use_gui = kwargs['use_gui'] if 'use_gui' in kwargs else True

class ClickTracker:

    def __init__(self, **kwargs):
        self.__configure(kwargs)
        self.max_clicks = 4 if self.tracker_type == 'runner' else 3
        self.click_images = []
        self.click_image_positions = [
            (self.x_pos + 4, self.y_pos + 3), 
            (self.x_pos + 79, self.y_pos + 46), 
            (self.x_pos + 154, self.y_pos + 3), 
            (self.x_pos + 229, self.y_pos + 46)
        ]

        self.init_tracker()
    
    def init_tracker(self):
        self.tracker_bg = self.pygame.image.load(
            'images/' + self.tracker_type + '_click_track.png').convert_alpha()

        if self.use_gui == True:
          self.click_btn = self.sgc.Button(label='click', pos=(self.x_pos, self.y_pos + 100))
          self.click_btn.on_click = self.advance_click
          self.click_btn.add()

    def click_image(self):
        return self.pygame.image.load('images/click_track_mask.png').convert_alpha()

    def update(self):
        self.screen.blit(self.tracker_bg, [self.x_pos, self.y_pos])

        for click in list(range(self.clicks)):
            self.screen.blit(self.click_image(), self.click_image_positions[click])

    def reset(self):
      self.clicks = 0

    def advance_click(self):
        if self.use_gui == True:
            self.sgc.Button.on_click(self.click_btn) 

        if self.clicks < self.max_clicks:
            self.clicks += 1

    def __configure(self, kwargs):
        self.pygame = kwargs['pygame']
        self.screen = kwargs['screen']
        self.sgc = kwargs['sgc']
        self.logger = kwargs['logger']
        self.tracker_type = kwargs['tracker_type']
        self.x_pos = kwargs['x_pos']
        self.y_pos = kwargs['y_pos']
        self.clicks = kwargs['clicks'] if 'clicks' in kwargs else 0
        self.use_gui = kwargs['use_gui'] if 'use_gui' in kwargs else True


