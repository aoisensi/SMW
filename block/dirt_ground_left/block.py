class Block_dirt_ground_left(Block):
    image = None

    @staticmethod
    def load_block():
        Block_dirt_ground_left.image = pygame.image.load('./block/dirt_ground_left/block.png')

    @staticmethod
    def get_name():
        return "dirt_ground_left"

    @staticmethod
    def get_picture():
        return Block_dirt_ground_left.image

    @staticmethod
    def get_collision(x, y):
        collision = Collision()
        if y == 0:
            collision.up = True
            if x == 0:
                collision.left = True
        return collision
block_class = Block_dirt_ground_left