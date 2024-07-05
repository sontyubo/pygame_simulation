import pygame
import math

# Pygameの初期化
pygame.init()

# 画面サイズ
screen_width = 400
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pendulum Animation')

# 色の定義
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)

# 長方形のサイズと位置
rect_width = 20
rect_height = 300
rect_x = screen_width // 2 - rect_width // 2
upper_rect_y = 100
lower_rect_y = upper_rect_y + rect_height

# アニメーションの設定
angle = 80  # 初期角度
angle_direction = 1  # 角度の変化方向
angle_speed = 1  # 角度の変化速度

# メインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 画面を白でクリア
    screen.fill(WHITE)

    # 上部の長方形の揺れ動きを計算
    angle += angle_speed * angle_direction
    if angle >= 100 or angle <= 80:
        angle_direction *= -1

    # 回転後の上部の長方形を描画
    upper_rect_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
    upper_rect_surface.fill(BLUE)
    rotated_upper_rect = pygame.transform.rotate(upper_rect_surface, angle - 90)
    offset_x = screen_width // 2
    offset_y = upper_rect_y + rect_height
    rotated_upper_rect_rect = rotated_upper_rect.get_rect(midbottom=(offset_x, offset_y+20))
    screen.blit(rotated_upper_rect, rotated_upper_rect_rect.topleft)

    # 下部の長方形を描画
    pygame.draw.rect(screen, GREEN, (rect_x, lower_rect_y, rect_width, rect_height))

    # 画面更新
    pygame.display.flip()
    pygame.time.delay(50)

# Pygameの終了
pygame.quit()