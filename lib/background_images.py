
class BackgroundImages:

    def __init__(self, _pygame, _screen, _logger):
        self.background_images = []
        self.cycle_time = 500
        self.elapsed_time = 0
        self.current_bg_index = 0
        self.pygame = _pygame
        self.screen = _screen
        self.init_images()

    def init_images(self):
        for i in range(1, 14):
            _bg = self.pygame.image.load('images/background_' + str(i) + '.png').convert()
            self.background_images.append(_bg)

    def current_bg_image(self):
       return self.background_images[self.current_bg_index]

    def cycle_images(self):
        self.elapsed_time += 1

        if self.elapsed_time > self.cycle_time:
            self.elapsed_time = 0

            if self.current_bg_index >= len(self.background_images) - 1:
                self.current_bg_index = 0
            else:
                self.current_bg_index += 1

        self.screen.blit(self.current_bg_image(), [0, 0])
        
