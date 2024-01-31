def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
    matrix (list of lists): The matrix to be divided.
    div (int or float): The divisor.

    Returns:
    list of lists: The resulting matrix with elements divided by div.

    Raises:
    TypeError: If matrix is not a list of lists of integers or floats,
               or if div is not a number (integer or float).
    ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(val, (int, float)) for row in matrix for val in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    divided_matrix = []
    for row in matrix:
        divided_row = [round(elem / div, 2) for elem in row]
        divided_matrix.append(divided_row)

    return divided_matrix

