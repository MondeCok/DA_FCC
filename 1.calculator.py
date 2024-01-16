import numpy as np

def calculate(matrix):

    matrix_np = np.array(matrix).reshape(3, 3)

    mean = np.mean(matrix_np)
    variance = np.var(matrix_np)
    std_dev = np.std(matrix_np)
    max_val = np.max(matrix_np)
    min_val = np.min(matrix_np)
    sum_val = np.sum(matrix_np)


    mean_axis0 = np.mean(matrix_np, axis=0)
    mean_axis1 = np.mean(matrix_np, axis=1)
    variance_axis0 = np.var(matrix_np, axis=0)
    variance_axis1 = np.var(matrix_np, axis=1)
    std_dev_axis0 = np.std(matrix_np, axis=0)
    std_dev_axis1 = np.std(matrix_np, axis=1)
    max_axis0 = np.max(matrix_np, axis=0)
    max_axis1 = np.max(matrix_np, axis=1)
    min_axis0 = np.min(matrix_np, axis=0)
    min_axis1 = np.min(matrix_np, axis=1)
    sum_axis0 = np.sum(matrix_np, axis=0)
    sum_axis1 = np.sum(matrix_np, axis=1)


    return {
        'mean' : [mean_axis0, mean_axis1, mean],
        'variance' : [variance_axis0, variance_axis1, variance],
        'standard deviation' : [std_dev_axis0, std_dev_axis1, std_dev],
        'max' : [max_axis0, max_axis1, max_val],
        'min' : [min_axis0, min_axis1, min_val],
        'sum' : [sum_axis0, sum_axis1, sum_val]
    }