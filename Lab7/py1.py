import pygame
from datetime import datetime

pygame.init()

WHITE = (255, 255, 255)
w, h = 800, 700
scr = pygame.display.set_mode((w, h), pygame.RESIZABLE)
main_image = pygame.image.load('/Users/zasulan/Downloads/fornastrgit/Lab7/mclock.png')
image = pygame.transform.scale(main_image, (w, h))
minute_arrow_image = pygame.image.load("/Users/zasulan/Downloads/fornastrgit/Lab7/mrh.png")
second_arrow_image = pygame.image.load("/Users/zasulan/Downloads/fornastrgit/Lab7/mlh.png")

def resize_arrows(new_width, new_height):
    global minute_arrow_image, second_arrow_image
    minute_arrow_image = pygame.transform.scale(minute_arrow_image, (new_width // 2, new_height // 2))
    second_arrow_image = pygame.transform.scale(second_arrow_image, (new_width // 2, new_height // 2))

resize_arrows(w, h)

minute_arrow_rect = minute_arrow_image.get_rect(center=(w // 2, h // 2))
second_arrow_rect = second_arrow_image.get_rect(center=(w // 2, h // 2))


prev_minute_rotation_angle = 0
prev_second_rotation_angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.VIDEORESIZE:
            w, h = event.w, event.h
            scr = pygame.display.set_mode((w, h), pygame.RESIZABLE)
            image = pygame.transform.scale(main_image, (w, h))
            resize_arrows(w, h)


    now = datetime.now()
    minute = now.minute
    second = now.second

    minute_rotation_angle = -(minute * 60) -270
    second_rotation_angle = -(second * 60) - 270


    minute_rotation_angle = prev_minute_rotation_angle + (minute_rotation_angle - prev_minute_rotation_angle) * 0.05
    second_rotation_angle = prev_second_rotation_angle + (second_rotation_angle - prev_second_rotation_angle) * 0.05

    prev_minute_rotation_angle = minute_rotation_angle
    prev_second_rotation_angle = second_rotation_angle

    rotated_minute_arrow = pygame.transform.rotate(minute_arrow_image, minute_rotation_angle)
    rotated_minute_rect = rotated_minute_arrow.get_rect(center=minute_arrow_rect.center)
    scr.blit(rotated_minute_arrow, rotated_minute_rect)

    rotated_second_arrow = pygame.transform.rotate(second_arrow_image, second_rotation_angle)
    rotated_second_rect = rotated_second_arrow.get_rect(center=second_arrow_rect.center)
    scr.blit(rotated_second_arrow, rotated_second_rect)

    pygame.display.flip()


    scr.fill(WHITE)
    scr.blit(image, (0, 0))


    