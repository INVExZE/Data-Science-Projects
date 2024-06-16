'''                 Word Frequency Counter
Topics Covered: String Manipulation, Dictionaries, File Handling
Description: Read a text file and count the frequency of each word. Output the results in
descending order of frequency.'''

def word_frequency(file):
    word_freq = {}
    with open(file, "r") as f:
        # print(f.read())
        for line in f:
            sentence = line.replace("."," ").split()
            for word in sentence:
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
    return word_freq
                

filename = "Word.txt"
output = word_frequency(filename)

for key, val in output.items():
    print(f"{key} : {val}")