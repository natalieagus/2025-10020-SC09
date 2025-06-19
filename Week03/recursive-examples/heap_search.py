def search_heap(heap, index, target):
    if index >= len(heap):
        return False
    if heap[index] > target:
        return False  # Prune branch in min-heap
    if heap[index] == target:
        return True
    left = 2 * index + 1
    right = 2 * index + 2
    return search_heap(heap, left, target) or search_heap(heap, right, target)

min_heap = [1, 3, 5, 7, 9, 6, 8]

target = 6
found = search_heap(min_heap, 0, target)

print(f"Target {target} found in heap: {found}")
