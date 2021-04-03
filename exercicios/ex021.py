# Desafio 021 -> Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3
import os
print(os.getcwd())
import pygame
pygame.init()
pygame.mixer.music.load(musicarussagenerica.mp3)
pygame.mixer.music.play()
pygame.event.wait()
