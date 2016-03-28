#!/usr/bin/env python

from __future__ import print_function

import sys

from elapsed import total_elapsed_time


def main():
    if len(sys.argv) < 2:
        print('Usage: %s timespec...' % sys.argv[0], file=sys.stderr)
        sys.exit(1)

    delta = total_elapsed_time(','.join(sys.argv[1:]))
    hours = delta.seconds / 3600.0
    print('%s (%.2f)' % (str(delta), hours))

if __name__ == '__main__':
    main()
