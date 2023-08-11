import pygame
import os
import random
import glob
import subprocess

# pygame setup

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OdderTech Game Corner")

rate = 10
ICON_WIDTH, ICON_HEIGHT = 130, 90
ICON_XPOS_L, ICON_XPOS_M, ICON_XPOS_R = 175, 385, 595
ICON_YPOS = 170
LOWER_BOUND, UPPER_BOUND = 400, 50


# assets

Veilstone_7 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Veilstone_Corner_7.png")),
    (ICON_WIDTH, ICON_HEIGHT),
)
Veilstone_Berries = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Veilstone_Corner_Berries.png")),
    (ICON_WIDTH, ICON_HEIGHT),
)
Veilstone_Galactic = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Veilstone_Corner_Galactic_Symbol.png")),
    (ICON_WIDTH, ICON_HEIGHT),
)
Veilstone_Lightning = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Veilstone_Corner_Lightning_Bolt.png")),
    (ICON_WIDTH, ICON_HEIGHT),
)
Veilstone_Moon = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Veilstone_Corner_Moon_Stone.png")),
    (ICON_WIDTH, ICON_HEIGHT),
)
Veilstone_Replay = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Veilstone_Corner_Replay.png")),
    (ICON_WIDTH, ICON_HEIGHT),
)
bg = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "backgrond.png")), (WIDTH, HEIGHT)
)
# window update function, need to add object arguments and create some kind
# animation to imitate "scrolling" so that the values loop back
# also need to somehow randomize the images that are appearing, and implement a slow down
# function so that it eventually stops at a defined y level on all three?
# likely implement this by reducing the frame rate so that it stops updaitng


# draw_window functions for each sprite
def draw_bg():
    WIN.fill((255, 255, 255))
    WIN.blit(bg, (0, 0))
    pygame.display.update()


def draw_window1(leftSprite):
    IMAGE_LEFT = random.choice(
        [
            Veilstone_7,
            Veilstone_Berries,
            Veilstone_Galactic,
            Veilstone_Lightning,
            Veilstone_Moon,
            Veilstone_Replay,
        ]
    )
    WIN.blit(
        random.choice(
            [
                Veilstone_7,
                Veilstone_Berries,
                Veilstone_Galactic,
                Veilstone_Lightning,
                Veilstone_Moon,
                Veilstone_Replay,
            ]
        ),
        (leftSprite.x, leftSprite.y),
    )
    pygame.display.update()
    return IMAGE_LEFT


def draw_window2(midSprite):
    IMAGE_MID = random.choice(
        [
            Veilstone_7,
            Veilstone_Berries,
            Veilstone_Galactic,
            Veilstone_Lightning,
            Veilstone_Moon,
            Veilstone_Replay,
        ]
    )
    WIN.blit(
        random.choice(
            [
                Veilstone_7,
                Veilstone_Berries,
                Veilstone_Galactic,
                Veilstone_Lightning,
                Veilstone_Moon,
                Veilstone_Replay,
            ]
        ),
        (midSprite.x, midSprite.y),
    )
    pygame.display.update()
    return IMAGE_MID


def draw_window3(rightSprite):
    IMAGE_RIGHT = random.choice(
        [
            Veilstone_7,
            Veilstone_Berries,
            Veilstone_Galactic,
            Veilstone_Lightning,
            Veilstone_Moon,
            Veilstone_Replay,
        ]
    )
    WIN.blit(
        random.choice(
            [
                Veilstone_7,
                Veilstone_Berries,
                Veilstone_Galactic,
                Veilstone_Lightning,
                Veilstone_Moon,
                Veilstone_Replay,
            ]
        ),
        (rightSprite.x, rightSprite.y),
    )
    pygame.display.update()
    return IMAGE_RIGHT


# conditions


def main():
    leftSprite = pygame.Rect(ICON_XPOS_L, ICON_YPOS, ICON_WIDTH, ICON_HEIGHT)
    midSprite = pygame.Rect(ICON_XPOS_M, ICON_YPOS, ICON_WIDTH, ICON_HEIGHT)
    rightSprite = pygame.Rect(ICON_XPOS_R, ICON_YPOS, ICON_WIDTH, ICON_HEIGHT)
    run = True
    clock = pygame.time.Clock()
    draw_bg()
    while run:
        clock.tick(rate)
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # print("Hello")
            if keys_pressed[pygame.K_f]:
                run = False
                # print("Correct")

        # icon_movement(keys_pressed, leftSprite, midSprite, rightSprite)
        draw_bg()
        sprite_left = draw_window1(leftSprite)
        draw_window2(midSprite)
        draw_window3(rightSprite)

    # first sprite is stopped
    stop_con1 = True
    while stop_con1:
        clock.tick(rate)
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # print("Hello")
            if keys_pressed[pygame.K_g]:
                stop_con1 = False
                # print("Correct2")
        draw_bg()
        WIN.blit(sprite_left, (leftSprite.x, leftSprite.y))
        sprite_mid = draw_window2(midSprite)
        draw_window3(rightSprite)
    stop_con2 = True
    while stop_con2:
        clock.tick(rate)
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # print("Hello")
            if keys_pressed[pygame.K_h]:
                stop_con2 = False
                # print("Correct3")
        draw_bg()
        WIN.blit(sprite_left, (leftSprite.x, leftSprite.y))
        WIN.blit(sprite_mid, (midSprite.x, midSprite.y))
        sprite_right = draw_window3(rightSprite)
    idle = True
    while idle:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                idle = False
                # print("Hello")
        WIN.blit(sprite_right, (rightSprite.x, rightSprite.y))
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            main()

    pygame.quit()


if __name__ == "__main__":
    main()
