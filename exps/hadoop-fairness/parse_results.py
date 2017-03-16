#!/usr/bin/python

import argparse
import numpy as np
import os
import re
import scipy.stats
import sys
import yaml

FLOAT_DESC_STR = '[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'

def get_percentile(data, percentile):
    return np.asscalar(scipy.stats.scoreatpercentile(data, percentile))

def parse_files(files):
    cts = []
    for fname in files:
        with open(fname) as resf:
            lines = resf.readlines()
            finish_ts = 0
            for line in lines:
                match = re.match(".*Job.*finished.* (%s) s.*" % FLOAT_DESC_STR, line)
                if match:
                    ts = float(match.groups()[0])
                    finish_ts = max(finish_ts, ts)
            cts.append(finish_ts)
    print yaml.dump(cts)
    return cts

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description='Parse the output of the '
        'Spark fairness experiments.')
    parser.add_argument('files', help='The output of the spark fairness runs.',
        nargs='+')
    args = parser.parse_args()

    # Parse the files
    completion_times = parse_files(args.files)
    print 'median:', get_percentile(completion_times, 50)
    print '75p:', get_percentile(completion_times, 75)


if __name__ == '__main__':
    main()
