import pygame
from pygame.constants import (QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_ESCAPE, K_UP, K_DOWN)
import os

#Klassen

class Settings:
    window_width = 700
    window_height = 400
    file_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(file_path, "images")

class Background(object):
    def __init__(self, filename):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.image_path, filename))
        self.image = pygame.transform.scale(self.image, (Settings.window_width, Settings.window_height))
        self.rect = self.image.get_rect()
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Defender(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()
        self.image = pygame.image.load(os.path.join(Settings.image_path, filename))
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.centerx = Settings.window_width // 2
        self.rect.centery = Settings.window_height // 2
        self.rect.bottom = Settings.window_height
        self.direction = 0
        self.speed = 2

    def update(self):
        newrect = self.rect.move(self.direction * self.speed, 0)
        if newrect.left <= 0:
            self.move_stop()
        if newrect.right >= 700:
            self.move_stop()
        self.rect.move_ip(self.direction * self.speed, 0)

#Bewegungen

    def move_left(self):
        self.direction = -1
    
    def move_right(self):
        self.direction = 1
    
    def move_up(self):
        self.direction = 1

    def move_down(self):
        self.direction -1

    def move_stop(self):
        self.direction = 0
    

if __name__ == '__main__':
    pygame.init()


    screen = pygame.display.set_mode((Settings.window_width, Settings.window_height))
    clock = pygame.time.Clock()
    
    all_sprites = pygame.sprite.Group()

    background = Background("background.png")
    defender = Defender("defender01.png")
    all_sprites.add(defender)

#Hauptprogrammschleife

    running = True 
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    defender.move_left()
                elif event.key == K_RIGHT:
                    defender.move_right()
            elif event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    defender.move_stop()

       
        defender.update()

        

        background.draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
        

    
