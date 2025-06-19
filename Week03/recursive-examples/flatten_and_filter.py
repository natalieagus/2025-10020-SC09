def flatten_and_filter_even(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            nested_result = flatten_and_filter_even(item)
            for x in nested_result:
                if x % 2 == 0:
                    result.append(x)
        else:
            if item % 2 == 0:
                result.append(item)
    return result

if __name__ == "__main__":
    data = [1, [2, [3, 4], 5], [6]]
    print(flatten_and_filter_even(data))  # Output: [2, 4, 6]
