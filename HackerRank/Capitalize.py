# Complete the solve function below.
import os
def solve(s):
    l = [x.capitalize() for x in s.split(" ")]
    return ' '.join(l)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
