from collections import Counter


INPUT_FILE = "./input.txt"


def gen_change():
    for line in open(INPUT_FILE, mode="rt"):
        yield int(line.strip())


def main():
    frequency = 0
    results = Counter({0: 0})
    i = 0
    changes = gen_change()

    while results.most_common(1)[0][1] < 2:
        frequency += next(changes)
        results[frequency] += 1

        i += 1

    print(i)
    print(results.most_common(1)[0])


if __name__ == '__main__':
    main()
