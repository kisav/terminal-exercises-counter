import questionary
import time
from plyer import notification
from playsound import playsound
from conf_utils import get_time
from terminal_parser import term_parse
from db_utils import init_db, add_exercise

init_db()
EXERCIES = ["приседаний", "отжиманий", "пресса"]

def ask_exs():
    for e in EXERCIES:
        count = questionary.text(
            f"Введите сколько вы сделали {e}",
            default="10"
        ).ask()
        if count.isdigit() and int(count) > 0:
                add_exercise(e, int(count))
                print(f"✅ {e} зафиксировано: {count}")
    
    print("Данные сохранены. Следующий опрос через 15 минут.")

while True:
    result = term_parse()

    if isinstance(result, str):
        print(result)
        exit()
    notification.notify(
        title='Упражнения',
        message='Пора размяться!',
        app_name='terminal_exercise',
        timeout=10
    )
    playsound('alarm.mp3')
    if result == -1:
        sleepy_time = get_time()
        print(sleepy_time)
    else:
        sleepy_time = result
        print(sleepy_time)
    ask_exs()
    time.sleep(sleepy_time)