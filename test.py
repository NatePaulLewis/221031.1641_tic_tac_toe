# PYGAME BUILD
import pygame
import os

WIDTH, HEIGHT = 1224, 792
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")

BG_COLOR = (32, 32, 32,)

FPS = 60
VEL = 5
CHARACTER_WIDTH, CHARACTER_HEIGHT = 256, 256

X9 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_x9.png'))
X8 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_x8.png'))
GAME_BOARD = pygame.image.load(os.path.join('assets', 'tic_tac_toe_game_board.png'))


def draw_window():
    WIN.fill(BG_COLOR)
    WIN.blit(GAME_BOARD, (0, 0))
    if pygame.MOUSEBUTTONDOWN:
        mouse_button_pressed = pygame.mouse.get_pressed()
        if mouse_button_pressed[0]:
            WIN.blit(X8, (0, 0))
    pygame.display.update()


def x_character():
    if pygame.MOUSEBUTTONDOWN:
        mouse_button_pressed = pygame.mouse.get_pressed()
        if mouse_button_pressed[0]:
            print("left is being pressed")
            WIN.blit(X9, (0, 0))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            x_character()
        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()

