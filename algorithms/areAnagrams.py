def areAnagrams(string1, string2):
    """
    Check if two strings are anagrams of each other.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.

    Time Complexity: O(n^2), where n is the length of the strings.
      - Explanation: For each character in string1 (n iterations), we perform a linear search in string2 (n iterations),
                     resulting in O(n^2) in the worst case.
    """
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    if len(string1) != len(string2):
        return False

    string2_list = list(string2)

    for char in string1:
        found = False
        for i in range(len(string2_list)):
            if string2_list[i] == char:
                found = True
                string2_list[i] = None
                i = len(string2_list)
        if not found:
            return False

    return True