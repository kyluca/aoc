from collections import defaultdict
from parse import parse


INPUT_FILE = "./input.txt"


def gen_lines():
    for line in open(INPUT_FILE, mode="rt"):
        yield line.strip()


def process_line(line):
    # Format is
    # parsed = parse("", line)
    ...


def main():
    lines = gen_lines()

    for line in lines:
        thing = process_line(line)

    print()


if __name__ == '__main__':
    main()
