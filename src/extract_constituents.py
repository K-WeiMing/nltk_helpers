def get_constituents(sentence: str, brackets: str = "()") -> list:
    """
    Uses a sliding window to extract the constituents of a sentence in treebank format.
    """
    constituency = []
    sentence_len = len(sentence)

    for i in range(sentence_len):
        # If match the first bracket, move onto the next char
        if sentence[i] == brackets[0]:

            for j in range(i + 1, sentence_len):
                # Check for start of the string if it matches another open bracket
                if sentence[j] == brackets[0]:
                    # Append the constituent to the list
                    constituency.append(sentence[i + 1 : j - 1])  # Remove extra space
                    break

                if sentence[j] == brackets[1]:
                    break
    return constituency
