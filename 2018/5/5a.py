from collections import defaultdict
from parse import parse


INPUT_FILE = "./input.txt"


def gen_lines():
    for line in open(INPUT_FILE, mode="rt"):
        yield line.strip()


def react(polymer):
    # Format is dabAcCaCBAcCcaDA
    changed = False
    last_pair_reacted = False
    new_polymer = polymer[:1]

    for a, b in zip(polymer, polymer[1:]):
        # print()
        # print((a, b))
        # print(new_polymer)
        # print(last_pair_reacted)

        if last_pair_reacted:
            last_pair_reacted = False
            new_polymer += b
            # print("skipping")
            # print()
            continue

        # print("comparing")
        # print()
        if (a.lower() != b.lower()) or (a == b):
            # print("ignored")
            new_polymer += b

        # Otherwise react!
        else:
            # print("reacted")
            new_polymer = new_polymer[:-1]
            last_pair_reacted = True
            changed = True

    return new_polymer, changed


def main():
    lines = gen_lines()
    polymer = next(lines)

    changed = True

    while changed:
        polymer, changed = react(polymer)
        print("******")
        # print(polymer)
        print(len(polymer))
        print("******")
        # break

    # print(polymer)
    print(len(polymer))


if __name__ == '__main__':
    main()
