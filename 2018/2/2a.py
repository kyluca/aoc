from collections import Counter


INPUT_FILE = "./input.txt"


def main():
    two_matched_count = 0
    three_matched_count = 0

    # One pass over the list rather than using sum() and doing two passes
    for line in open(INPUT_FILE, mode="rt"):
        box_id = line.strip()

        if matches_2(box_id):
            two_matched_count += 1

        if matches_3(box_id):
            three_matched_count += 1

    print(two_matched_count * three_matched_count)


def matches_2(box_id):
    return 2 in Counter(box_id).values()


def matches_3(box_id):
    return 3 in Counter(box_id).values()


if __name__ == '__main__':
    main()
