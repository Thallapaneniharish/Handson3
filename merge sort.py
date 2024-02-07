def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the two halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy the remaining elements of left_half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy the remaining elements of right_half, if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Test the Merge Sort implementation
arr_to_sort = [5, 2, 4, 7, 1, 3, 2, 6]
print("Original array:", arr_to_sort)

merge_sort(arr_to_sort)
print("Sorted array:", arr_to_sort)


Original array: [5, 2, 4, 7, 1, 3, 2, 6]
Sorted array: [1, 2, 2, 3, 4, 5, 6, 7]
