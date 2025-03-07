def countValidTriangles(sides):
    """
    Count the number of valid triangles that can be formed with an array of side lengths.

    Args:
        sides (list of int): Array of side lengths.

    Returns:
        int: Number of valid triangles.

    Time Complexity: O(n^2), where n is the size of the array.
      - Sorting the array takes O(n log n).
      - The two-pointer approach takes O(n^2).
    """
    n = len(sides)
    if n < 3:
        return 0

    sides.sort()  # O(n log n)

    count = 0

    for i in range(n - 1, 1, -1):  # O(n)
        left = 0
        right = i - 1
        while left < right:  # O(n)
            # Check the triangle inequality
            if sides[left] + sides[right] > sides[i]:
                # All elements between left and right also form valid triangles
                count += right - left
                right -= 1
            else:
                left += 1

    return count

