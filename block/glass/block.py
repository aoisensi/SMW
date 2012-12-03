class Block_glass(Block):
    image = None

    @staticmethod
    def load_block():
        Block_glass.image = pygame.image.load('./block/glass/glass.png')

    @staticmethod
    def get_name():
        return "glass"

    @staticmethod
    def get_picture():
        return Block_glass.image


block_class = Block_glass