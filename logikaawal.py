import random

top_of_range = input("Tentukan batasan angka yang ingin ditebak: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Tolong masukan angka positif di atas 0!")
        quit()
else:
    print("Tolong masukan angka!")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Mari kita cek intuisi mu, masukkan tebakan angka mu: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Tolong masukan angka!")
        continue

    if user_guess == random_number:
        print("Selamat, kamu benar!")
        break
    elif user_guess > random_number:
        print("Masih di atas nomor yang benar nih, turunkan tebakanmu..")
    else:
        print("Kalau ini, di bawah nomor yang benar, naikkan tebakanmu..")

print("Kamu benar dengan", guesses, "tebakan")
