class Block_dirt_ground_middle(Block):
    image = None

    @staticmethod
    def load_block():
        Block_dirt_ground_middle.image = pygame.image.load('./block/dirt_ground_middle/block.png')

    @staticmethod
    def get_name():
        return "dirt_ground_middle"

    @staticmethod
    def get_picture():
        return Block_dirt_ground_middle.image

    @staticmethod
    def get_collision(x, y):
        collision = Collision()

        collision.up = y == 0

        return collision
block_class = Block_dirt_ground_middle