#!/usr/bin/env python3


class WordTracker(object):
    """
    This class is used to track occurrences of words.
     The class uses a fixed list of words as its dictionary
     (note - 'dictionary' in this context is just a name and does
     not refer to the pythonic concept of dictionaries).
     The class maintains the occurrences of words in its
     dictionary as to be able to report if all dictionary's words
     were encountered.
    """

    def __init__(self, word_list):
        """
        Initiates a new WordTracker instance.
        :param word_list: The instance's dictionary.
        """
        self.dict = word_list[:]              # sets a NEW list
        self._sort_dict()                     # sorts it
        self.found = [False] * len(self.dict) # list of booleans that flags 
#        self.found_idx = 0                    # found words.

    def _sort_dict(self):
        '''
        Uses merge sort algorithm and python string comparison to sort the
        given list of words. Uses recursion.
        :return: a sorted list of words.
        '''
        def merge_sort(lst):
            '''
            the recursive sort.
            '''
            size = len(lst)
            if size <= 1:
                return lst # sorted list (contains 1 or less elements)
            middle = size // 2
            left, right = merge_sort(lst[:middle]), merge_sort(lst[middle:])
            lst = merge(left, right) # the merging
            return lst # returns a sorted list
            
        def merge(left, right):
            '''
            Merges two lists according to its' items' values.
            Gets two parameters 'left','right' as lists and merges them.
            :return: merged list.
            '''
            lst = left + right
            size = len(lst)
            l, r = 0, 0
            for i in range(size):
                l_val = left[l] if l < len(left) else None
                r_val = right[r] if r < len(right) else None
                r_bigger = l_val and r_val and l_val < r_val
                l_bigger = l_val and r_val and l_val >= r_val
                if r_bigger or r_val == None:
                    lst[i] = l_val
                    l += 1
                elif l_bigger or l_val == None:
                    lst[i] = r_val
                    r += 1
            return lst
        # calls the recursive sort.
        self.dict = merge_sort(self.dict)

    def __contains__(self, word):
        """
        Check if the input word in contained within dictionary.
         For a dictionary with n entries, this method guarantees a
         worst-case running time of O(n) by implementing a
         binary-search.
        :param word: The word to be examined if contained in the
        dictionary.
        :return: True if word is contained in the dictionary,
        False otherwise.
        """

        is_in_dict = False
        lst = self.dict
        left = 0
        right = len(lst)

        while left <= right and right <= len(lst) and left >= 0:
            middle_i = (right+left) // 2
            middle = lst[middle_i]
            if middle > word:
                if middle_i <= 0: break # to avoid infinite loop
                right = middle_i - 1
            elif middle < word:
                if middle_i >= len(lst) -1: break # same as ^
                left = middle_i + 1
            else:
                is_in_dict = True
                self.found[middle_i] = is_in_dict
                break
            # if the word isn't in the dictionary the middle_i index can
            # reach the end of the list, and that can cause infinite search.
        return is_in_dict
                

    def encounter(self, word):
        """
        A "report" that the give word was encountered.
        The implementation changes the internal state of the object as
        to "remember" this encounter.
        :param word: The encountered word.
        :return: True if the given word is contained in the dictionary,
        False otherwise.
        """ 
        return word in self # uses the __contains__ method

    def encountered_all(self):
        """
        Checks whether all the words in the dictionary were
        already "encountered".
        :return: True if for each word in the dictionary,
        the encounter function was called with this word;
        False otherwise.
        """
        for found in self.found:
            if not found: return found
        return True

    def reset(self):
        """
        Changes the internal representation of the instance such
        that it "forget" all past encounters. One implication of
        such forgetfulness is that for encountered_all function
        to return True, all the dictionaries' entries should be
        called with the encounter function (regardless of whether
        they were previously encountered ot not).
        """
        self.found = [False] * len(self.dict)
