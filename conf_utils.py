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
