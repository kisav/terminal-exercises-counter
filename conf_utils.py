import configparser

def save_time(time):
    config = configparser.ConfigParser()

    config['SETTINGS'] = {
        "time":f"{time}"
    }


    with open("app.conf", "w") as f:
        config.write(f)


def get_time():
    config = configparser.ConfigParser()
    config.read("app.conf")

    try:
        time = int(config["SETTINGS"]['time'])
        return time

    except Exception:
        return 15

def get_exercises():
    config = configparser.ConfigParser()
    config.read('app.conf')

    try:
        exercises = config["EXERCISES"]["exercises"].split(",")
    except KeyError:
        config['EXERCISES'] = {
            "exercises":""
        }
        exercises = []


    return exercises

def add_exercises(exercise):
    config = configparser.ConfigParser()

    exercises = get_exercises()

    exercises.append(exercise)

    config["EXERCISES"] = {
        "exercises": ",".join(exercises)
    }

    with open("app.conf", "w") as f:
        config.write(f)