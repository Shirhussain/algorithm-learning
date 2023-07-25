from operator import attrgetter
from itertools import chain
from datetime import datetime
import heapq


arr1 = [1, 4, 7]
arr2 = [2, 3, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def merge(arr1, arr2):
    return heapq.merge(arr1, arr2)
    # return list(heapq.merge(arr1, arr2))


print(merge(arr1, arr2))

# to print a generator function
# for i in merge(arr1, arr2):
#     print(i)
# or

print(' '.join(map(str, merge(arr1, arr2))))


class DT:
    def __init__(self, dt):
        self.dt = dt


list1 = [DT(datetime(2008, 12, 5, 2)),
         DT(datetime(2009, 1, 1, 13)),
         DT(datetime(2009, 1, 3, 5))]

list2 = [DT(datetime(2008, 12, 31, 23)),
         DT(datetime(2009, 1, 2, 12)),
         DT(datetime(2009, 1, 4, 15))]

list3 = sorted(chain(list1, list2), key=attrgetter('dt'))
for item in list3:
    print(item.dt)


l1 = [1, 3, 4, 7]
l2 = [0, 2, 5, 6, 8, 9]


def merge_two_sorted_list(list1, list2):
    result = []
    while list1 and list2:
        temp = list1.pop(0) if list1 <= list2 else list2.pop(0)
        result.append(temp)

    result.extend(list1 or list2)
    return result


print(merge_two_sorted_list(l1, l2))


def merge_sorted_lists(l1, l2):
    """Merge sort two sorted lists

    Arguments:
    - `l1`: First sorted list
    - `l2`: Second sorted list
    """
    sorted_list = []

    # Copy both the args to make sure the original lists are not
    # modified
    # l1 = l1[:]
    # l2 = l2[:]

    while (l1 and l2):
        item = l1.pop(0) if (l1[0] <= l2[0]) else l2.pop(0)
        sorted_list.append(item)
    # Add the remaining of the lists
    sorted_list.extend(l1 or l2)

    return sorted_list


l1 = [1, 3, 4, 7]
l2 = [0, 2, 5, 6, 8, 9]


if __name__ == '__main__':
    print(merge_sorted_lists(l1, l2))
