import argparse
from conf_utils import save_time
from db_utils import show_stats

def term_parse():
    parser = argparse.ArgumentParser(description="Simple terminal programm")
    
    parser.add_argument("-t", "--time", type=int, help="Minutes interval")
    parser.add_argument("--save", action="store_true", help="save settings")
    parser.add_argument("--stats", action="store_true", help="stats for all time")


    args = parser.parse_args()

    if args.time and args.save:
        save_time(args.time)
        return -1
    elif args.time:
        return args.time
    
    if args.stats:
        return show_stats()