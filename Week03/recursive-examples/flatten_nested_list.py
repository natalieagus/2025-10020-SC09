def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

if __name__ == "__main__":
    nested = [1, [2, [3, 4], 5], 6]
    print("flatten([1, [2, [3, 4], 5], 6]):", flatten(nested))


# Iterative version using a stack
def flatten_iterative(lst):
    stack = [lst[::-1]]
    result = []
    while stack:
        current = stack.pop()
        while current:
            item = current.pop()
            if isinstance(item, list):
                stack.append(current)
                current = item[::-1]
            else:
                result.append(item)
    return result

if __name__ == "__main__":
    nested = [1, [2, [3, 4], 5], 6]
    print("flatten_iterative([1, [2, [3, 4], 5], 6]):", flatten_iterative(nested))
