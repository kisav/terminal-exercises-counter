import questionary
from loguru import logger
import time
from plyer import notification

logger.add("workout_stats.log", format="{time:YYYY-MM-DD HH:mm:ss} | {message}")
EXERCIES = ["приседаний", "отжиманий", "пресса"]

def ask():
    
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
    ask()
    time.sleep(10) 
    notification.notify(
        title='Упражнения',
        message='Пора размяться!',
        app_name='terminal_exercise',
        timeout=10
    )