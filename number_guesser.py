import pygame
import random
import sys

# Inisialisasi pygame
pygame.init()

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Ukuran layar
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Font
font = pygame.font.Font(None, 36)

# Fungsi untuk menggambar teks di tengah layar
def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)

# Fungsi utama permainan
def game():
    # Batasan angka
    top_of_range = 100
    random_number = random.randint(0, top_of_range)
    guesses = 0

    # Kotak angka tebakan
    guess_box_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50, 100, 100)

    # Tombol +
    plus_button_rect = pygame.Rect(guess_box_rect.right + 10, guess_box_rect.centery - 15, 30, 30)

    # Tombol -
    minus_button_rect = pygame.Rect(guess_box_rect.left - 40, guess_box_rect.centery - 15, 30, 30)

    # Tombol Cek
    check_button_rect = pygame.Rect(guess_box_rect.left, guess_box_rect.bottom + 10, 100, 50)

    # Loop permainan
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if plus_button_rect.collidepoint(event.pos):
                    guesses += 1
                elif minus_button_rect.collidepoint(event.pos):
                    guesses -= 1
                elif check_button_rect.collidepoint(event.pos):
                    if guesses == random_number:
                        print("Selamat, kamu benar!")
                        running = False
                    elif guesses > random_number:
                        print("Masih di atas nomor yang benar nih, turunkan tebakanmu..")
                    else:
                        print("Kalau ini, di bawah nomor yang benar, naikkan tebakanmu..")

        # Tampilan permainan
        screen.fill(WHITE)
        pygame.draw.rect(screen, GRAY, guess_box_rect)
        draw_text(screen, str(guesses), font, BLACK, guess_box_rect.centerx, guess_box_rect.centery)
        pygame.draw.rect(screen, GRAY, plus_button_rect)
        pygame.draw.rect(screen, GRAY, minus_button_rect)
        pygame.draw.rect(screen, GRAY, check_button_rect)
        draw_text(screen, "+", font, BLACK, plus_button_rect.centerx, plus_button_rect.centery)
        draw_text(screen, "-", font, BLACK, minus_button_rect.centerx, minus_button_rect.centery)
        draw_text(screen, "Cek", font, BLACK, check_button_rect.centerx, check_button_rect.centery)
        pygame.display.flip()

# Main loop
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Permainan Tebak Angka")

# Tombol "Mulai"
start_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 30, 200, 50)

# Tombol "Keluar"
quit_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 50)

while True:
    screen.fill(WHITE)
    draw_text(screen, "Find My Hide Number", font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    pygame.draw.rect(screen, GRAY, start_button_rect)
    pygame.draw.rect(screen, GRAY, quit_button_rect)
    draw_text(screen, "Mulai", font, BLACK, start_button_rect.centerx, start_button_rect.centery)
    draw_text(screen, "Keluar", font, BLACK, quit_button_rect.centerx, quit_button_rect.centery)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if start_button_rect.collidepoint(event.pos):
                    game()
                elif quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
