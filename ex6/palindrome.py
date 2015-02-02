def is_palindrome_1(s):
    '''Gets a string [s] and returns True if it is a palindrome
    and False otherwise. '''
    length = len(s)
    if length == 0: return True #an empty string is a palindrome.
    #checks if the edges of the string are identical. if so, checks the sub
    #string that includes only the chars we didn't check.
    if s[0] == s[-1]:
        if length <= 2:
            return True #no more to check
        return is_palindrome_1(s[1:length-1])
    #if one of the edges set wasn't identical, it's not a palindrome.
    return False


def is_palindrome_2(s, i, j):
    '''Gets a string [s] and two indexes [i] and [j] and checks if a substring
    between those two indexes (including) is a palindrome.
    return True or False '''
    if len(s) == 0: return True
    if j < i:      # we want j to be the bigger index (for readability)
        j, i = i, j
    # works the same as the is_palindrome_1 function, only for a sub string
    if s[i] == s[j]:
        if j - i <= 2:
            return True
        else:
            return is_palindrome_2(s, i + 1, j - 1)
    # if True was not returned so far, return False.
    return False
