
class ClickTracker:

    def __init__(self, _pygame, _screen, _sgc, tracker_type, x_pos, y_pos):
        self.tracker_type = tracker_type
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.clicks = 0
        self.num_clicks = 4 if tracker_type == 'runner' else 3
        self.pygame = _pygame
        self.screen = _screen
        self.sgc = _sgc

        self.init_tracker()
    
    def init_tracker(self):
        self.tracker_bg = self.pygame.image.load(
            'images/' + self.tracker_type + '_click_track.png').convert_alpha()
        self.tracker_bg
        self.tracker = self.sgc.Container(
            pos=(self.x_pos, self.y_pos),
            widgets=self.widgets()
        )
        self.tracker.add()

    def widgets(self):
        _widgets = [
            self.sgc.Simple('images/click_track_mask.png', pos=(4, 3)),
            self.sgc.Simple('images/click_track_mask.png', pos=(79, 46)),
            self.sgc.Simple('images/click_track_mask.png', pos=(154, 3)),
            self.sgc.Simple('images/click_track_mask.png', pos=(229, 46))
        ]
        if self.tracker_type == 'runner':
            return _widgets
        else:
            return _widgets[0:3]

    def update(self):
        self.screen.blit(self.tracker_bg, [self.x_pos, self.y_pos])

    #def advance_click():
    #    if len(self.clicks) == self.num_clicks:
    #        self.tracker.widgets = []
    #        self.clicks = 0
    #    else:
    #        self.clicks += 1
    #        _mask = sgc.Simple('images/click_track_mask.png')
    #        logger.info(_mask)
    #        self.tracker.widgets.append(_mask)

