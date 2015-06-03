
class IncrementableCounter:

    def __init__(self, _pygame, _sgc, counter_type, x_pos, y_pos, x_adjust = 0, y_adjust = 0):
        self.counter_type = counter_type
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_adjust = x_adjust
        self.y_adjust = y_adjust
        self.counter = 0
        self.pygame = _pygame
        self.sgc = _sgc
        self.init_counter_icon()
        self.init_counter_label()

    def init_counter_icon(self):
        self.counter_icon = self.sgc.Simple(
            'images/' + self.counter_type + '.png', 
            pos=(self.x_pos + self.x_adjust, self.y_adjust + self.y_pos)
        )
        self.counter_icon.add()

    def init_counter_label(self):
        _font = self.pygame.font.SysFont('monospace', 80, bold=True)
        self.counter_label = self.sgc.Label(
            text=str(self.counter), 
            col=(255, 255, 255),
            font=_font,
            pos=(self.x_pos + 100, self.y_pos)
        )
        self.counter_label.add()

    def increment_counter(self):
        logger.info('increment')

    def decrement_counter(self):
        logger.info('decrement')

    def reset():
        self.counter = 0

