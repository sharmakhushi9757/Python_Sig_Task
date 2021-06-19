print("abhinit tiwari 1900300100003")



def longest_word(list):
    word_length = []
    for n in list:
        word_length.append((len(n), n))
    word_length.sort()
    return word_length[-1][1]

print(longest_word(["Ram", "Shyam", "Prabhas", "Parash"]))
