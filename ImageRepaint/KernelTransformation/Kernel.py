import numpy as np


class Kernel:
    def __init__(self, kernel_array: np.array, char: str = None, name: str = None):
        self.array: np.array = kernel_array
        self.char: str = char
        self.name: str = name
        self.value: int = np.sum(kernel_array)

    def __str__(self):
        return f"{self.name} -> {self.char}\n {self.array}"

    def __repr__(self):
        return self.__str__() + '\n'
