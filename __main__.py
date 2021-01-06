import view
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file", action="store", dest="filename")
parser.add_argument("-l", "--no_of_line", action="store", type=int, dest="no_of_line", default=16)
parser.add_argument("-b", "--bytes_per_line", action="store", type=int, dest="bytes_per_line", default=16)

args = parser.parse_args()

view.main(args.filename, args.bytes_per_line, args.no_of_line)