import math


def merge(*args):
    left, right = args[0] if len(args) == 1 else args
    left_length, right_length = len(left), len(right)
    left_index, right_index = 0, 0
    merged = []
    while left_index < left_length and right_index < right_length:
        if left[left_index][2] <= right[right_index][2]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    if left_index == left_length:
        merged.extend(right[right_index:])
    else:
        merged.extend(left[left_index:])
    return merged


def merge_sort(data, *args):
    length = len(data)
    if length <= 1:
        return data
    middle = length // 2
    left, right = merge_sort(data[:middle]), merge_sort(data[middle:])
    return merge(left, right)


def merge_sort_parallel(data, pool, threads):
    size = int(math.ceil(float(len(data)) / threads))
    data = [data[i * size:(i + 1) * size] for i in range(threads)]
    data = pool.map(merge_sort, data)
    while len(data) > 1:
        extra = data.pop() if len(data) % 2 == 1 else None
        paired_data = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
        data = [merge(data_pair) for data_pair in paired_data] + ([extra] if extra else [])
    return data[0]
