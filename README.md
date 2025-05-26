# Matrix Multiplication Calculator

A Python program that performs matrix multiplication with user input validation and error handling.

## Features

- Interactive matrix creation with user input
- Input validation for matrix dimensions and values
- Matrix multiplication with compatibility checking
- Error handling for invalid inputs
- Clear output formatting

## How It Works

The program guides users through creating two matrices and then multiplies them if they are compatible for multiplication.

### Matrix Multiplication Rules

Two matrices can be multiplied only if the number of columns in the first matrix equals the number of rows in the second matrix. The resulting matrix will have dimensions of (rows of first matrix) × (columns of second matrix).

## Usage

1. Run the program:
   ```bash
   python matrix_multiplication.py
   ```

2. Follow the prompts to create Matrix A:
   - Enter the number of rows
   - Enter the number of columns
   - Enter each row as comma-separated integers

3. Follow the same process to create Matrix B

4. The program will either:
   - Display the result matrix if multiplication is possible
   - Show an error message if matrices cannot be multiplied

## Example

```
Matrix A
Enter the number of rows: 2
Enter the number of columns: 3
Enter row 1 as a comma separated list of 3 integers: 1, 2, 3
Enter row 2 as a comma separated list of 3 integers: 4, 5, 6

Matrix B
Enter the number of rows: 3
Enter the number of columns: 2
Enter row 1 as a comma separated list of 2 integers: 7, 8
Enter row 2 as a comma separated list of 2 integers: 9, 10
Enter row 3 as a comma separated list of 2 integers: 11, 12

Result Matrix:
[[58, 64], [139, 154]]
```

## Functions

### `createMatrix()`
- Prompts user for matrix dimensions and values
- Validates input for proper format and data types
- Returns a 2D list representing the matrix

### `multipleMatrix(matrixA, matrixB)`
- Performs matrix multiplication on two input matrices
- Checks compatibility before multiplication
- Returns the result matrix or None if incompatible

### `main()`
- Controls program flow
- Handles the overall user interaction
- Manages the multiplication process and output

## Input Validation

The program includes robust error handling for:
- Non-integer values for matrix dimensions
- Incorrect number of values in a row
- Non-integer values in matrix elements
- Incompatible matrix dimensions for multiplication

## Requirements

- Python 3.x
- No external dependencies required

## Installation

1. Clone or download the script
2. Ensure Python 3.x is installed on your system
3. Run the script directly with `python matrix_multiplication.py`

## Error Handling

- **Invalid dimensions**: Program will re-prompt for valid integer inputs
- **Row length mismatch**: Program will ask to re-enter the row with correct number of elements
- **Non-integer values**: Program will request integer values only
- **Incompatible matrices**: Program will restart and ask for new matrices

## Mathematical Background

Matrix multiplication follows the rule:
```
C[i][j] = Σ(A[i][k] × B[k][j]) for k from 0 to n-1
```

Where:
- A is an m×n matrix
- B is an n×p matrix  
- C is the resulting m×p matrix

## License

This project is available for educational and personal use.
