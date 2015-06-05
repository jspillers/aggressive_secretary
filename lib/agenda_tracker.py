class AgendaTracker:

    def __init__(self, **kwargs):
        self.pygame = kwargs['pygame']
        self.sgc = kwargs['sgc'] 
        self.tracker_type = kwargs['tracker_type'] 
        self.x_pos = kwargs['x_pos'] 
        self.y_pos = kwargs['y_pos'] 
        self.agenda_icons = []

    def add_point(self):
        if len(self.agenda_icons) < 14:
            _agenda_icon = self.sgc.Simple(
                'images/agenda_point.png', 
                pos=(self.x_pos + (45 * len(self.agenda_icons)), self.y_pos)
            )
            _agenda_icon.add()
            self.agenda_icons.append(_agenda_icon)

    def remove_point(self):
        if len(self.agenda_icons) > 0:
            self.agenda_icons[-1].remove()
            del self.agenda_icons[-1]
