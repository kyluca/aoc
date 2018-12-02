from itertools import accumulate, cycle
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


def main2():
    # Lovely solution from
    # https://www.reddit.com/r/adventofcode/comments/a20646/2018_day_1_solutions/eauapmb
    changes = gen_change()
    seen = set([0])

    print(next(f for f in accumulate(cycle(changes)) if f in seen or seen.add(f)))


if __name__ == '__main__':
    main()
