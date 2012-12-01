class Block_air(object):
    def get_name(self):
        return "air"
    def get_picture(self):
        return None
    def get_collision(self, x, y):
        return Collision()
block_class = Block_air