import argparse

def term_parse():
    parser = argparse.ArgumentParser(description="Simple terminal programm")
    
    parser.add_argument("-t", "--time", type=int, default=15, help="Minutes interval")

    args = parser.parse_args()

    return args.time