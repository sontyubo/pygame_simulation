import math

import pygame
from pygame.locals import *

import sample

WHITE = (255, 255, 255)


def main():
    pygame.init()
    surface = pygame.display.set_mode((640,400))

    x, y, w, h = 300, 250, 5, 150
    rect1 = pygame.Rect(x, y, w, h)   # x, y(topの辺), w, h
    x2, y2 = sample.get_sample_data()
    h2 = 100
    rect2 = pygame.Rect(x+x2, y+y2-h2, w, h2)   
    rect2 = pygame.transform.rotate(surface, math.radians(20))
    surface.fill((0, 128, 0), rect1)
    surface.fill(WHITE, rect2)

    # 画面更新
    pygame.display.update(rect1)
    pygame.display.update(rect2)
    
    # 無限ループ
    while True:
    
        # イベント処理
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                break
    
        # whileループ終了
        #break
    
    # 終了処理
    pygame.quit()


    print('--- fin ---')


if __name__ == '__main__':
    main()
