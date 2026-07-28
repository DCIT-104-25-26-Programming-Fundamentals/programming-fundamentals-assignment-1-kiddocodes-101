# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def read_matrix(rows, cols):
    """Read a matrix of given size from user input."""
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        if len(row) != cols:
            print("Error: Row must have exactly", cols, "values.")
            return None
        matrix.append(row)
    return matrix


def display_matrix(matrix):
    """Display a matrix in neat grid format."""
    for row in matrix:
        print("  ".join(str(x) for x in row))


#  PART A: Transpose 
def transpose_matrix(matrix):
    """Return the transpose of a matrix."""
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)
    return transpose


#  PART B: Addition 
def add_matrices(A, B):
    """Return the sum of two matrices of same size."""
    rows = len(A)
    cols = len(A[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(A[i][j] + B[i][j])
        result.append(new_row)
    return result


#  PART C: Multiplication 
def multiply_matrices(A, B):
    """Return the product of two matrices (A x B)."""
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print("Error: Number of columns in A must equal number of rows in B.")
        return None

    result = []
    for i in range(rows_A):
        new_row = []
        for j in range(cols_B):
            total = 0
            for k in range(cols_A):
                total += A[i][k] * B[k][j]
            new_row.append(total)
        result.append(new_row)
    return result


#  MAIN PROGRAM 
if __name__ == "__main__":
    # Part A: Transpose
    print("=== PART A: Transpose a Matrix ===")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    matrix = read_matrix(m, n)
    if matrix:
        print("\nOriginal Matrix:")
        display_matrix(matrix)
        print("\nTransposed Matrix:")
        display_matrix(transpose_matrix(matrix))

    # Part B: Addition
    print("\n=== PART B: Add Two Matrices ===")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    print("Matrix A:")
    A = read_matrix(m, n)
    print("Matrix B:")
    B = read_matrix(m, n)
    if A and B:
        print("\nResult (A + B):")
        display_matrix(add_matrices(A, B))

    # Part C: Multiplication
    print("\n=== PART C: Multiply Two Matrices ===")
    m = int(input("Enter number of rows for Matrix A: "))
    n = int(input("Enter number of columns for Matrix A: "))
    print("Matrix A:")
    A = read_matrix(m, n)

    p = int(input("Enter number of columns for Matrix B: "))
    print("Matrix B:")
    B = read_matrix(n, p)

    if A and B:
        result = multiply_matrices(A, B)
        if result:
            print("\nResult (A x B):")
            display_matrix(result)

