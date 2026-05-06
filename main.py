import questionary
from loguru import logger
import time
from plyer import notification
from playsound import playsound
from conf_utils import get_time
from terminal_parser import term_parse


logger.add("workout_stats.log", format="{time:YYYY-MM-DD HH:mm:ss} | {message}")
EXERCIES = ["приседаний", "отжиманий", "пресса"]

def ask_exs():
    
    for e in EXERCIES:
        count = questionary.text(
            f"Введите сколько вы сделали {e}",
            default="10"
        ).ask()
        if count.isdigit() and int(count) > 0:
                logger.info(f"{e}: {count}")
                print(f"✅ {e} зафиксировано: {count}")
    
    print("Данные сохранены. Следующий опрос через 15 минут.")

while True:
    term_parse()
    notification.notify(
        title='Упражнения',
        message='Пора размяться!',
        app_name='terminal_exercise',
        timeout=10
    )
    playsound('alarm.mp3')
    if term_parse() == -1:
        sleepy_time = get_time()
        print(sleepy_time)
    else:
        sleepy_time = term_parse()
        print(sleepy_time)
    ask_exs()
    time.sleep(sleepy_time)