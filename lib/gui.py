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

    def __init_btn(self, label, callback, r, c):
        self._btn = self.sgc.Button(label=label, pos=self.__position(r, c))
        self._btn.on_click = callback
        self._btn.add()

    def init_click_track_btns(self):

        # Corp -----------------
        self.__init_btn('Corp Click', self.event_handler.corp_click_track, 0, 0)
        self.__init_btn('+ corp agenda', self.event_handler.incr_corp_agenda_pnt, 1, 0)
        self.__init_btn('- corp agenda', self.event_handler.decr_corp_agenda_pnt, 1, 1)
        self.__init_btn('+ corp credits', self.event_handler.incr_corp_credits, 2, 0)
        self.__init_btn('- corp credits', self.event_handler.decr_corp_credits, 3, 0)
        self.__init_btn('+ corp handsize', self.event_handler.incr_corp_handsize, 2, 1)
        self.__init_btn('- corp handsize', self.event_handler.decr_corp_handsize, 3, 1)
        self.__init_btn('+ bad pub', self.event_handler.incr_corp_bad_pub, 4, 0)
        self.__init_btn('- bad pub', self.event_handler.decr_corp_bad_pub, 5, 0)

        # Runner -----------------
        #
        self.__init_btn('Runner Click', self.event_handler.runner_click_track, 0, 2)
        self.__init_btn('+ runner agenda', self.event_handler.incr_runner_agenda_pnt, 1, 2)
        self.__init_btn('- runner agenda', self.event_handler.decr_runner_agenda_pnt, 1, 3)
        self.__init_btn('+ runner credits', self.event_handler.incr_runner_credits, 2, 2)
        self.__init_btn('- runner credits', self.event_handler.decr_runner_credits, 3, 2)
        self.__init_btn('+ runner handsize', self.event_handler.incr_runner_handsize, 2, 3)
        self.__init_btn('- runner handsize', self.event_handler.decr_runner_handsize, 3, 3)
        self.__init_btn('+ runner tags', self.event_handler.incr_runner_tags, 4, 2)
        self.__init_btn('- runner tags', self.event_handler.decr_runner_tags, 5, 2)
        self.__init_btn('+ brain dmg', self.event_handler.incr_runner_brain_dmg, 4, 3)
        self.__init_btn('- brain dmg', self.event_handler.decr_runner_brain_dmg, 5, 3)
        self.__init_btn('+ mem units', self.event_handler.incr_runner_mem_units, 6, 2)
        self.__init_btn('- mem units', self.event_handler.decr_runner_mem_units, 7, 2)

