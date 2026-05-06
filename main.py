import questionary
import time
from plyer import notification
from playsound import playsound
from conf_utils import get_time, save_time
from terminal_parser import term_parse
from db_utils import init_db, add_exercise, show_stats

init_db()
EXERCIES = ["приседаний", "отжиманий", "пресса"]
args = term_parse()


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


if args.time and not args.save:
    sleepy_time = args.time
elif not args.time:
    sleepy_time = get_time()
elif args.time and args.save:
    sleepy_time = args.time
    save_time(args.time)
    print(sleepy_time)
    exit()

if args.stats is None:
    pass
elif args.stats == 0:
    print(show_stats(None))
    exit()
else:
    print(show_stats(args.stats))
    exit()

while True:
    

    notification.notify(
        title='Упражнения',
        message='Пора размяться!',
        app_name='terminal_exercise',
        timeout=10
    )
    playsound('alarm.mp3')
    print(sleepy_time)
    ask_exs()
    time.sleep(sleepy_time)