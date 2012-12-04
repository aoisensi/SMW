class Sprite_kinoko(Sprite):

    image = None

    coordinate = None

    def __init__(self, id, stage, coordinate):
        self.stage = stage
        self.coordinate = coordinate

    @staticmethod
    def get_name():
        return 'kinoko'

    @staticmethod
    def load_sprite():
        Sprite_kinoko.image = pygame.image.load('./sprite/kinoko/kinoko.png')

    def render(self):
        return (Sprite_kinoko.image, self.coordinate)
sprite_class = Sprite_kinoko
