import matplotlib.pyplot as plt
import pandas as pd
from algorithms.areAnagrams import areAnagrams
from algorithms.countValidTriangles import countValidTriangles
from algorithms.findAllPairs import findAllPairs

from utils.helpers import measure_time, generate_large_string, generate_large_array

def main():
    input_sizes = [200*i for i in range(1,21)]

    anagram_times = []
    triangle_times = []
    pairs_times = []

    for size in input_sizes:
        string1 = generate_large_string(size)
        string2 = generate_large_string(size)
        sides = generate_large_array(size)
        arr = generate_large_array(size)

        anagram_time = measure_time(areAnagrams, string1, string2)
        anagram_times.append(anagram_time)

        triangle_time = measure_time(countValidTriangles, sides)
        triangle_times.append(triangle_time)

        pairs_time = measure_time(findAllPairs, arr)
        pairs_times.append(pairs_time)

        print("Computing "+str(size))
    data = {
        "Input Size": input_sizes,
        "Anagram Time (s)": anagram_times,
        "Triangle Time (s)": triangle_times,
        "Pairs Time (s)": pairs_times,
    }
    df = pd.DataFrame(data)

    print(df)

    plt.figure(figsize=(10, 6))
    plt.plot(df["Input Size"], df["Anagram Time (s)"], label="Are Anagrams", marker="o")
    plt.plot(df["Input Size"], df["Triangle Time (s)"], label="Count Valid Triangles", marker="s")
    plt.plot(df["Input Size"], df["Pairs Time (s)"], label="Find All Pairs", marker="^")

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (s)")
    plt.title("Algorithm Execution Times")
    plt.legend()
    plt.grid(True)
    plt.show(block=True)

if __name__ == "__main__":
    main()
