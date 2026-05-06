import argparse
from conf_utils import save_time
from db_utils import show_stats

def term_parse():
    parser = argparse.ArgumentParser(description="Simple terminal programm")
    
    parser.add_argument("-t", "--time", type=int, help="Minutes interval")
    parser.add_argument("--save", action="store_true", help="save settings")
    parser.add_argument("--stats",nargs="?",const=0, type=int, help="stats for n days")

    args = parser.parse_args()

    return args


    
    
