import argparse
from conf_utils import save_time

def term_parse():
    parser = argparse.ArgumentParser(description="Simple terminal programm")
    
    parser.add_argument("-t", "--time", type=int, default=15, help="Minutes interval")
    parser.add_argument("--save", action="store_true", help="save settings")

    args = parser.parse_args()

    if args.time and args.save:
        save_time(args.time)
        return -1
    elif args.time:
        return args.time