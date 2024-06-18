def binary_search(arr, x):
    # Initialize the left and right pointers
    left, right = 0, len(arr) - 1

    while left <= right:
        # Calculate the middle index
        mid = left + (right - left) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        # If x is greater, ignore the left half
        elif arr[mid] < x:
            left = mid + 1
        # If x is smaller, ignore the right half
        else:
            right = mid - 1

    # If the element is not present in the array
    return -1

# Helper function to print the result
def print_result(index):
    if index != -1:
        print(f"Element is present at index {index}")
    else:
        print("Element is not present in array")

# Example usage
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    result = binary_search(arr, x)
    print_result(result)

    x = 5
    result = binary_search(arr, x)
    print_result(result)
