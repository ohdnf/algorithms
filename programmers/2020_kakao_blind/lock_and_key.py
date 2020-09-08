def solution(key, lock):
    answer = True
    len_key = len(key[0])
    len_lock = len(key[0])
    
    print("key")
    for line in key:
        print(line)

    print()
    # 180도 회전
    key_180 = list()
    for i in range(len_key-1, -1, -1):
        key_180.append(key[i][::-1])

    print("key 180")
    for line in key_180:
        print(line)

    print()
    # 90도 회전
    tmp = list()
    for i in range(len_key):
        tmp.append(key_180[i][::-1])
    key_90 = list(zip(*tmp))

    print("key 90")
    for line in key_90:
        print(line)

    print()
    # 270도 회전
    tmp = list(zip(*tmp))
    key_270 = list()
    for i in range(len_key-1, -1, -1):
        key_270.append(tmp[i][::-1])

    print("key 270")
    for line in key_270:
        print(line)


    return answer


if __name__ == "__main__":
    k = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    l = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(k, l))
