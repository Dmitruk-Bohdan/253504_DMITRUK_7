import numpy as np
#from pandas import DataFrame

class NumpyHandler:
    """
    A class that demonstrates the capabilities of the NumPy library for working with arrays and mathematical/statistical operations.
    """

    def __init__(self, n, m):
        """
        Initializes the NumpyDemonstrator object.

        Parameters:
        - n (int): The number of rows in the matrix.
        - m (int): The number of columns in the matrix.
        """
        self.n = n
        self.m = m
        self.A = np.random.randint(0, 10, size=(n, m))
    
    def demonstrate_creation(self):
        """
        Demonstrates array creation using the array() and values() functions.
        """
        B = np.array([1, 2, 3, 4, 5])
        print("Array B:", B)

        # print("Demostration of 'values method':")
        # data = {'Name': ['John', 'Alice', 'Bob'],
        #         'Age': [25, 28, 30],
        #         'City': ['New York', 'Paris', 'London']}

        # df = DataFrame(data)

        # values_array = df.values

        # print(values_array)
    
    def demonstrate_indexing(self):
        """
        Demonstrates indexing of NumPy arrays.
        """
        print("Element A[0, 0]:", self.A[0, 0])
        print("Row A[2]:", self.A[2])
        print("Column A[:, 3]:", self.A[:, 3])
        print("Slice A[1:4, 1:4]:")
        print(self.A[1:4, 1:4])
    
    def demonstrate_operations(self):
        """
        Demonstrates operations with NumPy arrays.
        """
        print("Sum of elements in A:", np.sum(self.A))
        print("Minimum element in A: {:.2f}".format(np.min(self.A)))
        print("Maximum element in A:", np.max(self.A))
        print("Transposed matrix A:")
        print(np.transpose(self.A))
    
    def demonstrate_math_statistics(self):
        """
        Demonstrates mathematical and statistical operations with NumPy arrays.
        """
        print("Mean of elements in A:", np.mean(self.A))
        print("Median of elements in A:", np.median(self.A))
        print("Correlation matrix of A:")
        print(np.corrcoef(self.A))
        print("Variance of elements in the secondary diagonal:")
        diagonal = np.diagonal(self.A[::-1])
        variance = np.var(diagonal)
        print("Method 1 (using the standard function): {:.2f}".format(variance))
        print("Method 2 (using the formula): {:.2f}".format(self.calculate_variance(diagonal)))
    
    def calculate_variance(self, diagonal):
        """
        Calculates the variance of elements in the secondary diagonal.

        Parameters:
        - diagonal (ndarray): The secondary diagonal of the matrix.

        Returns:
        - variance (float): The variance of the diagonal elements.
        """
        mean = np.mean(diagonal)
        squared_diff = np.power(diagonal - mean, 2)
        variance = np.mean(squared_diff)
        return variance

    def demonstrate():
        """
        Demonstrates the capabilities of the NumPyDemonstrator class.
        """
        demonstrator = NumpyHandler(5, 5)
        demonstrator.demonstrate_creation()
        demonstrator.demonstrate_indexing()
        demonstrator.demonstrate_operations()
        demonstrator.demonstrate_math_statistics()
