import numpy as np
from heapq import merge
import multiprocessing

def prod(x1, x2):
    return np.sum((i*j) for (i,j) in zip(x1,x2))

def row_prod(row, matrix):
    r = []
    for i in range(matrix.shape[1]):
        col = [matrix[k][i] for k in range(len(matrix))]
        r.append(prod(row, col))
    return r

    
def sort_2(lst, end=None):
    if len(lst) < 2:
        res = lst
    else:
        mid = len(lst) // 2

        inputs = [lst[:mid], lst[mid:]]
        pipes = [multiprocessing.Pipe(False) for _ in inputs]
        processes = [multiprocessing.Process(target=sort_2, args=(input, end))
                    for input, (get_end, end) in zip(inputs, pipes)]
        for process in processes: process.start()
        for process in processes: process.join()
        result = [get_end.recv() for get_end, end in pipes]
        
        res = list(merge(*result))

    if end:
        end.send(res)
    else:
        return res