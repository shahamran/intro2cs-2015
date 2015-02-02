#!/usr/bin/env python3


class WordExtractor(object):
    """
    This class should be used to iterate over words contained in files.
     The class should maintain space complexity of O(1); i.e, regardless
     of the size of the iterated file, the memory requirements ofa class
     instance should be bounded by some constant.
     To comply with the space requirement, the implementation may assume
     that all words and lines in the iterated file are bounded by some
     constant, so it is allowed to read words or lines from the
     iterated file (but not all of them at once).
    """

    def __init__(self, filename):
        """
        Initiate a new WordExtractor instance whose *source file* is
        indicated by filename.
        :param filename: A string representing the path to the instance's
        *source file*
        """

        self.NEW_LINE = '\n'
        self.file = open(filename)
        self.line = self.file.readline() # the line string
        self.splitted = self.line.split() # list of words in the line
        self.curr_index = 0
        self.end_of_file = False
        

    def __iter__(self):
        """
        Returns an iterator which iterates over the words in the
        *source file* (i.e - self)
        :return: An iterator which iterates over the words in the
        *source file*
        """

        return self

    def _next_line(self):
        '''
        Reads next line in the file and saves it to the class.
        '''
        self.line = self.file.readline()
        self.splitted = self.line.split()
        self.curr_index = 0
    
    def _bad_line(self,line):
        '''
        Checks if a certain line contains no readable words (string).
        :param line: a string that represents a line in the file.
        :return: >True if the line is empty or if the end of line is reached
                 >False if the line is good or it is the end of file.
        '''
      
        self.end_of_file = len(line) == 0
        empty_line = len(self.splitted) == 0
        end_of_line = self.curr_index >= len(self.splitted)

        # the end of file line isn't a bad line.
        return (empty_line or end_of_line) and (not self.end_of_file)

    def __next__(self):
        """
        Make a single word iteration over the source file.
        :return: A word from the file.
        """

        while self._bad_line(self.line):
            self._next_line() # only read good lines.

        if not self.end_of_file:
            word = self.splitted[self.curr_index]
            self.curr_index += 1
            return word
        else:
            self.file.close()
            raise StopIteration()

            

