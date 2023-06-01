import pygame

class Spider(pygame.sprite.Sprite):
    def __init__(self, screen, size, pos) -> None:
        self.sprites = []
        self.sprites.append(pygame.image.load('1.png'))
        self.sprites.append(pygame.image.load('2.png'))
        self.sprites.append(pygame.image.load('3.png'))
        self.sprites.append(pygame.image.load('4.png'))
        self.sprites.append(pygame.image.load('5.png'))
        self.sprites.append(pygame.image.load('6.png'))
        self.sprites.append(pygame.image.load('7.png'))
        self.current_sprite = 0
        self.size = size
        self.screen = screen
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, size)
        self.rect = pygame.Rect(pos[0], pos[1], self.image.get_width(), self.image.get_height())
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.vel_orizz = 4
        self.vel_vert = 4
        self.animazione = False
        self.animazione2 = False
    
    def update(self,speed):
        if self.animazione == True or self.animazione2 == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]
        self.image = pygame.transform.scale(self.image, self.size)

    def move_right(self):
        self.moving_right = True
    
    def stop_move_right(self):
        self.moving_right = False

    def move_left(self):
        self.moving_left = True
    
    def stop_move_left(self):
        self.moving_left = False

    def move_up(self):
        self.moving_up= True
        self.animazione2 = True
    
    def move_down(self):
        self.moving_down= True
        self.animazione = True

    def stop_move_up(self):
        self.moving_up = False
        self.animazione2 = False

    def stop_move_down(self):
        self.moving_down = False
        self.animazione = False

    def muovi(self):
        if self.moving_up:
            self.rect.top -= self.vel_vert
        if self.moving_down:
            self.rect.top += self.vel_vert
        # muovi orizzontale
        if self.moving_right:
            self.rect.right += self.vel_orizz
            if self.rect.right > self.screen.get_width():
                self.rect.right = self.screen.get_width()
        if self.moving_left:
            self.rect.left -= self.vel_orizz
            if self.rect.left < 0:
                self.rect.left = 0


    def draw(self):
        self.screen.blit(self.image, self.rect)