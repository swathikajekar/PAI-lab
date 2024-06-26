def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Helper function to print the array
def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Given array is")
    print_list(arr)
    insertion_sort(arr)
    print("Sorted array is")
    print_list(arr)
