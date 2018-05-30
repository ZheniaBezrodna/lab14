import random
import time

from linkedbst import LinkedBST


class Words:
    def __init__(self):
        self.tree = LinkedBST()
        self.words_list = None

    def read_file(self):
        #  This function reads the file with words.
        with open('words.txt', "r") as file:
            self.words_list = file.readlines(100000)
            for i in random.sample(self.words_list, len(self.words_list)):
                self.tree.add(i)

    def random_words(self):
        # This method selects randomly 10,000 words from the file.
        random_words1 = random.choice(self.words_list)
        for numb in range(10001):
            for items in self.words_list:
                if items == random_words1:
                    pass

    def linear_tree_time(self):
        for numb in range(10001):
            self.tree.find(self.words_list[
                               random.randint(0, len(self.words_list) - 1)])

    def tree_balanced_time(self):
        self.tree.rebalance()
        for i in range(10001):
            self.tree.find(self.words_list[
                               random.randint(0, len(self.words_list) - 1)])


if __name__ == "__main__":
    print("Please, wait a little bit...")
    word = Words()
    initial_time = time.time()
    word.random_words()
    print("linear time: {} seconds".format(time.time() - initial_time))
    initial_time = time.time()
    word.linear_tree_time()
    print("linear tree time: {} seconds".format(time.time() - initial_time))
    initial_time = time.time()
    word.tree_balanced_time()
    print("balanced time: {} seconds".format(time.time() - initial_time))
