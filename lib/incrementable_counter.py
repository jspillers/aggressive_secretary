
class IncrementableCounter:

    def __init__(self, **kwargs):
        self.__configure(kwargs)
        self.init_counter_icon()
        self.init_counter_label()

    def init_counter_icon(self):
        self.counter_icon = self.sgc.Simple(
            'images/' + self.counter_type + '.png', 
            pos=(self.x_pos + self.x_adjust, self.y_adjust + self.y_pos)
        )
        self.counter_icon.add()

    def init_counter_label(self):
        _font = self.pygame.font.SysFont('arial', 80, bold=True)
        self.counter_label = self.sgc.Label(
            text=str(self.counter), 
            col=(255, 255, 255),
            font=_font,
            pos=(self.x_pos + 100, self.y_pos)
        )
        self.counter_label.add()

    def update(self):
        self.counter_label.config(text=str(self.counter))

    def increment_counter(self):
        self.counter += 1
        self.update()

    def decrement_counter(self):
        self.counter -= 1
        self.update()
        
    def reset():
        self.counter = 0

    def __configure(self, kwargs):
        self.counter_type = kwargs['counter_type']
        self.x_pos = kwargs['x_pos']
        self.y_pos = kwargs['y_pos']
        self.pygame = kwargs['pygame']
        self.sgc = kwargs['sgc']

        self.x_adjust = kwargs['x_adjust'] if 'x_adjust' in kwargs else 0
        self.y_adjust = kwargs['y_adjust'] if 'y_adjust' in kwargs else 0
        self.counter = kwargs['counter'] if 'counter' in kwargs else 0


