"""faça um programa em python que abra e
reproduza um audio em mp3
"""
import pygame
import time

pygame.init()
pygame.mixer.music.load('oTam.mp3')
pygame.mixer.music.play()

# Aguarda até que a música termine
while pygame.mixer.music.get_busy():
    time.sleep(1)
