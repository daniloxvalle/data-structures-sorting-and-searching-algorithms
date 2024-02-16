# pylint: disable=consider-using-enumerate
from random import randint


def random_unordered_array(length=20, max_value=50) -> list:
    unordered_array = []
    for _ in range(0, length):
        unordered_array.append(randint(0, max_value))
    print("array:", unordered_array)
    return unordered_array


# Quick Sort
# Complexity: O(n log n) - best, average
# Complexity: O(n^2) - worst
# In-place: Yes
# Stable: No
def quick_sort(array: list, start: int = 0, end: int = None) -> list:
    if end is None:
        end = len(array) - 1
    if start < end:
        pivot_index = partition(array, start, end)
        print(f"pivot: {array[pivot_index]} index: {pivot_index}")
        print(array)
        quick_sort(array, start, pivot_index - 1)
        quick_sort(array, pivot_index + 1, end)
    return array


def partition(array: list, start: int, end: int) -> int:
    print(array[start : end + 1])
    pivot = array[end]
    i = start  # new pivot index
    for j in range(start, end):
        if array[j] < pivot:
            # i += 1
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[end] = array[end], array[i]
    return i


# Merge Sort
# Complexity: O(n log n) - best, worst, average
# In-place: No
# Stable: Yes
def merge_sort(array: list, start: int = 0, end: int = None) -> list:
    if end is None:
        end = len(array)
    if end - start > 1:
        # splits the array in half
        middle = (start + end) // 2
        print("left: ", array[start:middle], end="  ")
        print("right: ", array[middle:end], end="  ")
        print("middle:", array[middle])
        merge_sort(array, start, middle)
        merge_sort(array, middle, end)
        # merges the two halves
        merge(array, start, middle, end)


def merge(array: list, start: int, middle: int, end: int) -> list:
    left = array[start:middle]
    right = array[middle:end]

    top_left, top_right = 0, 0
    for k in range(start, end):

        # if left reached the end, add the right element to the array
        if top_left >= len(left):
            array[k] = right[top_right]
            top_right += 1

        # if right reached the end, add the left element to the array
        elif top_right >= len(right):
            array[k] = left[top_left]
            top_left += 1

        # if the left element is smaller than the right element, add the left element to the array
        elif left[top_left] < right[top_right]:
            array[k] = left[top_left]
            top_left += 1

        # if the right element is smaller than the left element, add the right element to the array
        else:
            array[k] = right[top_right]
            top_right += 1

    print(array)
    return array


# Insertion Sort
# Complexity: O(n^2) - worst, average
# Complexity: O(n) - best
# In-place: Yes
# Stable: Yes
def insertion_sort(array: list) -> list:
    if len(array) <= 1:
        return array

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        print(f"{i+1}.", array)
    return array


# Bubble Sort
# Complexity: O(n^2) - best, worst, average
# In-place: Yes
# Stable: Yes
def bubble_sort(array: list) -> list:
    # iterate len(array) times
    for i in range(len(array)):
        # iterate through the array considering the last i elements are already sorted
        for j in range(0, len(array) - i - 1):
            # if the current element is greater than the next element, swap them
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        print(f"{i+1}.", array)
    return array


### Selection Sort ###
# Complexity: O(n^2) - best, worst, average
# In-place: Yes (it doesn't require any extra space)
# Stable: No (it doesn't maintain the relative order of equal elements)
def selection_sort(array: list) -> list:
    # iterate through the array
    for i in range(len(array)):
        # set the min_index to the current index
        min_index = i
        # find the smallest element in the array
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        # swap the smallest element with the min_index element
        array[i], array[min_index] = array[min_index], array[i]
        print(f"{i+1}.", array)
    return array


# selection_sort(random_unordered_array())
# bubble_sort(random_unordered_array())
# insertion_sort(random_unordered_array())
# merge_sort(random_unordered_array(10, 30))
quick_sort(random_unordered_array(10, 30))
