class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class MatrixSummationException(Error):
    def __init__(self):
        self.message = 'ERROR: rows or columns numbers are not equal!'


class MatrixMultipltionException(Error):
    def __init__(self):
        self.message = 'ERROR: Can not multiple these matrixes!\n'
