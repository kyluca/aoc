from collections import Counter


INPUT_FILE = "./input.txt"


def main():
    box_ids = sorted(line.strip() for line in open(INPUT_FILE, mode="rt"))
    n = len(box_ids)

    for i, box_id in enumerate(box_ids):
        # Only compare with a few similar boxes, rather than the whole bunch
        similar_boxes = box_ids[max(i - 3, 0):min(i+3, n)]

        for other_box in similar_boxes:
            if box_id == other_box:
                continue

            # Find the first difference
            for j, _ in enumerate(box_id):
                if box_id[j] != other_box[j]:
                    first_different_index = j
                    break

            # Find the last difference
            for k, _ in reversed(list(enumerate(box_id))):
                if box_id[k] != other_box[k]:
                    last_different_index = k
                    break

            # A single difference should occur in the same position
            if first_different_index == last_different_index:
                print("Found a match!")
                print(i)
                print(box_id)
                print(other_box)
                print(box_id[:first_different_index] + box_id[first_different_index + 1:])

                return


if __name__ == '__main__':
    main()
