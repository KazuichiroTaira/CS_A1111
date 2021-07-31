# Y1 SUMMER 2021
# Basic Course in Programming Y1
# Grids for Sudoku Checker exercise 6.3
# Author: Vilma Kahri and Joel Lahenius

GRID_NAMES = ["is valid", "is valid containing None values", "is valid containing None values (2)",
              "has an invalid row", "has an invalid column", "has an invalid subgrid"]

GRID_RETURNS = ["True", "True", "True", "False", "False", "False"]

n = None

a = 'a'
b = 'b'
c = 'c'
d = 'd'
e = 'e'
f = 'f'
g = 'g'

GRID_VALID = [[7, 3, 5, 6, 1, 4, 8, 9, 2],
              [8, 4, 2, 9, 7, 3, 5, 6, 1],
              [9, 6, 1, 2, 8, 5, 3, 7, 4],

              [2, 8, 6, 3, 4, 9, 1, 5, 7],
              [4, 1, 3, 8, 5, 7, 9, 2, 6],
              [5, 7, 9, 1, 2, 6, 4, 3, 8],

              [1, 5, 7, 4, 9, 2, 6, 8, 3],
              [6, 9, 4, 7, 3, 8, 2, 1, 5],
              [3, 2, 8, 5, 6, 1, 7, 4, 9]
              ]

GRID_VALID_NONE = [[7, 3, 5, 6, 1, 4, 8, 9, 2],
                   [8, 4, 2, 9, 7, 3, 5, 6, 1],
                   [9, 6, 1, 2, 8, 5, 3, 7, 4],

                   [2, n, n, 3, 4, n, 1, 5, 7],
                   [4, 1, 3, 8, 5, 7, 9, 2, 6],
                   [5, 7, 9, 1, 2, 6, 4, 3, 8],

                   [1, 5, 7, 4, 9, n, 6, 8, 3],
                   [6, 9, 4, 7, 3, 8, 2, 1, 5],
                   [n, 2, 8, 5, 6, 1, 7, 4, 9]
                   ]

GRID_VALID_NONE_2 = [[7, 3, 5, 6, 1, 4, n, 9, 2],
                     [8, 4, 2, 9, 7, 3, 5, 6, 1],
                     [n, n, 1, 2, 8, 5, 3, 7, 4],

                     [2, n, n, 3, 4, n, 1, 5, 7],
                     [4, 1, 3, 8, 5, 7, 9, 2, 6],
                     [5, n, 9, 1, 2, 6, 4, 3, 8],

                     [1, 5, 7, 4, 9, n, n, 8, 3],
                     [6, 9, 4, 7, 3, 8, 2, 1, 5],
                     [n, 2, 8, 5, 6, 1, 7, 4, n]
                     ]

GRID_INVALID_SUBGRID = [[7, 3, 5, 6, 1, 4, 8, 9, 2],
                        [8, 4, 2, 9, 7, 3, 5, 6, 1],
                        [9, 6, 1, 2, 8, 5, 3, 7, 4],

                        [2, 8, 6, 3, 4, 9, 1, 5, 7],
                        [4, 1, 3, n, 5, 7, 9, 2, 6],
                        [5, 7, 9, 1, 2, 6, 4, 3, 8],

                        [1, 5, 7, 4, 9, 2, 6, 8, 3],
                        [6, 9, 4, 7, 3, 8, 2, 1, 5],
                        [3, 2, n, 8, 6, 1, 7, 4, 9]
                        ]

GRID_INVALID_ROW = [[7, 3, 5, 6, 1, 4, 8, 9, 2],
                    [8, 4, 2, 9, 7, 3, 5, 6, 1],
                    [9, 6, 1, 2, 8, 5, 3, 7, 4],

                    [2, 8, 6, 3, 4, 9, 1, 5, 7],
                    [4, 1, 3, 8, 5, 7, 9, 2, 6],
                    [5, 7, 9, 1, 2, 6, 4, 3, 8],

                    [1, 5, 7, 4, 9, 2, 6, 8, n],
                    [6, 9, 4, 7, 3, 8, 2, 1, 3],
                    [3, 2, 8, 5, 6, 1, 7, 4, 9]
                    ]

GRID_INVALID_COLUMN = [[7, 3, 5, 6, 1, 4, 8, 9, 2],
                       [8, 4, 2, 9, 7, 3, 5, 6, 1],
                       [9, 6, 1, 2, 8, 5, 3, 7, 4],

                       [2, 8, 6, 3, 4, 9, 1, 5, 7],
                       [4, 1, 3, 8, 5, 7, 9, 2, 6],
                       [5, 7, 9, 1, 2, 6, 4, 3, 8],

                       [1, 5, n, 4, 9, 2, 6, 8, 3],
                       [6, 9, 4, 7, 3, 8, 2, 1, 5],
                       [7, 2, 8, 5, 6, 1, n, 4, 9]
                       ]

GRIDS = [GRID_VALID, GRID_VALID_NONE, GRID_VALID_NONE_2, \
         GRID_INVALID_ROW, GRID_INVALID_COLUMN, GRID_INVALID_SUBGRID]

GRID_SMALL_VALID = [[1, 2, 3, 4],
                    [3, 4, 1, 2],

                    [2, 3, 4, 1],
                    [4, 1, 2, 3]]

GRID_SMALL_VALID_NONE = [[1, n, 3, 4],
                         [3, 4, n, n],

                         [2, n, 4, 1],
                         [4, 1, n, 3]]

GRID_SMALL_VALID_NONE_2 = [[1, n, 3, 4],
                           [n, n, n, 2],

                           [2, n, 4, 1],
                           [4, n, 2, 3]]

GRID_SMALL_INVALID_ROW = [[1, 2, 3, n],
                          [2, 3, 4, 4],

                          [3, 4, 1, 2],
                          [4, 1, 2, 3]]

GRID_SMALL_INVALID_COLUMN = [[1, 2, 3, 4],
                             [2, 3, 4, 1],

                             [3, 4, n, 1],
                             [4, 1, 2, 3]]

GRID_SMALL_INVALID_SUBGRID = [[1, 2, 3, 4],
                              [2, 3, 4, 1],

                              [3, 4, 1, 2],
                              [4, 1, 2, 3]]

GRIDS_SMALL = [GRID_SMALL_VALID, GRID_SMALL_VALID_NONE, GRID_SMALL_VALID_NONE_2, \
               GRID_SMALL_INVALID_ROW, GRID_SMALL_INVALID_COLUMN, GRID_SMALL_INVALID_SUBGRID]

GRID_BIG_VALID = [[4, a, 9, f, 1, 7, d, 8, 6, e, 2, c, g, 5, 3, b],
                  [2, 5, 3, 1, f, 4, b, g, d, 9, 8, 7, 6, a, c, e],
                  [e, 6, d, c, 3, a, 5, 2, g, b, 1, 4, 8, f, 9, 7],
                  [b, 7, g, 8, 6, e, 9, c, 5, 3, a, f, 1, 2, d, 4],

                  [8, g, b, 4, d, f, e, 9, 2, 5, 7, 3, c, 1, a, 6],
                  [1, e, 6, d, c, 8, 4, 5, a, g, 9, b, 2, 3, 7, f],
                  [a, f, 5, 3, 2, 1, 6, 7, 4, c, e, 8, 9, b, g, d],
                  [c, 2, 7, 9, b, 3, g, a, f, d, 6, 1, 4, 8, e, 5],

                  [9, 4, 1, a, e, 2, 3, d, b, f, c, 6, 7, g, 5, 8],
                  [5, 8, e, g, 7, 9, 1, 6, 3, 4, d, a, b, c, f, 2],
                  [7, 3, f, 6, g, b, c, 4, 8, 2, 5, 9, e, d, 1, a],
                  [d, c, 2, b, a, 5, 8, f, 7, 1, g, e, 3, 6, 4, 9],

                  [f, 9, 8, 2, 4, c, 7, 3, 1, a, b, d, 5, e, 6, g],
                  [6, d, c, 5, 9, g, f, 1, e, 8, 4, 2, a, 7, b, 3],
                  [g, b, 4, 7, 8, d, a, e, c, 6, 3, 5, f, 9, 2, 1],
                  [3, 1, a, e, 5, 6, 2, b, 9, 7, f, g, d, 4, 8, c]
                  ]

GRID_BIG_VALID_NONE = [[4, a, 9, n, 1, 7, d, 8, 6, e, n, c, g, 5, 3, n],
                       [n, 5, 3, 1, f, n, b, g, d, 9, 8, 7, 6, a, c, e],
                       [e, 6, d, c, 3, a, 5, 2, g, b, n, 4, n, f, n, 7],
                       [b, 7, n, 8, n, e, 9, c, n, 3, a, f, 1, 2, d, 4],

                       [8, g, b, 4, d, f, n, 9, 2, 5, 7, n, c, 1, a, 6],
                       [1, e, n, d, c, n, 4, 5, a, g, n, b, 2, 3, 7, f],
                       [a, f, n, 3, 2, 1, n, 7, n, n, e, 8, 9, b, g, n],
                       [c, 2, 7, 9, b, 3, g, a, f, d, 6, 1, 4, n, n, 5],

                       [9, 4, 1, a, e, n, 3, d, b, f, c, 6, 7, g, 5, 8],
                       [5, n, e, g, 7, 9, n, 6, 3, 4, d, a, b, n, f, 2],
                       [7, 3, f, 6, g, b, c, 4, n, n, 5, 9, e, d, n, a],
                       [n, n, n, b, a, 5, 8, f, 7, 1, n, e, 3, 6, 4, 9],

                       [f, 9, 8, 2, 4, c, 7, 3, n, n, b, d, 5, e, 6, g],
                       [6, n, c, 5, 9, n, f, 1, e, n, 4, 2, a, 7, n, 3],
                       [g, b, 4, 7, 8, d, a, e, c, 6, n, 5, f, 9, 2, n],
                       [3, 1, n, n, n, 6, 2, b, 9, 7, f, g, d, 4, 8, c]
                       ]

GRID_BIG_VALID_NONE_2 = [[4, a, 9, f, 1, 7, d, n, 6, e, n, n, g, n, 3, b],
                         [2, 5, 3, 1, f, 4, b, g, d, n, 8, 7, 6, a, n, e],
                         [e, 6, d, c, 3, a, n, 2, g, b, 1, 4, 8, f, 9, 7],
                         [b, 7, g, n, n, e, 9, c, 5, 3, a, n, n, 2, d, 4],

                         [8, g, b, 4, d, f, e, n, 2, 5, 7, 3, c, 1, a, 6],
                         [1, n, 6, d, n, n, 4, n, a, g, n, b, 2, 3, 7, f],
                         [a, f, 5, 3, 2, 1, 6, 7, 4, c, e, 8, 9, b, g, d],
                         [c, 2, 7, n, b, 3, g, a, f, d, 6, 1, 4, 8, e, 5],

                         [9, 4, 1, a, e, 2, n, n, b, f, c, n, 7, g, 5, 8],
                         [5, n, e, g, 7, 9, n, 6, 3, 4, d, a, b, c, f, 2],
                         [7, 3, f, 6, g, b, c, 4, 8, n, n, n, e, d, 1, a],
                         [d, c, 2, n, a, n, 8, f, 7, 1, g, n, 3, 6, n, 9],

                         [f, n, 8, 2, 4, c, 7, 3, 1, a, b, d, n, e, 6, n],
                         [6, d, c, 5, 9, g, f, 1, e, 8, 4, 2, a, 7, b, 3],
                         [g, b, n, 7, 8, d, a, e, n, 6, n, 5, f, n, 2, n],
                         [n, 1, a, e, n, 6, 2, b, 9, n, f, g, d, n, 8, c]
                         ]

GRID_BIG_INVALID_ROW = [[4, a, 9, f, 1, 7, d, 8, 6, e, 2, c, g, 5, 3, b],
                        [2, 5, 3, 1, f, 4, b, g, d, 9, 8, 7, 6, a, c, e],
                        [e, 6, d, c, 3, a, 5, 2, g, b, 1, 4, 8, f, 9, 7],
                        [b, 7, g, 8, 6, e, 9, c, 5, 3, a, f, 1, 2, d, 4],

                        [8, g, b, 4, d, f, e, 9, 2, 5, 7, 3, c, 1, a, 6],
                        [1, e, 6, d, c, n, 4, 5, a, g, 9, b, 2, 3, 7, f],
                        [a, f, 5, 3, 2, 1, 6, 7, 4, c, e, 8, 9, b, g, d],
                        [c, 2, 7, 9, b, 3, g, a, f, d, 6, 1, 4, 8, e, 5],

                        [9, 4, 1, a, e, 2, 3, d, b, f, c, 6, 7, g, 5, 8],
                        [5, 8, e, g, 7, 9, 1, 6, 3, 4, d, a, b, c, f, 2],
                        [7, 3, f, 6, g, b, c, 4, 8, 2, 5, 9, e, d, 1, a],
                        [d, c, 2, b, a, 8, 8, f, 7, 1, g, e, 3, 6, 4, 9],

                        [f, 9, 8, 2, 4, c, 7, 3, 1, a, b, d, 5, e, 6, g],
                        [6, d, c, 5, 9, g, f, 1, e, 8, 4, 2, a, 7, b, 3],
                        [g, b, 4, 7, 8, d, a, e, c, 6, 3, 5, f, 9, 2, 1],
                        [3, 1, a, e, 5, 6, 2, b, 9, 7, f, g, d, 4, 8, c]
                        ]

GRID_BIG_INVALID_COLUMN = [[4, a, 9, f, 1, 7, d, 8, 6, e, 2, c, g, 5, 3, b],
                           [2, 5, 3, 1, f, 4, b, g, d, 9, 8, 7, 6, a, c, e],
                           [e, 6, d, c, 3, a, 5, 2, g, b, 1, 4, 8, f, 9, 7],
                           [b, 7, g, 8, 6, e, 9, c, 5, 3, a, f, 1, 2, d, 4],

                           [8, g, b, 4, d, f, e, 9, 2, 5, 7, 3, c, 1, a, 6],
                           [1, e, 6, d, c, 8, 4, 5, a, g, 9, b, 2, 3, 7, f],
                           [a, f, 5, 3, 2, 1, 6, n, 4, c, e, 8, 9, b, 7, d],
                           [c, 2, 7, 9, b, 3, g, a, f, d, 6, 1, 4, 8, e, 5],

                           [9, 4, 1, a, e, 2, 3, d, b, f, c, 6, 7, g, 5, 8],
                           [5, 8, e, g, 7, 9, 1, 6, 3, 4, d, a, b, c, f, 2],
                           [7, 3, f, 6, g, b, c, 4, 8, 2, 5, 9, e, d, 1, a],
                           [d, c, 2, b, a, 5, 8, f, 7, 1, g, e, 3, 6, 4, 9],

                           [f, 9, 8, 2, 4, c, 7, 3, 1, a, b, d, 5, e, 6, g],
                           [6, d, c, 5, 9, g, f, 1, e, 8, 4, 2, a, 7, b, 3],
                           [g, b, 4, 7, 8, d, a, e, c, 6, 3, 5, f, 9, 2, 1],
                           [3, 1, a, e, 5, 6, 2, b, 9, 7, f, g, d, 4, 8, c]
                           ]

GRID_BIG_INVALID_SUBGRID = [[4, a, 9, f, 1, 7, d, 8, 6, e, 2, c, g, 5, 3, b],
                            [2, 5, 3, 1, f, 4, b, g, d, 9, 8, 7, 6, a, c, e],
                            [e, 6, d, c, 3, a, 5, 2, g, b, 1, 4, 8, f, 9, 7],
                            [b, 7, g, 8, 6, e, 9, c, 5, 3, a, f, 1, 2, d, 4],

                            [8, g, b, 4, d, f, e, 9, 2, 5, 7, 3, c, 1, a, 6],
                            [1, e, 6, d, c, 8, 4, 5, a, g, 9, b, 2, 3, 7, f],
                            [a, f, 5, 3, 2, 1, 6, 7, 4, c, e, 8, 9, b, g, d],
                            [c, 2, 7, 9, b, 3, g, a, f, d, 6, 1, 4, 8, e, 5],

                            [9, 4, 1, a, e, 2, 3, d, b, f, c, 6, 7, g, 5, 8],
                            [5, 8, e, g, 7, 9, 1, 6, 3, n, d, a, b, c, f, 2],
                            [7, 3, f, 6, g, b, c, 4, 8, 2, 5, 9, e, d, 1, a],
                            [d, c, 2, b, a, 5, 8, f, 7, 1, g, e, 3, 6, 4, 9],

                            [f, 9, 8, 2, 4, c, 7, 3, 1, a, b, d, 5, e, 6, g],
                            [6, d, c, 5, 9, g, f, 1, e, 8, 4, 2, a, 7, b, 3],
                            [g, b, n, 7, 8, d, a, e, c, 4, 3, 5, f, 9, 2, 1],
                            [3, 1, a, e, 5, 6, 2, b, 9, 7, f, g, d, 4, 8, c]
                            ]

GRIDS_BIG = [GRID_BIG_VALID, GRID_BIG_VALID_NONE, GRID_BIG_VALID_NONE_2,
             GRID_BIG_INVALID_ROW, GRID_BIG_INVALID_COLUMN, GRID_BIG_INVALID_SUBGRID]


