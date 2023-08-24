"""
MIT License

Copyright (c) 2023 Diego Sealtiel Valderrama Garcia

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import numpy as np


def matrixsort_np(elements):
    """Matrix sort (with numpy)."""

    max_element = max(elements)
    matrix = np.zeros((max_element + 1, len(elements)))
    matrix[elements, np.arange(len(elements))] = elements

    return matrix.sum(axis=1)


def matrixsort(elements):
    """Matrix sort."""
    
    max_element = max(elements)
    matrix = [[0] * len(elements) for _ in range(max_element + 1)]

    for i, element in enumerate(elements):
        matrix[element][i] = element

    row_sums = [sum(row) for row in matrix]

    return row_sums


def maxinsort(elements):
    """Maxin sort (Max sort)."""
    end = len(elements)
    
    while True:
        m = elements.index(max(elements[:end]))
        elements[end - 1], elements[m] = elements[m], elements[end - 1]
                
        end -= 1
        
        if end <= 1:
            break
        
    
    return elements


def colomossort(elements):
    """Colomos sort."""
    _min, _max = [], []
    length = len(elements)
    
    if length == 2:
        if elements[0] > elements[1]:
            return [elements[1], elements[0]]
        
        return elements
    elif length <= 1:
        return elements
    
    m = sum(elements) / length
    
    for v in elements:
        if v > m:
            _max.append(v)
        else:
            _min.append(v)
            
    _min = colomossort(_min)
    _max = colomossort(_max)
    
    return _min + _max
  
