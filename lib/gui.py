class Gui:

    def __init__(self, **kwargs):
        self.event_handler = kwargs['event_handler']
        self.sgc = kwargs['sgc']
        self.x_pos = kwargs['x_pos']
        self.y_pos = kwargs['y_pos']
        self.padding = 10
        self.row_size = 60
        self.column_size = 120
        self.init_click_track_btns()

    def __position(self, row, col):
        return (
            self.x_pos + self.padding + (self.column_size * col),
            self.y_pos + self.padding + (self.row_size * row),
        )

    def init_click_track_btns(self):

        # Corp -----------------
        #
        self._btn = self.sgc.Button(label='Corp Click', pos=self.__position(0, 0))
        self._btn.on_click = self.event_handler.corp_click_track
        self._btn.add()

        self._btn = self.sgc.Button(label='+ corp agenda', pos=self.__position(1, 0))
        self._btn.on_click = self.event_handler.incr_corp_agenda_pnt
        self._btn.add()

        self._btn = self.sgc.Button(label='- corp agenda', pos=self.__position(1, 1))
        self._btn.on_click = self.event_handler.decr_corp_agenda_pnt
        self._btn.add()

        self._btn = self.sgc.Button(label='+ corp credits', pos=self.__position(2, 0))
        self._btn.on_click = self.event_handler.incr_corp_credits
        self._btn.add()

        self._btn = self.sgc.Button(label='- corp credits', pos=self.__position(3, 0))
        self._btn.on_click = self.event_handler.decr_corp_credits
        self._btn.add()

        self._btn = self.sgc.Button(label='+ corp handsize', pos=self.__position(2, 1))
        self._btn.on_click = self.event_handler.incr_corp_handsize
        self._btn.add()

        self._btn = self.sgc.Button(label='- corp handsize', pos=self.__position(3, 1))
        self._btn.on_click = self.event_handler.decr_corp_handsize
        self._btn.add()

        self._btn = self.sgc.Button(label='+ bad pub', pos=self.__position(4, 0))
        self._btn.on_click = self.event_handler.incr_corp_handsize
        self._btn.add()

        self._btn = self.sgc.Button(label='- bad pub', pos=self.__position(5, 0))
        self._btn.on_click = self.event_handler.decr_corp_handsize
        self._btn.add()

        # Runner -----------------
        #
        self._btn = self.sgc.Button(label='Runner Click', pos=self.__position(0, 2))
        self._btn.on_click = self.event_handler.runner_click_track
        self._btn.add()

        self._btn = self.sgc.Button(label='+ runner agenda', pos=self.__position(1, 2))
        self._btn.on_click = self.event_handler.incr_runner_agenda_pnt
        self._btn.add()

        self._btn = self.sgc.Button(label='- runner agenda', pos=self.__position(1, 3))
        self._btn.on_click = self.event_handler.decr_runner_agenda_pnt
        self._btn.add()

        self._btn = self.sgc.Button(label='+ runner credits', pos=self.__position(2, 2))
        self._btn.on_click = self.event_handler.incr_runner_credits
        self._btn.add()

        self._btn = self.sgc.Button(label='- runner credits', pos=self.__position(3, 2))
        self._btn.on_click = self.event_handler.decr_runner_credits
        self._btn.add()

        self._btn = self.sgc.Button(label='+ runner handsize', pos=self.__position(2, 3))
        self._btn.on_click = self.event_handler.incr_runner_handsize
        self._btn.add()

        self._btn = self.sgc.Button(label='- runner handsize', pos=self.__position(3, 3))
        self._btn.on_click = self.event_handler.decr_runner_handsize
        self._btn.add()

        self._btn = self.sgc.Button(label='+ tags', pos=self.__position(4, 2))
        self._btn.on_click = self.event_handler.incr_runner_tags
        self._btn.add()

        self._btn = self.sgc.Button(label='- tags', pos=self.__position(5, 2))
        self._btn.on_click = self.event_handler.decr_runner_tags
        self._btn.add()

        self._btn = self.sgc.Button(label='+ brain damage', pos=self.__position(4, 3))
        self._btn.on_click = self.event_handler.incr_runner_brain_dmg
        self._btn.add()

        self._btn = self.sgc.Button(label='- brain damage', pos=self.__position(5, 3))
        self._btn.on_click = self.event_handler.decr_runner_brain_dmg
        self._btn.add()

        self._btn = self.sgc.Button(label='+ mem units', pos=self.__position(6, 2))
        self._btn.on_click = self.event_handler.incr_runner_mem_units
        self._btn.add()

        self._btn = self.sgc.Button(label='- mem units', pos=self.__position(7, 2))
        self._btn.on_click = self.event_handler.decr_runner_mem_units
        self._btn.add()

