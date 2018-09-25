
def isEmpty(matrix):
    if matrix == []:
        return True
    return False

# [] is a vector
# [1,2,3] is a vector
# 3 is not a vector
# [[1,2]] is not a vector
# [[1,2],[2,3]] is not a vector
def isVector(matrix):
    if not isinstance(matrix,list):
        return False
    for i in range(len(matrix)):
        if isinstance(matrix[i],list):
            return False
    return True

def isMatrix(matrix):
    # if a single item --> Not Matrix
    if not isinstance(matrix,list):
        return False
    # if vector --> Matrix
    if isVector(matrix):
        return True
    # if different lengths --> not Matrix
    if isinstance(matrix[0],list):
        rowLength = len(matrix[0])
    else:
        return False
    for i in range(len(matrix)):
        if ((not isinstance(matrix[i],list)) or (len(matrix[i])!= rowLength)):
            return False
    return True

# Vector Operations
def zeroVector(size):
    if size <0:
        return 'Error (zeroVector): invalid size'
    vector = []
    for i in range(size):
        vector = vector + [0]
    return vector

# zeroMatrix
def zeroMatrix(rows, columns):
    if rows < 0 or columns < 0:
        return 'Error (zeroMatrix): invalid size'
    if rows == 1:
        return zeroVector(columns)
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row = row + [0]
        matrix = matrix + [row]
    return matrix

# get number of rows
def getRowSize(matrix):
    if not isMatrix(matrix):
        return 'Error (getRowSize): input not a matrix'
    if isEmpty(matrix):
        return 0
    if isVector(matrix):
        return 1
    return len(matrix)

# get number of columns
def getColumnSize(matrix):
    if not isMatrix(matrix):
        return 'Error (getColumnSize): input not a matrix'
    if isEmpty(matrix):
        return 0
    if isVector(matrix):
        return len(matrix)
    return len(matrix[0])

def getSize(matrix):
    if not isMatrix(matrix):
        return 'Error (getSize): input is not a matrix'
    return getRowSize(matrix), getColumnSize(matrix)

def printMatrix(matrix):
    if isVector(matrix):
        print(matrix)
    elif isMatrix(matrix):
        for i in range(len(matrix)):
            print(matrix[i])
    else:
            print('Error (printMatrix): not a matrix')
 
def subtract(m1,m2):

    if not isMatrix(m1) or not isMatrix(m2):
        return 'Error (add): invalid matrix input'
    for i in range(len(m1)):
        if isVector(m1) and isVector(m2):
            m1[i]-m2[i]
    if (getSize(m1) != getSize(m2)):
        return 'Error (add): invalid matrix input'
    if isVector(m1):
        for i in range(len(m1)):
            m1[i] -= m2[i]
    else:
        for i in range (getRowSize(m2)):
            for j in range (getColumnSize(m2)):
                m1[i][j]-= m2[i][j]
    return m1
    
def isSymmetric(matrix):
    count = len(matrix)
    if not matrix:
        return True
    if count != len(matrix[0]):
        return False
    for i in range(count):
        for j in range (count):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

        
def isEqualSize(m1,m2):
    if getSize(m1) != getSize(m2):
        return False
    return True 
    print('Error (printMatrix): not a matrix')

 #First I call the funtion isMetrix with both values  to check if is a matrix
 #call the funtion get size to compare if we can add
 #Call the funtion isVector and create a for loop to add the first value with the second
 #if is n ot a vector add from the 2dimentional list
def vAdd(m1,m2):
    if not isMatrix(m1) or not isMatrix(m2):
        return 'Error: invalid Vector input'
    if (getSize(m1)!=getSize(m2)):
        return 'Error: vector size mismatch'
    if isVector(m1):
        for i in range(len(m1)):
            m1[i] += m2[i]
    else:
        for i in range (getRowSize(m2)):
            for j in range (getColumnSize(m2)):
                m1[i][j]+= m2[i][j]
    return m1
#first look to see if we have an empty input
#look into the funtion isMatrixan if is not a matrix return false
#if the matrix is zero return true, otherwise return false
def isZeroMatrix(m):
    if isEmpty(m) :
        return False
    if not isMatrix(m):
        return False
    rows,columns=getSize(m)
    zero=zeroMatrix(rows,columns)
    if (m==zero):
        return True
    else:
        return False

#take the rows and columns from the funtion getSize and compare with the elements promtp for the user
#if has less colimns or rows than the index input return an error
#return the element in the index given for the user
def getElement(matrix,i,j):
   
    if isEmpty(matrix) :
        return 'Error: invalid matrix input'
    if not isMatrix(matrix):
        return 'Error: invalid matrix input'
    rows,columns=getSize(matrix)
    if (columns<j or j<0):
        return 'Error: illegal columns number'
    if (rows <i or i<0):
        return 'Error: illegal row number'
    if rows==1:
        return matrix[j]
    
    return (matrix[i][j])


#m is the colums and n is the rows, start is the first number of the list and is going to increase the time of steps
def numMatrix(m,n,start,step):
    
    if m <= 0 or n <= 0:
        return 'Error (zeroMatrix): invalid size'
    matrix = []
    for i in range(m):
        m = []
        for j in range(n):
            m = m + [start]
            start = start+step
        matrix = matrix + [m]
        
    return matrix
#Makes the first number and the last one of the list x and y
def setCorners(matrix,x,y):
    if isEmpty(matrix) :
        return 'Error: imput is an empty matrix'
    if not isMatrix(matrix):
        return 'Error: is not a matrix'
    rows,columns=getSize(matrix)
    matrix[rows-1][columns-1]=y
    matrix[0][0]=x
    print (matrix)
    
    
