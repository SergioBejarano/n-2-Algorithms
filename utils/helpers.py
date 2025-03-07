import time
import random

def measure_time(algorithm, *args):
    """
    Measure the execution time of an algorithm.

    Args:
        algorithm (function): The algorithm to measure.
        *args: Arguments to pass to the algorithm.

    Returns:
        float: Execution time in seconds.
    """
    start_time = time.time()
    algorithm(*args)
    return time.time() - start_time


def generate_large_string(size):
    """
    Generate a large string of random lowercase letters.

    Args:
        size (int): Length of the string.

    Returns:
        str: A random string.
    """
    return ''.join(random.choice('abcdefghiaaaaaaajklmnaaaaopqaaarstaaauvwaaaaaxyz') for _ in range(size))


def generate_large_array(size):
    """
    Generate a large array of random integers.

    Args:
        size (int): Size of the array.

    Returns:
        list: A list of random integers.
    """
    return [random.randint(1, 1000) for _ in range(size)]