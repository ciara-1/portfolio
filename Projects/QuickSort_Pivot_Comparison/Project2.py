import random
import time



# Quick Sort with first item as pivot
def quick_sort_with_first_pivot(dataset, first, last):
    #TODO: Fill here
    if first < last:
        # Partition the dataset and get the pivot index
        pivot_idx = partition_first_pivot(dataset, first, last)
        # Recursively sort the two halves
        quick_sort_with_first_pivot(dataset, first, pivot_idx -1)
        quick_sort_with_first_pivot(dataset, pivot_idx +1, last)

def partition_first_pivot(dataset, first, last):
    # Choose the first element as the pivot
    pivot_value = dataset[first]
    lower_idx = first +1
    upper_idx = last

    done = False
    while not done:
        # Move left index to the right if less than the pivot
        while lower_idx <= upper_idx and dataset[lower_idx] <= pivot_value:
            lower_idx += 1
        # Move right index to the left if greater than the pivot
        while lower_idx <= upper_idx and dataset[upper_idx] >= pivot_value:
            upper_idx -= 1

        # Swap lower index and upper index is they haven't crossed
        if lower_idx > upper_idx:
            done = True
        else:
            dataset[lower_idx], dataset[upper_idx] = dataset[upper_idx], dataset[lower_idx]

    # Swap the pivot with the upper index to place the pivot in the correct position
    dataset[first], dataset[upper_idx] = dataset[upper_idx], dataset[first]

    return upper_idx # Return the index of the pivot

# Quick Sort with random pivot
def quick_sort_with_random_pivot(dataset, first, last):
    #TODO: Fill here
    if first < last:
        # Partition the dataset and get the pivot index using a random pivot
        pivot_idx = partition_random_pivot(dataset, first, last)
        # Recursively sort the two halves
        quick_sort_with_random_pivot(dataset, first, pivot_idx -1)
        quick_sort_with_random_pivot(dataset, pivot_idx +1, last)

def partition_random_pivot(dataset, first, last):
    # Choose a random pivot index and swap with first element
    pivot_idx = random.randint(first, last)
    dataset[first], dataset[pivot_idx] = dataset[pivot_idx], dataset[first]

    pivot_value = dataset[first]
    lower_idx = first +1
    upper_idx = last

    done = False
    while not done:
        # Move left index to the right if less than the pivot
        while lower_idx <= upper_idx and dataset[lower_idx] <= pivot_value:
            lower_idx += 1
        # Move right index to the left if greater than the pivot
        while lower_idx <= upper_idx and dataset[upper_idx] >= pivot_value:
            upper_idx -= 1

        # Swap lower index and upper index is they haven't crossed
        if lower_idx > upper_idx:
            done = True
        else:
            dataset[lower_idx], dataset[upper_idx] = dataset[upper_idx], dataset[lower_idx]

    # Swap the pivot with the upper index to place the pivot in the correct position
    dataset[first], dataset[upper_idx] = dataset[upper_idx], dataset[first]
    
    return upper_idx # Return the index of the pivot

# Function to generate different types of arrays
def generate_array(type, size):
    if type == "random":
        return [random.randint(1, 100) for _ in range(size)]
    elif type == "sorted":
        return [i for i in range(size)]
    elif type == "reversed":
        return [i for i in range(size, 0, -1)]
    elif type == "identical":
        return [size for _ in range(size)]

# Function to calculate the running time
def calculate_running_time(array_type, size, random_pivot):

    array = generate_array(array_type, size)
    start_time = time.time()
    if random_pivot:
        quick_sort_with_random_pivot(array.copy(), 0, len(array) - 1)
    else:
        quick_sort_with_first_pivot(array.copy(), 0, len(array) - 1)
    end_time = time.time()    
   
    return end_time - start_time

if __name__ == "__main__":

    # Test and print running times
    array_types = ["random", "sorted", "reversed", "identical"]
    array_size = 950  # You can adjust the size for testing
    

    # Random item as pivot
    print("Random item as pivot")
    for array_type in array_types:
        time_taken = calculate_running_time(array_type, array_size, True)
        print(f"Running time for {array_type} array of size {array_size}: {time_taken:.6f} seconds")

    # First item as pivot
    print("First item as pivot")
    for array_type in array_types:
        time_taken = calculate_running_time(array_type, array_size, False)
        print(f"Running time for {array_type} array of size {array_size}: {time_taken:.6f} seconds")