# Started late: 9:00pm - 9:06pm (6 mins)
from collections import defaultdict


INPUT_FILE = "./input.txt"


def main():
    # Use a sparse mapping rather than initialising 1000 x 1000 matrix
    fabric_map = defaultdict(lambda: defaultdict(list))
    claim_ids = set()

    for line in open(INPUT_FILE, mode="rt"):
        claim_id, start_x, start_y, size_x, size_y = process_line(line)
        claim_ids.add(claim_id)

        for x in range(start_x, start_x + size_x):
            for y in range(start_y, start_y + size_y):
                fabric_map[x][y].append(claim_id)

    # Find any fabric locations with more than one booking
    overloaded_fabric_locations = [
        (x, y)
        for x in fabric_map
        for y in fabric_map[x]
        if len(fabric_map[x][y]) > 1
    ]

    overlapping_claims = {
        claim_id
        for x, y in overloaded_fabric_locations
        for claim_id in fabric_map[x][y]
    }

    print(f"Number of overloaded fabric locations: {len(overloaded_fabric_locations)}")
    print(f"Number of overlapping claims: {len(overlapping_claims)}")
    print(f"Non-overlapping claims: {claim_ids - overlapping_claims}")


def process_line(line):
    # Claim format: "#123 @ 3,2: 5x4"
    claim_id, _, start, size = line.strip().split()

    start_x, start_y = start.strip(":").split(",")
    size_x, size_y = size.split("x")

    return claim_id, int(start_x), int(start_y), int(size_x), int(size_y)


if __name__ == '__main__':
    main()
