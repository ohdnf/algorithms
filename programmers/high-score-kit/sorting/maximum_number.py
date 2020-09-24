import functools


def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer




def solution(numbers):
    return str(int(''.join(sorted(list(map(str, numbers)), key=lambda n: n*3, reverse=True))))



if __name__ == "__main__":
    print(solution([6, 10, 2]))
    print(solution([3, 30, 34, 5, 9]))
    print(solution([121, 12]))
    print(solution([0, 0, 0, 0, 0, 0]))