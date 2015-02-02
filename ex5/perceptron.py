##################################################################
# FILE : perceptron.py
# WRITER : Ran Shaham , ransha , 203781000
# EXERCISE : intro2cs ex5
# DESCRIPTION:
# This is file contains functions that apply the perceptron
# algorithm to desired data and returns it's results.
# Also, there are many functions for internal use for mathematical
# operations such as vector addition, dot product etc...
##################################################################

def dot(A, B):
    '''Gets two lists of the same size (vectors A and B)
       and returns their dot product'''
    total= 0
    length= range(len(A))
    for index in length: 
        total+= A[index] * B[index]
    return total

def vector_add(A, B):
    '''Gets two lists of the same size (vectors A,B)
       and returns one list(=vector A + B) (vector addition)'''
    result= []
    length= range(len(A))
    for i in length: # 'i' stands for index
        result.append(A[i] + B[i])
    return result

def multi_scalar(a,V):
    '''Gets a number(=scalar) [a] (int or float) and a list [V] (vector)
      and returns a list (vector) of the result of multiplication by scalar'''
    result= []
    length= range(len(V))
    for i in length: # 'i' stands for index
        result.append(a * V[i])
    return result

def sign(number):
    '''Gets a number and returns '1' if its positive,
       '-1' if it's negative and '0' if it's exactly 0'''
    if number > 0:
        return 1
    elif number < 0:
        return -1
    elif number == 0:
        return 0

def perceptron(data, labels):
    ''' Gets data list (list of vectors) and labels list (of the same
        size) and returns the linear classifier if it exists for the
        given data. If it doesn't returns (None,None)'''
    w_changed= 0 # counts how many times the weight vector was changed
    found= False
    first_run= True
    m= len(data) # the size of the list of vectors
    w= []     
    b= 0
    MAX_ERRORS = m * 10 # maximal number of errors (changes) allowed
                        # until we decide there's no classifier
    for j in range(len(data[0])): # sets the initial weight vector to be 0v
        w.append(0)
    # this is the main loop that finds a linear classifier
    while not found:
        found= True
        for i in range(m): # i is index in the list of vectors
            # this condition checks if our weight vector is OK. if not, we
            # update it. <=> makes the classifier.
            if sign( dot(w, data[i]) - b ) != labels[i]: 
                found= False
                w= vector_add( multi_scalar(labels[i], data[i]), w )
                b-= labels[i]
                # we count the number of changes only after the first run
                if not first_run: w_changed+= 1
                if w_changed > MAX_ERRORS: # if the max number of allowed
                                           # attempts, we stop and return None
                    found= True
                    return (None,None)
        if first_run:
            first_run= False   
        else:
            if found: return (w,b)

def generalization_error(data, labels, w, b):
    '''Gets a list of vectors [data], a labels vector [labels] and
       possible weight vector [w] and bias value [b] and determines
       whether our classifier (w,b) succeeded in classifying the
       given data. returns a list in the size of the [data] list that
       contains 0 for the indexes in which the classifier worked
       and 1 for the indexes it didn't '''
    m= len(data)
    result= []
    OK= 0
    ERROR= 1
    for index in range(m):
        if sign(dot(w, data[index]) - b) == labels[index]:
            result.append(OK)
        else:
            result.append(ERROR)
    return result

def vector_to_matrix(vec):
    '''Gets a list (vector) in the size x ^ 2 [vec] and returns a matrix
     (list of lists) in the size x * x ( |matrix[x]| == x ) '''
    matrix= [] # starts with an empty list
    row= 0        # an index for the row number in the matrix
    vec_size= int( len(vec) ** (1/2) ) # the length of each row in the matrix
    for i in range(len(vec)):
        if i % (vec_size * (row + 1)) == 0: # checks if a new row is needed
            if row != 0 or i != 0: row += 1
            matrix.append([])
        #copies the data from the vector to the correct place in the matrix
        matrix[row].append(vec[i])
    return matrix

def classifier_4_7(data, labels):
    '''Gets a list of vectors [data] and labels list [labels]. Each vector in
       the data list is a number, each number in the labels list is '1' if
       the number is 4 and '-1' if it's 7. returns the classifier of the
       perceptron algorithm that seperates the 4's from the 7's (w,b) '''
    (w,b)= perceptron(data,labels)
    # NOTE that if no classifier was found, the perceptron function will
    # return the (None,None) tuple.
    return (w,b)

def test_4_7(train_data, train_labels, test_data, test_labels):
    '''Gets training data and labels to find a classifier, and checks
       the classifier for a chosen test data and labels. If no classifier
       was found in the training data, it returns (None,None,None). If one
       was found it returns it and a list of errors in classification in the
       test data = (w, b, errors) '''
    (train_w,train_b)= classifier_4_7(train_data,train_labels)
    if train_w== None: return (None,None,None)
    errors= generalization_error(test_data, test_labels, train_w, train_b)
    return(train_w, train_b, errors)
