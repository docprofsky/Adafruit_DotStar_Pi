#!/usr/bin/python

import pygame

pygame.init()

black = (0, 0, 0)

class Strip:

    def __init__(self, size, scale, pixsPerLine, pixelBorder):
        self.data = [0] * size
        self.begun = False
        self.brightness = 64

        self.pixelBorder = pixelBorder
        self.pixsPerLine = pixsPerLine
        self.scale = scale

        self.screenSize = (pixsPerLine * scale), ((size / pixsPerLine) * scale)

        self.screen = pygame.display.set_mode(self.screenSize)

        self.screen.fill(black)

        pygame.display.update()

    def begin(self):
        begun = True

    def setBrightness(self, brightness):
        self.brightness = brightness

    def setPixelColor(self, index, color):
        if index < len(self.data):
            self.data[index] = color

    def show(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            elif event.type == pygame.QUIT:
                exit()

        self.screen.fill(black)
        for i in range(len(self.data)):
            color = (self.data[i] & 0xFF, (self.data[i] >> 8) & 0xFF, (self.data[i] >> 16) & 0xFF)
            pos = ((i % self.pixsPerLine) * self.scale), (( i / self.pixsPerLine) * self.scale), self.scale, self.scale
            pygame.draw.rect(self.screen, color, pos, 0)
            if self.pixelBorder:
                pygame.draw.rect(self.screen, black, pos, 1)
        pygame.display.update()
