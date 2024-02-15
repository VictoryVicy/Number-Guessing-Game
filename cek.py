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

        # Handling input tebakan pengguna
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            guesses += 1
            user_guess = random.randint(0, top_of_range)
            if user_guess == random_number:
                print("Selamat, kamu benar!")
                running = False
            elif user_guess > random_number:
                print("Masih di atas nomor yang benar nih, turunkan tebakanmu..")
            else:
                print("Kalau ini, di bawah nomor yang benar, naikkan tebakanmu..")
        elif key[pygame.K_DOWN]:
            guesses -= 1
            user_guess = random.randint(0, top_of_range)
            if user_guess == random_number:
                print("Selamat, kamu benar!")
                running = False
            elif user_guess > random_number:
                print("Masih di atas nomor yang benar nih, turunkan tebakanmu..")
            else:
                print("Kalau ini, di bawah nomor yang benar, naikkan tebakanmu..")

        # Tampilan permainan
        screen.fill(WHITE)
        draw_text(screen, "Tebak Angka", font, BLACK, SCREEN_WIDTH // 2, 50)
        draw_text(screen, "Tebakan: {}".format(guesses), font, BLACK, SCREEN_WIDTH // 2, 100)
        draw_text(screen, "Tekan panah atas untuk menebak", font, BLACK, SCREEN_WIDTH // 2, 150)
        pygame.display.flip()

# Main loop
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Permainan Tebak Angka")

while True:
    screen.fill(WHITE)
    draw_text(screen, "Find My Hide Number", font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    draw_text(screen, "Tekan spasi untuk memulai", font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text(screen, "Tekan ESC untuk keluar", font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_SPACE:
                game()
