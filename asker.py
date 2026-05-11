from db_utils import add_exercise
from conf_utils import get_exercises
import questionary
import pygame

EXERCIES = get_exercises()

def ask_exs():

    pygame.mixer.init()
    pygame.mixer.music.load('alarm.mp3')
    pygame.mixer.music.play(-1)  # -1 = бесконечный цикл

    for e in EXERCIES:
        count = questionary.text(
            f"Введите сколько вы сделали {e}",
            default="10"
        ).ask()
        if count.isdigit() and int(count) > 0:
                add_exercise(e, int(count))
                print(f"✅ {e} зафиксировано: {count}")
    
    print("Данные сохранены.")

    pygame.mixer.music.stop()
    pygame.mixer.quit()
