class Block_hatena_block(object):
    turn = 0
    image = None
    image2 = None
    def __init__(self):
        Block_hatena_block.image = pygame.image.load('./block/hatena_block/block.png')
        Block_hatena_block.image2 = pygame.image.load('./block/hatena_block/block2.png')
    def update(self):
        if(self.turn > 0 and self.turn < 20):
            self.turn = self.turn + 1
#debug only
##        elif(self.turn == 20):
##            self.turn = 0
    def get_name(self):
        return "hatena_block"
    def get_picture(self):
        if(self.turn < 15):
            return Block_hatena_block.image
        else:
            return Block_hatena_block.image2
    def get_collision(self, x, y):
        collision = Collision()
        collision.left = x == 0
        collision.right = x == 15
        collision.up = y == 0
        collision.down = y == 15
        return collision
    def get_gap(self):
        return (0, abs(int(self.turn / 2) - 5) - 5)
    def event_player_strike(self):
        if(self.turn == 0):
            self.turn = 1

block_class = Block_hatena_block