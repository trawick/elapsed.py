from datetime import datetime, timedelta


def parse_time(s):
    try:
        return datetime.strptime(s, '%H:%M')
    except ValueError:
        return datetime.strptime(s, "%H:%M:%S")


def elapsed_time(s):
    if '-' in s:
        start, stop = s.split('-')
    else:
        start, stop = '0:00', s
    start = parse_time(start)
    stop = parse_time(stop)
    return stop - start


def total_elapsed_time(s):
    delta = timedelta(seconds=0)
    if isinstance(s, str):
        items = s.split(',')
    else:
        items = s
    for s1 in items:
        delta += elapsed_time(s1.strip())
    return delta
