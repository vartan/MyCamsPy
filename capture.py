from VideoCapture import Device
import pygame
try:
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    sound = pygame.mixer.Sound('shutter.wav').play()
except IOError as e:
    pass
Device().saveSnapshot('image.jpg', timestamp=3, boldfont=1, quality=70)
quit
