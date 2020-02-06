from math import isclose

T = int(input())

for test_case in (1, T + 1):
    N = int(input())
    cube_root = N ** (1/3)
    result = -1
    if isclose(cube_root, int(cube_root)):
        result = int(cube_root)
    print('#{0} {1}'.format(test_case, result))