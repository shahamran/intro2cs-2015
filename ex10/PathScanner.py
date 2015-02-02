import os
from WordExtractor import *
from WordTracker import *

class PathIterator:
    """
    An iterator which iterates over all the directories and files
    in a given path (note - in the path only, not in the
    full depth). There is no importance to the order of iteration.
    """
    def __init__(self, path):
        self.items = os.listdir(path)
        self.index = 0
        self.path = path
        self.SEPERATOR = '/'

    def __iter__(self):
        return self

    def __next__(self):
        '''
        Goes over the items list, as given by the os.listdir() function one
        item at a time.
        returns the path of a file/dir in the directory as string
        '''
        if self.index >= len(self.items): raise StopIteration()
        item = self.items[self.index]
        self.index += 1
        return self.path + self.SEPERATOR + item
        


def path_iterator(path):
    """
    Returns an iterator to the current path's filed and directories.
    Note - the iterator class is not outlined in the original
     version of this file - but rather is should be designed
     and implemented by you.
    :param path: A (relative or an absolute) path to a directory.
    It can be assumed that the path is valid and that indeed it
    leads to a directory (and not to a file).
    :return: An iterator which returns all the files and directories
    in the *current* path (but not in the *full depth* of the path).
    """
    return PathIterator(path)

def print_tree(path, sep='  '):
    """
    Print the full hierarchical tree of the given path.
    Recursively print the full depth of the given path such that
    only the files and directory names should be printed (and not
    their full path), each in its own line preceded by a number
    of separators (indicated by the sep parameter) that correlates
    to the hierarchical depth relative to the given path parameter.
    :param path: A (relative or an absolute) path to a directory.
    It can be assumed that the path is valid and that indeed it
    leads to a directory (and not to a file).
    :param sep: A string separator which indicates the depth of
     current hierarchy.
    """

    def recursive_tree(path, sep, depth):
        '''
        The recursive function that goes over the path.
        Gets a path of a DIRECTORY, prints every file in it and recursively
        enters directories in it.
        :param path: A relative or an absolute path to a directory.
        :type path: string
        :param sep: a string which indicates the depth of current hierarchy.
        :type sep: string
        :param depth: The current directory depth (distance from input folder)
        :type depth: int
        '''
        # an index for the 'absolute' name of file (or dir) inside 'path'
        path_index = len(path) + 1
        items = path_iterator(path)
        for item in items:
            print(sep * depth + item[path_index:])
            if os.path.isdir(item):
                recursive_tree(item, sep, depth + 1)
    # starts printing with 0 depth.
    recursive_tree(path,sep,0)
        
        
    
    


def file_with_all_words(path, word_list):
    """
    Find a file in the full depth of the given path which contains
    all the words in word_list.
    Recursively go over  the files in the full depth of the given
    path. For each, check whether it contains all the words in
     word_list and if so return it.
    :param path: A (relative or an absolute) path to a directory.
    In the full path of this directory the search should take place.
    It can be assumed that the path is valid and that indeed it
    leads to a directory (and not to a file).
    :param word_list: A list of words (of strings). The search is for
    a file which contains this list of words.
    :return: The path to a single file which contains all the
    words in word_list if such exists, and None otherwise.
    If there exists more than one file which contains all the
    words in word_list in the full depth of the given path, just one
    of theses should be returned (does not matter which).
    """

    def recursive_search(path, word_tracker):
        '''
        Recursive search for the file containing all of the words in
        the input word_list, using the class WordTracker.
        :param path: Relative or absolute path of a directory. a string.
        :param word_tracker: a WordTracker object that holds the word list
        that we are looking for in the file system.
        '''
        items = path_iterator(path)

        for item in items:
            if os.path.isfile(item):

                try: # to avoid file system errors
                    words = WordExtractor(item)
                    for word in words: # checks every word in the file
                        word_tracker.encounter(word)
                    if word_tracker.encountered_all():
                        return item # if desired file was found stop searching
                    else:
                        word_tracker.reset()
                except: # will be reached if the file wasn't meant to be read.
                        # if so, resets the tracker and continues the search.
                    word_tracker.reset()

            elif os.path.isdir(item): # recursive search in directories
                recursive_search(item, word_tracker)

        return None # reached if no file was found.
    # let the search begin.
    word_tracker = WordTracker(word_list)
    return recursive_search(path, word_tracker)   

