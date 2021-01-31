def longestUniqueSubstring(input: str) -> str:

    # a travel map of char in our input and its last found index
    visited = dict()

    output = ""

    start = 0
    for end in range(0, len(input)):
        currentChar = input[end]
        if visited.get(currentChar) is not None:
            start = max(visited[currentChar] + 1, start)

        # update the output string if it is smaller in lenght than (end - start) + 1 for zero based indexing
        if len(output) < (end - start + 1):
            output = input[start : end + 1]

        # add char and its last found index to our visited map
        visited[currentChar] = end
    return output


if __name__ == "__main__":
    input = "AABCDEF"
    print(longestUniqueSubstring(input))
