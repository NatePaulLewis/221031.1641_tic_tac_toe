import pygame
import os
from pygame import mixer

WIDTH, HEIGHT = 1224, 792
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")

BG_COLOR = (32, 32, 32,)
# BOARDER = pygame.Rect()

FPS = 60
VEL = 5
CHARACTER_WIDTH, CHARACTER_HEIGHT = 256, 256

X9 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_x9.png'))
X8 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_x8.png'))
X7 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_x7.png'))
X6 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_x6.png'))
X5 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_x5.png'))
X4 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_x4.png'))
X3 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_x3.png'))
X2 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_x2.png'))
X1 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_x1.png'))

O9 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_o9.png'))
O8 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_o8.png'))
O7 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_o7.png'))
O6 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_o6.png'))
O5 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_o5.png'))
O4 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_o4.png'))
O3 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_o3.png'))
O2 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_o2.png'))
O1 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_o1.png'))

GAME_BOARD = pygame.image.load(os.path.join('assets', 'tic_tac_toe_game_board.png'))


# X_CHARACTER = pygame.image.load(os.path.join('assets', 'tic_tac_toe_x9.png'))
# X_CHARACTER       = pygame.transform.scale(X_CHARACTER_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
# O_CHARACTER_IMAGE = pygame.image.load(os.path.join('assets', 'graphics_o.png'))
# O_CHARACTER       = pygame.transform.scale(O_CHARACTER_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

# Music:
# music_file = '6. my_oh_my.mp3'
# mixer.init()
# mixer.music.load(music_file)
# mixer.music.play()

# def draw_window(x_shape, o_shape):
#     WIN.fill(BG_COLOR)
#     WIN.blit(GAME_BOARD,  (0, 0))
#     WIN.blit(X9, (x_shape.x, x_shape.y))
#     WIN.blit(O5, (o_shape.x, o_shape.y))
#     pygame.display.update()

def draw_window():
    WIN.fill(BG_COLOR)
    WIN.blit(GAME_BOARD, (0, 0))
    pygame.display.update()


# def x_shape_character(keys_pressed, x_shape):
#     if keys_pressed[pygame.K_LEFT]:
#         WIN.blit(X9, (x_shape.x, x_shape.y))
#
#     if keys_pressed[pygame.K_RIGHT]:
#         WIN.blit(X8, (x_shape.x, x_shape.y))
#
#     if keys_pressed[pygame.MOUSEBUTTONDOWN]:
#         WIN.blit(X8, (x_shape.x, x_shape.y))
#
#     pygame.display.update()


# def x_shape_character(mouse_button_pressed, x_shape):
#     if mouse_button_pressed[pygame.K_LEFT]:
#         WIN.blit(X9, (x_shape.x, x_shape.y))
#
#     if mouse_button_pressed[pygame.K_RIGHT]:
#         WIN.blit(X8, (x_shape.x, x_shape.y))
#
#     if mouse_button_pressed[pygame.MOUSEBUTTONDOWN]:
#         WIN.blit(X8, (x_shape.x, x_shape.y))
#
#     if mouse_button_pressed[pygame.MOUSEBUTTONDOWN]:
#         print("left is being pressed")
#         WIN.blit(X9, (x_shape.x, x_shape.y))

#     pygame.display.update()
# pygame.mouse.get_pos()
# pygame.mouse.get_pressed()

# def x_shape_movement(keys_pressed, x_shape):
#         if keys_pressed[pygame.K_LEFT] and x_shape.x - VEL > 0: #LEFT
#             x_shape.x -= VEL
#         if keys_pressed[pygame.K_RIGHT] and x_shape.x + VEL < WIDTH - 300: #RIGHT
#             x_shape.x += VEL
#         if keys_pressed[pygame.K_UP] and x_shape.y - VEL > 0: #UP
#             x_shape.y -= VEL
#         if keys_pressed[pygame.K_DOWN] and x_shape.y + VEL < HEIGHT- 300: #DOWN
#             x_shape.y += VEL

# def o_shape_movement(keys_pressed, o_shape):
#         if keys_pressed[pygame.K_LEFT] and o_shape.x - VEL > 0: #LEFT
#             o_shape.x -= VEL
#         if keys_pressed[pygame.K_RIGHT] and o_shape.x + VEL < WIDTH - 300: #RIGHT
#             o_shape.x += VEL
#         if keys_pressed[pygame.K_UP] and o_shape.y - VEL > 0: #UP
#             o_shape.y -= VEL
#         if keys_pressed[pygame.K_DOWN] and o_shape.y + VEL < HEIGHT- 300: #DOWN
#             o_shape.y += VEL

def main():
    x_shape = pygame.Rect(0, 0, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    # o_shape = pygame.Rect(0, 0, CHARACTER_WIDTH, CHARACTER_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_button_pressed = pygame.mouse.get_pressed()
                # if (mouse_button_pressed):
                if mouse_button_pressed[0]:
                    print("left is being pressed")

                # x_shape_character(mouse_button_pressed, x_shape)
                # o_shape_movement(keys_pressed, o_shape)
        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()

