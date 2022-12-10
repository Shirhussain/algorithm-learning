import collections
from operator import itemgetter
import pprint

with open("test.txt", "r") as f:
    counted_data = collections.Counter(f.read())
    # count_result = pprint.pformat(counted_data)
    # print(count_result, "\n")
    sorted_data = sorted(counted_data.items(), key=itemgetter(1))
    print(sorted_data)
    # for key, value in counted_data.items():
