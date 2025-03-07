def findAllPairs(arr):
    """
    Find all possible pairs of elements in a given array.

    Args:
        arr (list): The input array.

    Returns:
        list: A list of tuples, where each tuple represents a pair of elements.

    Time Complexity: O(n^2), where n is the size of the array.
      - Explanation: The nested loops iterate over all possible pairs, resulting in O(n^2) operations.
    """
    pairs = []  # Initialize an empty list to store pairs
    n = len(arr)  # Get the length of the array

    # Outer loop: Iterate over each element in the array
    for i in range(n):  # O(n)
        # Inner loop: Iterate over the remaining elements to form pairs
        for j in range(i + 1, n):  # O(n)
            pairs.append((arr[i], arr[j]))  # O(1): Append the pair as a tuple

    return pairs

