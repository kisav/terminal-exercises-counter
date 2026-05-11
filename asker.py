import threading
from playsound import playsound
import questionary
from db_utils import add_exercise
from conf_utils import get_exercises
import questionary

EXERCIES = get_exercises()

def play_alarm_continuous(stop_event):
    while not stop_event.is_set():
        playsound('alarm.mp3')

def ask_exs():
    stop_event = threading.Event()
    alarm_thread = threading.Thread(target=play_alarm_continuous, args=(stop_event,))
    alarm_thread.start()

    try:
        for e in EXERCIES:
            count = questionary.text(
                f"Введите сколько вы сделали {e}",
                default="10"
            ).ask()
            if count.isdigit() and int(count) > 0:
                add_exercise(e, int(count))
                print(f"✅ {e} зафиксировано: {count}")
        print("Данные сохранены.")
    finally:
        stop_event.set()
        alarm_thread.join()