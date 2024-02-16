# pylint: disable=consider-using-enumerate


# Returns the index of the first occurrence of the element in the array
def linear_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return None


array = [12, 6, 9, 41, 33, 10, 24]
element = 33

print(linear_search(array, element))
