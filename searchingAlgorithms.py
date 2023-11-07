from math import sqrt
###############################################################################
def linear_search_equals(array, start, end, target, key):
    result = []
    for i in range(start, end+1):
        if str(key(array[i])) == str(target):
            result.append(array[i])   
    return result          

def linear_search_contains(array, start, end, target, key):
    result = []
    for i in range(start, end+1):
        if str(target) in str(key(array[i])):
            result.append(array[i])   
    return result 

def linear_search_startswith(array, start, end, target, key):
    result = []
    for i in range(start, end+1):
        if str(key(array[i])).startswith(str(target)):
            result.append(array[i])
    return result

def linear_search_endswith(array, start, end, target, key):
    result = []
    for i in range(start, end+1):
        if str(key(array[i])).endswith(str(target)):
            result.append(array[i])
    return result


def linearSearch(array, start, end, target, filter, key):
    if filter == "--Select filter--":
        return linear_search_equals(array, start, end, target, key)
    if filter == "Contains":
        return linear_search_contains(array, start, end, target, key)
    elif filter == "Starts With":
        return linear_search_startswith(array, start, end, target, key)
    elif filter == "Ends With":
        return linear_search_endswith(array, start, end, target, key)



##########################################################################


def binary_search_equals(array, start, end, target, key):
    result = []
    while start <= end:
        mid = start + (end - start) // 2
        if str(target) == str(key(array[mid])):
            result.append(array[mid])
            # Continue searching on both sides of the midpoint for more matches
            left_idx = mid - 1
            right_idx = mid + 1
            # Search to the left for more matches
            while left_idx >= start and str(target) == str(key(array[left_idx])):
                result.append(array[left_idx])
                left_idx -= 1
            # Search to the right for more matches
            while right_idx <= end and str(target) == str(key(array[right_idx])):
                result.append(array[right_idx])
                right_idx += 1
            return result
        elif target < str(key(array[mid])):
            end = mid - 1
        else:
            start = mid + 1
    return result  # No matches found

def binary_search_contains(array, start, end, target, key):
    result = []

    while start <= end:
        mid = start + (end - start) // 2
        element = str(key(array[mid]))
        
        if str(target) in str(element):
            # Continue searching to the left for more matches
            left_idx = mid - 1
            while left_idx >= start and str(target) in str(key(array[left_idx])):
                result.append(array[left_idx])
                left_idx -= 1
            # Search to the right for more matches
            right_idx = mid + 1
            while right_idx <= end and str(target) in str(key(array[right_idx])):
                result.append(array[right_idx])
                right_idx += 1

            result.append(array[mid])  # Add the current match
            return result
        elif target < element:
            end = mid - 1
        else:
            start = mid + 1

    return result

def binary_search_startswith(array, start, end, target, key):
    result = []
    
    while start <= end:
        mid = start + (end - start) // 2
        element = str(key(array[mid]))

        if element.startswith(target):
            # Continue searching to the left for more matches
            left_idx = mid - 1
            while left_idx >= start and key(array[left_idx]).startswith(target):
                result.append(array[left_idx])
                left_idx -= 1
            # Return the found matches and stop searching to the right
            result.append(array[mid])
            return result
        if target < element:
            end = mid - 1
        else:
            start = mid + 1

    return result

def binary_search_endswith(array, start, end, target, key):
    result = []

    while start <= end:
        mid = start + (end - start) // 2
        element = str(key(array[mid]))

        if element.endswith(target):
            # Continue searching to the right for more matches
            right_idx = mid + 1
            while right_idx <= end and key(array[right_idx]).endswith(target):
                result.append(array[right_idx])
                right_idx += 1
            # Return the found matches and stop searching to the left
            result.append(array[mid])
            return result
        if target < element:
            end = mid - 1
        else:
            start = mid + 1

    return result


def binary_search(array, start, end, target, filter, key):
    if filter == "--Select filter--":
        return binary_search_equals(array, start, end, target, filter, key)
    if filter == "Contains":
        return binary_search_contains(array, start, end, target, filter, key)
    elif filter == "Starts With":
        return binary_search_startswith(array, start, end, target, filter, key)
    elif filter == "Ends With":
        return binary_search_endswith(array, start, end, target, filter, key)
    



##########################################################################
def jump_search_equals(array, start, end, target, key):
    results = []
    step = int(sqrt(end - start + 1))

    # Find the block containing the target
    i = start
    while i <= end:
        if str(key(array[i])) == target:
            results.append(array[i])  # Add matching element to results list
            i += 1
        elif str(key(array[i])) > target:
            break
        else:
            i += step

    # Perform a linear search within the block
    for j in range(max(i - step, start), i):
        if j >= start and j <= end and str(key(array[j])) == target:
            results.append(array[j])  # Add matching element to results list

    return results



def jump_search_contains(array, start, end, target, key):
    results = []
    step = int(sqrt(end - start + 1))
    # Find the block containing the target
    for i in range(start, end, step):
        if target in str(key(array[i])):
            results.append(array[i])  # Add matching element to results list

    return results

def jump_search_startswith(array, start, end, target, key):
    results = []
    step = int(sqrt(end - start + 1))
    # Find the block containing the target
    for i in range(start, end, step):
        if str(key(array[i])).startswith(target):
            results.append(array[i])  # Add matching element to results list

    return results

def jump_search_endswith(array, start, end, target, key):
    results = []
    step = int(sqrt(end - start + 1))
    # Find the block containing the target
    for i in range(start, end, step):
        if str(key(array[i])).endswith(target):
            results.append(array[i])  # Add matching element to results list

    return results

def jump_search(array, start, end, target, filter, key):
    if filter == "--Select filter--":
        return jump_search_equals(array, start, end, target, key)
    if filter == "Contains":
        return jump_search_contains(array, start, end, target, key)
    elif filter == "Starts With":
        return jump_search_startswith(array, start, end, target, key)
    elif filter == "Ends With":
        return jump_search_endswith(array, start, end, target, key)