

screen = pygame.display.set_mode(gm.SIZESCREEN)
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, file_image):
        super().__init__()
        self.image = file_image
        self.movement_x = 0
        self.movement_y = 0
        self._count = 0
        self.rect = self.image.get_rect()
        self.press_left = False
        self.press_right = False
        self.level = None
        self.lifes = 3

    def shoot(self):
        if self.items.get("shotgun", False):
            if self.rotate_left:
                bullet = Bullet(gm.BULLET_L, self.rotate_left, self.rect.centerx, self.rect.centery)
            else:
                bullet = Bullet(gm.BULLET_R, self.rotate_left, self.rect.centerx, self.rect.centery)
            self.level.set_of_bullets.add()