# Own The Game Polska Auto-Clicker

Automatyczny skrypt w Pythonie do gry **Own The Game Polska** w trybie **Celowanie**. Skrypt wykrywa cele na ekranie i automatycznie w nie klika, pomagając zdobywać punkty.

## Funkcje

- Wykrywanie celów na ekranie
- Automatyczne klikanie w wykryte cele
- Sterowanie skryptem za pomocą klawiszy F8 (start) i F9 (stop)

## Wymagania

- Python 3.7+
- Biblioteki:
  - opencv-python
  - numpy
  - pyautogui
  - keyboard
  - Pillow

## Instalacja

1. Sklonuj repozytorium:

   ```bash
   git clone https://github.com/twoja-nazwa/own-the-game-auto-clicker.git
   cd own-the-game-auto-clicker
   ```

2. Zainstaluj wymagane pakiety:
   ```bash
   pip install opencv-python numpy pyautogui keyboard Pillow
   ```

## Użycie

1. Przygotuj obraz celu jako `target.png` w katalogu projektu.
2. Uruchom skrypt:
   ```bash
   python auto_clicker.py
   ```
3. Użyj klawiszy:
   - **F8**: Uruchom skrypt
   - **F9**: Zatrzymaj skrypt

## Uwagi

- Upewnij się, że gra jest widoczna na ekranie podczas działania skryptu.
- Korzystanie ze skryptów automatyzujących może naruszać regulamin gry.

## Licencja

Ten projekt jest udostępniony na licencji MIT.
