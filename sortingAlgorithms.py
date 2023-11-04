import random


#############################################################################
def bubble_sort(array, start, end, key):
    for i in range(start, end):
        swapped = False
        for j in range(start, end - i + start):
            if key(array[j]) > key(array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped == False:
            break
    return array


############################################################################
def selection_sort(array, start, end, key):
    for i in range(start, end):
        smallest = i
        for j in range(i + 1, end + 1):
            if key(array[j]) < key(array[smallest]):
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]
    return array


#############################################################################
def insertion_sort(array, start, end, key):
    n = end - start + 1
    for i in range(start + 1, start + n):
        key_element = array[i]
        j = i - 1
        while j >= start and (key(array[j]) > key(key_element)):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key_element
    return array


#############################################################################
def merge_sort(array, start, end, key):
    if start < end:
        mid = (start + end) // 2
        merge_sort(array, start, mid, key)
        merge_sort(array, mid + 1, end, key)
        merge(array, start, mid, end, key)
    return array


def merge(array, start, mid, end, key):
    left_array = array[start : mid + 1]
    right_array = array[mid + 1 : end + 1]
    i = j = 0
    k = start

    while i < len(left_array) and j < len(right_array):
        if key(left_array[i]) <= key(right_array[j]):
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1
    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1
    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1


################################################################################
def hybrid_merge_sort(array, start, end, key):
    if start >= end:
        return
    if start < end:
        if end - start <= 30:
            insertion_sort(array, start, end, key)
        else:
            mid = (start + end) // 2

            hybrid_merge_sort(array, start, mid, key)
            hybrid_merge_sort(array, mid + 1, end, key)

            left_array = array[start : mid + 1]
            right_array = array[mid + 1 : end + 1]

            i = j = 0
            k = start

            while i < len(left_array) and j < len(right_array):
                if key(left_array[i]) <= key(right_array[j]):
                    array[k] = left_array[i]
                    i += 1
                else:
                    array[start + k] = right_array[j]
                    j += 1
                k += 1

            while i < len(left_array):
                array[k] = left_array[i]
                i += 1
                k += 1

            while j < len(right_array):
                array[k] = right_array[j]
                j += 1
                k += 1
    return array


################################################################################
def quick_sort(array, start, end, key):
    if start < end:
        pv = partition(array, start, end, key)
        quick_sort(array, start, pv - 1, key)
        quick_sort(array, pv + 1, end, key)
    return array


def partition(array, start, end, key):
    random_indx = random.randint(start + 1, end)
    array[random_indx], array[end] = array[end], array[random_indx]
    pivot = key(array[end])
    i = start - 1
    for j in range(start, end):
        if key(array[j]) <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1


#############################################################################
def even_odd_sort(array, start, end, key):
    n = len(array)
    # if you are sorting from in between
    if end - start + 1 != len(array):
        n = end + start - 1

    is_sorted = False
    while not is_sorted:
        is_sorted = True
        # Sort even-indexed elements
        for i in range(start, n, 2):
            if i + 1 < n and (key(array[i]) > key(array[i + 1])):
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
        # Sort odd-indexed elements
        for i in range(start + 1, n, 2):
            if i + 1 < n and (key(array[i]) > key(array[i + 1])):
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
    return array


############################################################################
def heapify(arr, n, i, key):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # See if left child of root exists and is greater than root
    if left_child < n and (key(arr[left_child]) > key(arr[largest])):
        largest = left_child
    # See if right child of root exists and is greater than root
    if right_child < n and (key(arr[right_child]) > key(arr[largest])):
        largest = right_child
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Heapify the root
        heapify(arr, n, largest, key)


def heap_sort(array, start, end, key):
    n = end - start + 1
    # Build a maxheap
    for i in range((n // 2) - 1, start - 1, -1):
        heapify(array, end, i, key)
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        array[start + i], array[start] = array[start], array[start + i]
        heapify(array, start + i, 0, key)

    return array


###################################################################
###########TESTING OUTPUTS OF COMPARISON BASED ALGORITHMS##########
###################################################################
# print(even_odd_sort(test))


###################################################################
def count_sort(array, start, end, key):
    max_key = max(key(video) for video in array[start : end + 1])
    min_key = min(key(video) for video in array[start : end + 1])
    k = max_key - min_key + 1
    n = end - start + 1  # Number of elements to sort
    count = [0] * k
    output = [None] * n

    # Store Count of each element
    for i in range(start, end + 1):
        count[key(array[i]) - min_key] += 1
    # Calculate cumulative counts
    for i in range(1, k):
        count[i] += count[i - 1]
    # Place items in the correct position in the output array
    for i in range(end, start - 1, -1):
        video = array[i]
        count[key(video) - min_key] -= 1
        output[count[key(video) - min_key]] = video
    # Copy the sorted output back to the original array
    for i in range(n):
        array[start + i] = output[i]


###################################################################
# def radix_sort(array, start, end, key):
#     mul = 1
#     max_key = max(key(video) for video in array[start:end + 1])
#     while max_key // mul > 0:
#         output = counting_sort(array, mul, start, end, key)
#         array[start:end + 1] = output
#         mul *= 10

#     return array

# def counting_sort(array, mul, start, end, key):
#     temp = []
#     for num in array:
#         num = num // mul
#         mod = num % 10
#         temp.append(mod)

#     n = len(temp)
#     maxi = max(temp)
#     k = maxi + 1  # Calculate the range of elements in the array
#     count = [0] * k
#     output = [0] * n

#     # Store Count of each element
#     for num in temp:
#         count[num] += 1

#     # Store cumulative count in array
#     for i in range(1, k):
#         count[i] += count[i - 1]

#     for i in range(end, start - 1, -1):
#         count[temp[i]] -= 1
#         output[count[temp[i]]] = array[end - i]
#     # Copy the sorted output back to the original array
#     for i in range(n):
#         array[start + i] = output[i]

#     return output
########################################################################
# def bucket_sort(array, start, end, key):
#     # Determine the number of buckets (n)
#     n = end - start + 1
#     buckets = [[] for _ in range(n)]
#     # Determine the range of key values in the specified range
#     min_key = key(array[start])
#     max_key = key(array[start])
#     for i in range(start, end + 1):
#         current_key = key(array[i])
#         if current_key < min_key:
#             min_key = current_key
#         if current_key > max_key:
#             max_key = current_key

#     # Insert elements in buckets based on key within the specified range
#     for i in range(start, end + 1):
#         current_key = key(array[i])
#         index = int(n * (current_key - min_key) / (max_key - min_key))
#         index = max(0, min(n - 1, index))  # Ensure index is within a valid range
#         buckets[index].append(array[i])

#     # Sort each bucket with insertion sort
#     for bucket in buckets:
#         insertion_sort(bucket, 0, len(bucket) - 1, key)

#     # Concatenate all buckets into an output array
#     output = [element for bucket in buckets for element in bucket]
#     # Copy the sorted output back to the original array within the specified range
#     for i, element in enumerate(output):
#         array[start + i] = element

#     return array


def bucket_sort(array, start, end, key):
    n = end - start + 1
    buckets = [[] for _ in range(n)]

    # Insert elements in buckets based on key within the specified range
    for i in range(start, end + 1):
        current_key = key(array[i])
        index = int(n * current_key)
        index = max(0, min(n - 1, index))
        buckets[index].append(array[i])

    # Sort each bucket with insertion sort
    for bucket in buckets:
        insertion_sort(bucket, 0, len(bucket) - 1, key)

    # Concatenate all buckets into an output array
    output = [element for bucket in buckets for element in bucket]
    # Copy the sorted output back to the original array within the specified range
    for i, element in enumerate(output):
        array[start + i] = element

    return array


###########################################################################
def pigeonhole_sort(array, start, end, key):
    min_number = min(key(item) for item in array[start : end + 1])
    max_number = max(key(item) for item in array[start : end + 1])
    size = max_number - min_number + 1
    n = end - start + 1
    holes = [0] * size

    # Populate the pigeonholes.
    for item in array[start : end + 1]:
        holes[key(item) - min_number] += 1

    # Put the elements back into the array in order.
    sorted_values = [0] * n
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1

            for j in range(n):
                if key(array[start + j]) == count + min_number:
                    sorted_values[i] = array[start + j]
                    i += 1
                    break
    # Assign the sorted values back to the original array
    for i in range(n):
        array[start + i] = sorted_values[i]

    return array


#############################################################################
def bead_sort(array, start, end, key):
    # If sorting the entire array, n remains the same
    n = len(array)
    # Check if we are sorting the entire array or a specified range
    if end - start + 1 != len(array):
        n = end - start + 1

    maximum = max(key(item) for item in array[start : end + 1])
    beads = [[0] * maximum for _ in range(n)]

    for i in range(n):
        for j in range(key(array[start + i])):
            beads[i][j] = 1

    for j in range(maximum):
        drop_beads_by_column = 0
        for i in range(n):
            drop_beads_by_column += beads[i][j]
            beads[i][j] = 0
        for i in range(n - 1, n - drop_beads_by_column - 1, -1):
            beads[i][j] = 1

    sorted_values = [0] * n
    for i in range(n):
        num_beads_in_row = beads[i].count(1)
        for j in range(n):
            if key(array[start + j]) == num_beads_in_row:
                sorted_values[i] = array[start + j]
                break
    # Assign the sorted values back to the original array
    for i in range(n):
        array[start + i] = sorted_values[i]
    return array


##############################################################################
def radix_sort(array, start, end, key):
    n = end - start + 1
    max_key = max(key(item) for item in array[start : end + 1])
    mul = 1

    while max_key // mul > 0:
        counting_sort(array, start, end, key, mul)
        mul *= 10

    return array


def counting_sort(array, start, end, key, mul):
    n = end - start + 1
    output = [0] * n
    count = [0] * 10

    for i in range(start, end + 1):
        count[(key(array[i]) // mul) % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (key(array[start + i]) // mul) % 10
        output[count[index] - 1] = array[start + i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        array[start + i] = output[i]
