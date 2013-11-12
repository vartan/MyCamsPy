import pygame
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
sound = pygame.mixer.Sound('shutter.wav').play()
