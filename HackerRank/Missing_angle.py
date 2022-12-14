import math
from math import sqrt,sin,cos,degrees
import numpy
from numpy import arcsin,arccos
ab = int(input())
bc = int(input())
ab_sq = pow(ab, 2)
bc_sq = pow(bc, 2)
ac = sqrt(ab_sq + bc_sq)
# print(ac)
mc = ac/2
acb = numpy.arcsin(ab/ac)
deg_acb = degrees(acb)
print(round(deg_acb))