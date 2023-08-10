import pygame
import os

# pygame setup

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OdderTech Game Corner")
rate = 1
ICON_WIDTH, ICON_HEIGHT = 130, 90
ICON_XPOS_L, ICON_XPOS_M, ICON_XPOS_R = 175, 385, 595
ICON_YPOS = 170
LOWER_BOUND, UPPER_BOUND = 400, 50

# assets

Veilstone_7 = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Veilstone_Corner_7.png")),
    (ICON_WIDTH, ICON_HEIGHT),
)
Veilstone_Berries = pygame.image.load(
    os.path.join("Assets", "Veilstone_Corner_Berries.png")
)
Veilstone_Galactic = pygame.image.load(
    os.path.join("Assets", "Veilstone_Corner_Galactic_Symbol.png")
)
Veilstone_Lightning = pygame.image.load(
    os.path.join("Assets", "Veilstone_Corner_Lightning_Bolt.png")
)
Veilstone_Moon = pygame.image.load(
    os.path.join("Assets", "Veilstone_Corner_Moon_Stone.png")
)
Veilstone_Replay = pygame.image.load(
    os.path.join("Assets", "Veilstone_Corner_Replay.png")
)
bg = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "backgrond.png")), (WIDTH, HEIGHT)
)
# window update function, need to add object arguments and create some kind
# animation to imitate "scrolling" so that the values loop back
# also need to somehow randomize the images that are appearing, and implement a slow down
# function so that it eventually stops at a defined y level on all three?
# likely implement this by reducing the frame rate so that it stops updaitng


def draw_window(leftSprite, midSprite, rightSprite):
    WIN.fill((255, 255, 255))
    WIN.blit(bg, (0, 0))
    WIN.blit(Veilstone_7, (leftSprite.x, leftSprite.y))
    WIN.blit(Veilstone_7, (midSprite.x, midSprite.y))
    WIN.blit(Veilstone_7, (rightSprite.x, rightSprite.y))
    pygame.display.update()


# conditions


# movement
def icon_movement(keys_pressed, leftSprite, midSprite, rightSprite):
    while leftSprite.y < LOWER_BOUND:
        if keys_pressed[pygame.K_f]:
            print("Correct")
            break
        leftSprite.y += 1
        if leftSprite.y >= LOWER_BOUND:
            print("Hello")
            leftSprite.y = UPPER_BOUND
            draw_window(leftSprite, midSprite, rightSprite)

    if keys_pressed[pygame.K_g]:
        midSprite.y += 1
    if keys_pressed[pygame.K_h]:
        rightSprite.y += 1


def main():
    leftSprite = pygame.Rect(ICON_XPOS_L, ICON_YPOS, ICON_WIDTH, ICON_HEIGHT)
    midSprite = pygame.Rect(ICON_XPOS_M, ICON_YPOS, ICON_WIDTH, ICON_HEIGHT)
    rightSprite = pygame.Rect(ICON_XPOS_R, ICON_YPOS, ICON_WIDTH, ICON_HEIGHT)
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(rate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        icon_movement(keys_pressed, leftSprite, midSprite, rightSprite)

        draw_window(leftSprite, midSprite, rightSprite)

    pygame.quit()


if __name__ == "__main__":
    main()
