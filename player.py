import pygame

class Player:
    position = pygame.Vector2()
    position.xy = 20, 350
    money = 0
    speed = 1
    sprite = pygame.image.load('data/images/player1.png')
