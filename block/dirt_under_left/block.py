class Block_dirt_under_left(Block):
    image = None

    @staticmethod
    def load_block():
        Block_dirt_under_left.image = pygame.image.load('./block/dirt_under_left/block.png')

    @staticmethod
    def get_name():
        return "dirt_under_left"

    @staticmethod
    def get_picture():
        return Block_dirt_under_left.image


block_class = Block_dirt_under_left