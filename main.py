import questionary
import time
from plyer import notification
from playsound import playsound
from conf_utils import get_time, save_time, add_exercises
from terminal_parser import term_parse
from db_utils import init_db, show_stats
from asker import ask_exs

init_db()

args = term_parse()



if args.configure:
    exercises = questionary.text(
        f"Введите название упражнения, которое хотите добавить "
    ).ask()
    add_exercises(exercises)
    print(f"Упражнение {exercises} успешно добавлено")
    exit()
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

    ask_exs()
    print(f"Следующий запрос через {sleepy_time} секунд.")
    time.sleep(sleepy_time)