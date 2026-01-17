def insertion_sort_descending(arr):
    """
    Sorts the input list in monotonically decreasing order
    using the Insertion Sort algorithm.
    """
    for i in range(1, len(arr)):
        
        key = arr[i]

        
        j = i - 1

        # Move elements that are smaller than key
        # one position ahead to make space for key
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


if __name__ == "__main__":
    # Example usage
    numbers = [12, 11, 13, 5, 6, 7]

    print("Original array:")
    print(numbers)

    insertion_sort_descending(numbers)

    print("\nSorted array (monotonically decreasing):")
    print(numbers)
