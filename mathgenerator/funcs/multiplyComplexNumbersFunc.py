from .__init__ import *
from ..__init__ import Generator


def multiplyComplexNumbersFunc(minRealImaginaryNum=-20,
                               maxRealImaginaryNum=20):
    num1 = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum),
                   random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    num2 = complex(random.randint(minRealImaginaryNum, maxRealImaginaryNum),
                   random.randint(minRealImaginaryNum, maxRealImaginaryNum))
    problem = f"{num1} * {num2} = "
    solution = num1 * num2
    return problem, solution


complexNumMultiply = Generator("Multiplication of 2 complex numbers", 65,
                               "(x + j) (y + j) = ", "xy + xj + yj -1",
                               multiplyComplexNumbersFunc)
