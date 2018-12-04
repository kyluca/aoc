from collections import defaultdict


INPUT_FILE = "./input.txt"


def gen_lines():
    for line in open(INPUT_FILE, mode="rt"):
        yield line


def main():
    current_guard = None
    lines = gen_lines()
    guard_logs = defaultdict(list)

    for line in lines:
        date, hour, minute, guard_id, action = process_line(line)

        if guard_id is not None:
            current_guard = guard_id

        if action == "falls":
            # Get the "wakes" line
            next_line = next(lines)
            next_date, next_hour, next_minute, next_guard_id, next_action = process_line(next_line)

            guard_logs[current_guard].append((date, hour, next_hour, minute, next_minute))

    guard_sleeping_sums = {
        guard_id: sum((log[4] - log[3]) for log in guard_log)
        for guard_id, guard_log in guard_logs.items()
    }

    def get_max_sleeping_time(guard_id):
        max_sleeping_time = defaultdict(list)
        for log in guard_logs[guard_id]:
            for minute in range(log[3], log[4]):
                max_sleeping_time[minute].append(log[0])

        max_sleeping_minute = max(max_sleeping_time.items(), key=lambda x: len(x[1]))
        return max_sleeping_minute[0], len(max_sleeping_minute[1])

    all_sleep_minutes = {
        guard_id: get_max_sleeping_time(guard_id)
        for guard_id in guard_sleeping_sums.keys()
    }

    max_sleeping_guard = max(all_sleep_minutes.items(), key=lambda x: x[1][1])

    print(max_sleeping_guard)
    print(int(max_sleeping_guard[0]) * max_sleeping_guard[1][0])


def process_line(line):
    timestamp, log = line.strip().strip("[").split("] ")
    date, time = timestamp.split()
    hour, minute = time.split(":")

    try:
        _, guard_id, _, _ = log.split()
        guard_id = guard_id.strip("#")
        action = None

    except:
        action, _ = log.split()
        guard_id = None

    return date, int(hour), int(minute), guard_id, action


if __name__ == '__main__':
    main()


# year-month-day hour:minute

# [1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up
