import cv2
import numpy as np
import pyautogui
import time
import keyboard
from PIL import ImageGrab

# Ścieżka do obrazu celu, np. "target.png"
target_image_path = "target.png"
target_image = cv2.imread(target_image_path, cv2.IMREAD_COLOR)

# Flaga kontrolująca działanie skryptu
running = False

def start_script():
    global running
    if not running:
        running = True
        print("Skrypt został uruchomiony. Naciśnij F9, aby zatrzymać.")

def stop_script():
    global running
    if running:
        running = False
        print("Skrypt został zatrzymany. Naciśnij F8, aby uruchomić ponownie.")

# Przypisz funkcje do klawiszy F8 (włącza) i F9 (wyłącza)
keyboard.add_hotkey("F8", start_script)
keyboard.add_hotkey("F9", stop_script)

print("Naciśnij F8, aby uruchomić skrypt. Naciśnij F9, aby zatrzymać.")

# Rozpocznij pętlę
while True:
    # Skrypt działa tylko wtedy, gdy flaga running jest ustawiona na True
    if running:
        # Przechwyć ekran jako zrzut
        screen = np.array(ImageGrab.grab())
        screen_rgb = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

        # Dopasowanie obrazu
        result = cv2.matchTemplate(screen_rgb, target_image, cv2.TM_CCOEFF_NORMED)
        threshold = 0.9  # Próg dopasowania

        # Znajdź wszystkie lokalizacje, które przekraczają próg
        yloc, xloc = np.where(result >= threshold)

        # Rozmiar obrazu celu
        target_height, target_width, _ = target_image.shape

        # Lista klikniętych pozycji
        clicked_positions = []

        # Kliknij w każdy znaleziony cel
        for (x, y) in zip(xloc, yloc):
            # Oblicz środek celu
            center_x = x + target_width // 2
            center_y = y + target_height // 2

            # Sprawdź, czy to miejsce nie zostało już kliknięte (aby uniknąć wielokrotnego klikania tego samego miejsca)
            if not any(abs(center_x - px) < target_width and abs(center_y - py) < target_height for (px, py) in clicked_positions):
                # Kliknij w środek znalezionego obrazu
                pyautogui.click(center_x, center_y)
                print(f"Kliknięto w cel na pozycji {(center_x, center_y)}")
                clicked_positions.append((center_x, center_y))

