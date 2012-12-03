class Block_dirt_under_right(Block):
    image = None

    @staticmethod
    def load_block():
        Block_dirt_under_right.image = pygame.image.load('./block/dirt_under_right/block.png')

    @staticmethod
    def get_name():
        return "dirt_under_right"

    @staticmethod
    def get_picture():
        return Block_dirt_under_right.image


block_class = Block_dirt_under_right