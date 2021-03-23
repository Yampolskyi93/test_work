"""Develop method which get list as input param and return 2 biggest values in this list
○ Please use python for developing
○ Example:
get_2_max([1,2,3]) => (2,3)
get_2_max([1]) => (1,None)"""


def get_2_max(lst):
    sorted_list = sorted(lst, reverse=True)[:2]
    return sorted_list[0] if len(sorted_list) >= 1 else None, sorted_list[1] if len(sorted_list) == 2 else None


if __name__ == '__main__':
    print(get_2_max([2, 3, 19, 0, -1, 5]))
    print(get_2_max([1]))
    print(get_2_max([]))
