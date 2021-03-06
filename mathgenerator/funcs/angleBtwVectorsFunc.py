from .__init__ import *
from ..__init__ import Generator


def angleBtwVectorsFunc(maxEltAmt=20):
    s = 0
    v1 = [random.uniform(0, 1000) for i in range(random.randint(2, maxEltAmt))]
    v2 = [random.uniform(0, 1000) for i in v1]
    for i in v1:
        for j in v2:
            s += i * j

    mags = math.sqrt(sum([i**2 for i in v1])) * math.sqrt(sum([i**2 for i in v2]))
    problem = f"angle between the vectors {v1} and {v2} is:"
    solution = ''
    try:
        solution = str(math.acos(s / mags))
    except MathDomainError:
        print('angleBtwVectorsFunc has some issues with math module, line 16')
        solution = 'NaN'
    # would return the answer in radians
    return problem, solution


angleBtwVectors = Generator(
    "Angle between 2 vectors", 70,
    "Angle Between 2 vectors V1=[v11, v12, ..., v1n] and V2=[v21, v22, ....., v2n]",
    "V1.V2 / (euclidNorm(V1)*euclidNorm(V2))", angleBtwVectorsFunc)
