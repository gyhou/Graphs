"""
Given two words (begin_word and end_word), and a dictionary's word list, 
return the shortest transformation sequence from begin_word to end_word, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
Note:

Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.

Sample:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']

begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

beginWord = "hungry"
endWord = "happy"
None
"""
from util import Queue
from graph import Graph

f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()


def shortest_transformation(begin_word, end_word):
    if len(begin_word) != len(end_word):
        return # "There is no such transformation sequence"
    
    word = set([word.lower() for word in words if len(word) == len(end_word)])

    graph = Graph()  # Instantiate your graph
    return len(word)


if __name__ == '__main__':

    print(shortest_transformation("hit", "cog"))
