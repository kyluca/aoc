from collections import defaultdict


INPUT_FILE = "./input.txt"


def gen_lines():
    for line in open(INPUT_FILE, mode="rt"):
        yield line.strip()


def process_line(line):
    ...


def main():
    lines = gen_lines()

    for line in lines:
        thing = process_line(line)


if __name__ == '__main__':
    main()
