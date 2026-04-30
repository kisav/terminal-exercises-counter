import os
from dotenv import load_dotenv, set_key

PATH = ".env"

def save_data(time):
    if not os.path.exists(PATH):
        with open(PATH, 'w') as f:
            pass  
    set_key(PATH, "TIME", f"{time}")


