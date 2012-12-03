class Block_dirt_under_middle(Block):
    image = None

    @staticmethod
    def load_block():
        Block_dirt_under_middle.image = pygame.image.load('./block/dirt_under_middle/block.png')

    @staticmethod
    def get_name():
        return "dirt_under_middle"

    @staticmethod
    def get_picture():
        return Block_dirt_under_middle.image


block_class = Block_dirt_under_middle