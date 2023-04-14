import numpy as np


def get_kernels():
    kernels = {}

    vertical_kernel = np.zeros((5, 5))
    vertical_kernel[:, 2] = 1
    kernels["vertical_kernel"] = vertical_kernel

    horizontal_kernel = np.zeros((5, 5))
    horizontal_kernel[2, :] = 1
    kernels["horizontal_kernel"] = horizontal_kernel

    x_kernel = np.zeros((5, 5))
    for i in range(5):
        x_kernel[i, i] = 1
        x_kernel[i, 4 - i] = 1
    kernels["x_kernel"] = x_kernel

    star_kernel = np.copy(x_kernel)
    star_kernel[2, :] = 1
    star_kernel[:, 2] = 1
    kernels["star_kernel"] = star_kernel

    o_kernel = np.ones((5, 5))
    o_kernel[1:-1, 1:-1] = 0
    kernels["o_kernel"] = o_kernel

    division_kernel = np.zeros((5, 5))
    reversed_division_kernel = np.zeros((5, 5))
    for i in range(5):
        division_kernel[i, i] = 1
        reversed_division_kernel[i, 4 - i] = 1
    kernels["division_kernel"] = x_kernel
    kernels["reversed_division_kernel"] = x_kernel

    full_kernel = np.ones((5, 5))
    kernels["full_kernel"] = full_kernel

    return kernels
