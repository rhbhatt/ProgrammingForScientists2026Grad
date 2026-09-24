#!/usr/bin/env python3
from dataclasses import dataclass
from pprint import pprint

@dataclass
class DistanceMatrix:
    matrix: list[list[float]]

    def add_row_col(self, l: list[float]):
        for row, item in zip(self.matrix, l):
            row.append(item)
        self.matrix.append(l.copy())

    def del_rows_cols(self, indices: list[int]):
        pass

    def find_min_element(self) -> tuple[int, int, float]:
        curr_min = self.matrix[0][1]
        curr_row = 0
        curr_col = 1
        for i in range(len(self.matrix)):
            row = self.matrix[i]
            for j, item in enumerate(row):
                if i == j:
                    continue
                if item < curr_min and item != 0:
                    curr_min = item
                    curr_row = i
                    curr_col = j
        return curr_row, curr_col, curr_min

# test data

d = DistanceMatrix(
    matrix=[
        [0, 3, 4, 3],
        [3, 0, 4, 5],
        [4, 4, 0, 2],
        [3, 5, 2, 0],
    ]
)

print(d.find_min_element())
assert d.find_min_element() == (2, 3, 2)

#print(d)
pprint(d.matrix)
d.add_row_col([3.5, 4.5, 0, 0, 0])

assert d.matrix == [
    [0, 3, 4, 3, 3.5],
    [3, 0, 4, 5, 4.5],
    [4, 4, 0, 2, 0],
    [3, 5, 2, 0, 0],
    [3.5, 4.5, 0, 0, 0],
]

d.del_rows_cols([2, 3])
pprint(d.matrix)

assert d.matrix == [
    [0, 3, 3.5],
    [3, 0, 4.5],
    [3.5, 4.5, 0],
]

assert d.find_min_element() == 3
