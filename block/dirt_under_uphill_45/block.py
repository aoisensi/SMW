class Block_dirt_under_uphill_45(Block):
    image = None

    @staticmethod
    def load_block():
        Block_dirt_under_uphill_45.image = pygame.image.load('./block/dirt_under_uphill_45/block.png')

    @staticmethod
    def get_name():
        return "dirt_under_uphill_45"

    @staticmethod
    def get_picture():
        return Block_dirt_under_uphill_45.image


block_class = Block_dirt_under_uphill_45