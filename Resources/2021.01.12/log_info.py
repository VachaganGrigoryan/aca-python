from collections import defaultdict


def yield_file(file_path: str):
    with open(file_path, 'r') as logfile:
        for line in logfile:
            yield line


def get_log_category(line: str):
    return line.split(' - ')[1].strip()


if __name__ == '__main__':
    counts = defaultdict(int)
    for category in map(get_log_category, yield_file('application.log')):
        counts[category] += 1
    print(counts)
        
