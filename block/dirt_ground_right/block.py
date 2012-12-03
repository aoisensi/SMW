class Block_dirt_ground_right(Block):
    image = None

    @staticmethod
    def load_block():
        Block_dirt_ground_right.image = pygame.image.load('./block/dirt_ground_right/block.png')

    @staticmethod
    def get_name():
        return "dirt_ground_right"

    @staticmethod
    def get_picture():
        return Block_dirt_ground_right.image

    @staticmethod
    def get_collision(x, y):
        collision = Collision()
        if y == 0:
            collision.up = True
            if x == 15:
                collision.right = True
        return collision
block_class = Block_dirt_ground_right