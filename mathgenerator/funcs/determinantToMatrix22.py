from .__init__ import *
from ..__init__ import Generator


def determinantToMatrix22(maxMatrixVal=100):
    a = random.randint(0, maxMatrixVal)
    b = random.randint(0, maxMatrixVal)
    c = random.randint(0, maxMatrixVal)
    d = random.randint(0, maxMatrixVal)

    determinant = a * d - b * c
    problem = f"Det([[{a}, {b}], [{c}, {d}]]) = "
    solution = f" {determinant}"
    return problem, solution


intMatrix22determinant = Generator("Determinant to 2x2 Matrix", 77,
                                   "Det([[a,b],[c,d]]) =", " a * d - b * c",
                                   determinantToMatrix22)
