INPUT_FILE = "./input.txt"


def main():
    print(sum(int(line.strip()) for line in open(INPUT_FILE, mode="rt")))


if __name__ == '__main__':
    main()
