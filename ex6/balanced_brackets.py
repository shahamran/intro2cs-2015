#Constants for the brackets strings
OPEN_STR = "("
CLOSED_STR = ")"


def is_balanced(s):
    '''Gets a string varibale [s] and checks if it contains
    balanced brackets. return True if so, and False otherwise. '''
    length = len(s)
    opened = 0
    #checks every character in the string. If it's a closed bracket and
    #there were no open ones, it returns False
    for i in range(length):
        if s[i] == OPEN_STR:
            opened += 1
        elif s[i] == CLOSED_STR:
            opened -= 1
        if opened < 0:
            return False
    #If after checking every char the number of opened brackets isn't
    #the same as the closed ones, it returns False.
    if opened == 0:
        return True
    else:
        return False


def violated_balanced(s):
    '''Gets a string variable [s] and checks if it is balanced. If not it
    returns the index of the char which breaks the balance. If the balance
    can be restored by adding closed brackets, it returns the string's
    length. If the string is balanced, returns '-1' '''
    #first checks if the string is balanced
    if is_balanced(s):
        return -1
    #The recursive funciton. gets an unbalanced string and an index and
    #checks every sub-string (from the start to the index) to find the last
    #index in which it was balanced and if it can be rebalanced
    def check_index(s, index):
        #if the index is greater than the length of the string, the string
        #can be balanced and the function returns the length of the string
        if index >= len(s):
            return len(s)
        #if the sub-string is balanced, check the next one.
        if is_balanced(s[:index + 1]):
            return check_index(s, index + 1)
        else:
            #if the string isn't balanced, checks if there is any number
            #of closed brackets that can be added in order to balance it
            #if not, then a closed bracket broke our balance and the function
            #returns it's index.
            for i in range(1, index + 2):
                if is_balanced(s[:index + 1] + (CLOSED_STR * i)):
                    return check_index(s, index + 1)
            return index
    #calls the recursive function with the index '0', to start the search.
    return check_index(s, 0)


def match_brackets(s):
    '''Gets a string variable [s] and returns a list in the size of the string
    that specify the location of a bracket set by a set of numbers which
    indicate the distance from the index in the list to the matching bracket.
    if the string is unbalanced, returns [] '''

    def get_list(s, index, result=[0] * len(s)):
        '''the recursive function. assuming it's initial input string is balanced,
        checks every char to find an open bracket. when found, goes over every
        next substring to check where its matching closer is found. then sets
        the list in those indexes to the correct values according to this info.
        NOTE: Gets a non-empty string '''
        if s[index] == OPEN_STR:
            #uses another function to check where the matching bracket is
            j = violated_balanced(s[index + 1:])
            result[index] = j + 1
            result[index + j + 1] -= j + 1
        #stops when it reaches the end of the string (index > len(s))
        if index < len(s) - 1:
            result = get_list(s, index + 1, result)               
        return result

    out_list = [] # initial output list is empty    
    if is_balanced(s) and len(s) != 0:
        out_list = get_list(s, 0) # calls the recursive function
    return out_list
