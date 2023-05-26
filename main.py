import re


def word_frequency(paragraph):
    frequency_dict = {}
    for string in paragraph:
        words = re.compile('\w+').findall(string)
        for word in words:
            word = word.lower()
            if word in frequency_dict.keys():
                frequency_dict[word] += 1
            else:
                frequency_dict[word] = 1

    return frequency_dict


if __name__ == '__main__':
    paragraph = [
        "The quick brown fox",
        "jumps over the lazy dog.",
        "The dog barks,",
        "and the fox runs away.",
        ]
    frequency = word_frequency(paragraph)
    print(frequency)
