class Block_dirt_ground_uphill_45(Block):
    image = None

    @staticmethod
    def load_block():
        Block_dirt_ground_uphill_45.image = pygame.image.load('./block/dirt_ground_uphill_45/block.png')

    @staticmethod
    def get_name():
        return "dirt_ground_uphill_45"

    @staticmethod
    def get_picture():
        return Block_dirt_ground_uphill_45.image

    @staticmethod
    def get_collision(x, y):
        collision = Collision()
        if(15-x==y):
            collision.up = True
        return collision
block_class = Block_dirt_ground_uphill_45