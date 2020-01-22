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
import time

f = open('words.txt', 'r')
word_list = f.read().split("\n")
f.close()

word_set = set([word.lower() for word in word_list])

# def get_neighbors(word_set, target):
#     neighbors = []
#     for index in range(len(target)):
#         start = target[:index]
#         end = target[index+1:]
#         neighbor = [word for word in word_set if word.startswith(start) and word.endswith(end)]
#         neighbors.extend(neighbor)
#     return neighbors


def get_neighbors(word):
    neighbors = []
    for i in range(len(word)):
        for letter in list('abcdefghijklmnopqrstuvwxyz'):
            temp_word = list(word)
            temp_word[i] = letter
            new_word = "".join(temp_word)
            if new_word != word and new_word in word_set:
                neighbors.append(new_word)
    return neighbors

def bfs(begin_word, end_word):
    if len(begin_word) != len(end_word):
        raise Exception("Length of words do not match")

    # words = set([word.lower() for word in word_list if len(word) == len(end_word)])
    # Create an empty queue and enqueue A PATH TO starting vertext ID
    queue = Queue()
    queue.enqueue([begin_word])
    # Create an empty Set to store visited vertices
    visited = set()
    # While the que is not empty..
    while queue.size() > 0:
        # Deqeue the first PATH
        path = queue.dequeue()
        vertex = path[-1]
        # Grab last vertex from the PATH
        # If that vertex hasn't been visited..
        if vertex not in visited:
            if vertex == end_word:
                return path
            # Mark it as visited
            # print(vertex)
            visited.add(vertex)
            # Then add A PATH to its neighbors to the back of the queue
            for neighbor in get_neighbors(vertex):
                # COPY THE PATH
                new_path = path.copy()
                # APPEND THE NEIGHBOR TO THE BACK
                new_path.append(neighbor)
                queue.enqueue(new_path)
    return "There is no such transformation sequence"


start_time = time.time()
begin_word = "achen"
end_word = "sabik"
print(bfs(begin_word, end_word))
print(f"Time: {time.time() - start_time: .3f} sec")
