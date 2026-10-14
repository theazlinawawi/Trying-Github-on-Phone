import random
import time

# Warna & Karakter ala-ala Matrix
chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%^&*"

print("\033[92m=== MATRIX DIGITAL RAIN ===\033[0m\n")
time.sleep(1)

try:
    while True:
        # Hasilkan satu baris rawak
        line = "".join(
            random.choice(chars) if random.random() > 0.4 else " "
            for _ in range(40)
        )
        # Cetak dengan warna hijau neon
        print(f"\033[92m{line}\033[0m")
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\n\033[91m[SYSTEM OFFLINE]\033[0m")
