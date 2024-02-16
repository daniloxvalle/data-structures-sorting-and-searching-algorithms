sample_array = [5, 14, 22, 39, 41, 50, 53, 66, 74, 81, 90, 99]


### Binary Search
# Returns the index of the first occurrence of the element in the array
# Complexity: O(log n)
def binary_search(array, value, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    if begin > end:
        #  Value not found
        return None

    middle_index = (begin + end) // 2
    middle_value = array[middle_index]

    if middle_value == value:
        return middle_index

    if middle_value > value:
        return binary_search(array, value, begin, middle_index - 1)

    if middle_value < value:
        return binary_search(array, value, middle_index + 1, end)


print(binary_search(sample_array, 22))
