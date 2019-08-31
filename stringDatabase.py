import random

words_File = open("four_letters.txt", "r")
new_list = []
for w in words_File.readlines():  # print each line by using for loop
    p_list = w.split(" ")  # split each line using space to get all words
    new_list.extend(p_list)  # add the list of words from each line to main list
new_list.remove("\n")  # remove \n from the list
for s in new_list:  # for each word in the main list
    if s[4:] == "\n":
        index = new_list.index(s)
        s = s[0:4]
        new_list[index] = s
    if s[0:2] == "\n":
        index1 = new_list.index(s)
        s = s[2:]
        new_list[index1] = s
words_File.close()

class stringDatabase:

    """
    Class stringDatabase is to perform all disk I/O operations.
    It reads the text file with all the words, stores it in a list named new_list.
    And enables the random selection of the words.
    """
    def __init__(self, list_n):
        """
        It enables the random selection/choice of the words from list 'new_list'.

        """
        word_random = random.SystemRandom()
        word_chosen = word_random.choice(list_n)
        self.word_chosen = word_chosen

