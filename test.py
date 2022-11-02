# PYGAME BUILD
import pygame
import os

WIDTH, HEIGHT = 1224, 792
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")

BG_COLOR = (32, 32, 32,)
FPS = 60
CLOCK = pygame.time.Clock()
VEL = 5
CHARACTER_WIDTH, CHARACTER_HEIGHT = 256, 256



X9 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_x9.png'))
X8 = pygame.image.load(os.path.join('assets', 'tic_tac_toe_x8.png'))
GAME_BOARD = pygame.image.load(os.path.join('assets', 'tic_tac_toe_game_board.png'))

def draw_window():
    WIN.fill(BG_COLOR)
    WIN.blit(GAME_BOARD, (0, 0))
    if pygame.MOUSEBUTTONDOWN:
        mouse_click = pygame.mouse.get_pressed()
        if mouse_click[0]:
            WIN.blit(X9, (0, 0))
            print('left click')
    pygame.display.update()

def x_character():
    mouse_click = pygame.mouse.get_pressed()
    if mouse_click[0]:
        WIN.blit(X8, (0, 0))
        print('left click')
        pygame.display.update()

def main():
    run = True
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()
        draw_window()
        x_character()
        pygame.display.update()
if __name__ == "__main__":
    main()