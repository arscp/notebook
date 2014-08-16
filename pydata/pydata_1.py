__author__ = 'celery_qcc'

#Get current working directly
import os
os.getcwd()

import json
path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
#open(path).readline()
records = [json.loads(line) for line in open(path)]
#records[3]['a']
time_zones = [rec['tz'] for rec in records if 'tz' in rec]


def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

from collections import defaultdict

def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts



def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

from collections import Counter
counts = Counter(time_zones)
counts.most_common(10)


from pandas import DataFrame, Series
import pandas as pd
from matplotlib import pyplot as plt
from IPython.core.pylabtools import figsize

figsize(11, 9)
frame = DataFrame(records)

tz_counts = frame['tz'].value_counts()
tz_counts[:10].plot(kind='barh', rot=0)
plt.show()

