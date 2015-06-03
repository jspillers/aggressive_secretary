class ClickTrackers:

    def __init__(self, _pygame, _screen, _sgc, _logger):
        self.corp_click_track = ClickTracker(_pygame, _screen, _sgc, 'corp', 20, 20, _logger)
        self.runner_click_track = ClickTracker(_pygame, _screen, _sgc, 'runner', 420, 20, _logger)
        self.runner_click_track.clicks = 4
        self.current_player = 'corp'
        self.logger = _logger
        self.turn_num = 1

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
                self.turn_num += 1

class ClickTracker:

    def __init__(self, _pygame, _screen, _sgc, tracker_type, x_pos, y_pos, _logger):
        self.tracker_type = tracker_type
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.clicks = 0
        self.max_clicks = 4 if tracker_type == 'runner' else 3
        self.click_images = []
        self.pygame = _pygame
        self.screen = _screen
        self.sgc = _sgc
        self.logger = _logger

        self.click_image_positions = [
            (x_pos + 4, y_pos + 3), 
            (x_pos + 79, y_pos + 46), 
            (x_pos + 154, y_pos + 3), 
            (x_pos + 229, y_pos + 46)
        ]
        self.init_tracker()
    
    def init_tracker(self):
        self.tracker_bg = self.pygame.image.load(
            'images/' + self.tracker_type + '_click_track.png').convert_alpha()

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
        self.sgc.Button.on_click(self.click_btn)
        if self.clicks < self.max_clicks:
            self.clicks += 1

