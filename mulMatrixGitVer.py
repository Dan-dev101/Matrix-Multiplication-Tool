

def createMatrix():
    """ Function Description:
            Prompts user input values for a matrix and checks for errors
        Parameter(s): 
            None
        Return: 
            matrix: is a multidimensional list / ('Matrix') 
    """
    while True:
        #Error checking and getting input form user 
        try:
            user_row = int(input("Enter the number of rows: "))
            user_cols = int(input("Enter the number of columns: "))
            break
        except ValueError:
            print("Invalid input please enter positive integers for rows and columns.")

    matrix = []
    for i in range(user_row):
        while True:
            user_input = input(f"Enter row {i + 1} as a comma separated list of {user_cols} integers: ")
            totalrows = user_input.split(',') #Split the input string by commas

            #Checking if the input does not match the number of columns
            if len(totalrows) != user_cols:
                print(f"Input does not match the number of columns which you entered {user_cols}.")
                continue

            rows = [] #List to store integers for this row
            try:
                #Each value in the row is striped and converted to an integer and appended to rows
                for j in totalrows:
                    rows.append(int(j.strip()))
                if len(totalrows) != user_cols:
                    print(f"Input does not match the number of columns which you entered {user_cols}.")
                    continue
                matrix.append(rows) #Append the row to matrix
                break
            except ValueError:
                print("Values must be integers.")
    return matrix

def multipleMatrix(matrixA, matrixB):
    """ Function Description:
            Does the actually multiplication of 2 matrices
        Parameter(s): 
            matrixA, matrixB: Two matrices that the user has choosen are passed
        Return: 
            final_matrix: is a multidimensional list as a result of multiplying the two matrices passed
    """
    row_A = len(matrixA) #Number of rows in Matrix A
    rows_B = len(matrixB) #Number of rows in Matrix B
    cols_A = len(matrixA[0]) #Number of columns in Matrix A
    cols_B = len(matrixB[0]) #Number of columns in Matrix B

    #Checking if matrices can be multiplied
    if cols_A != rows_B:
        print("Matrices cannot be multiplied.")
        return None
    
    #The result matrix with zeroes 
    final_matrix = []
    for i in range(row_A):
        row = [0] * cols_B #Creating a row with zeroes for each column in B
        final_matrix.append(row)

    #Matrix multiplication
    for i in range(row_A):
        for j in range(cols_B):
            for k in range(cols_A):  
                 final_matrix[i][j] += matrixA[i][k] * matrixB[k][j] #Dot product calculation
    
    return final_matrix

def main():
    """ Function Description:
            Runs the program and calls functions and handles users inputs.
        Parameter(s): 
            None
        Return: 
            None  
    """
    while True:
        print("\nMatrix A")
        matrix_a = createMatrix()
        print("\nMatrix B")
        matrix_b = createMatrix()

        result = multipleMatrix(matrix_a, matrix_b)

        #Checking if the multiplication was done
        if result == None:
            print("\nMatrix multiplication is not valid for the given matrices. Please reenter.")
        else:
            print("\nResult Matrix:")
            print(result)
            break

if __name__ == "__main__":
    main()