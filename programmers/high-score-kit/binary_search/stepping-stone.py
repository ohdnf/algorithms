def solution(distance, rocks, n):
    rocks.sort()    # 바위 거리 순으로 정렬
    
    lt = 0
    rt = distance // (len(rocks) - n + 1)
    # mid는 현재 최소 바위 간격
    mid = (lt + rt) // 2
    
    
    while lt <= rt:
        removed = 0
        before = 0
        for rock in rocks:
            # 현재 최소 거리보다 짧다면
            if rock - before < mid:
                # 바위 제거
                removed += 1
            # 현재 최소 거리보다 길거나 같다면
            else:
                # 마지막 바위를 현재 바위로 갱신
                before = rock
            # print(f'before: {before}, rock: {rock}')
        # 마지막 바위 처리
        if distance - before < mid:
            removed += 1
        # 제거한 바위의 수가 n보다 작으면
        # 최소 간격 기준이 짧아서 제거할 바위가 적은 것
        # 때문에 최소 간격을 늘려서 제거할 바위를 늘려야 함
        if removed <= n:
            lt = mid + 1
        # 제거한 바위의 수가 n보다 크면
        # 최소 간격 기준이 길어서 제거할 바위가 많은 것
        # 때문에 최소 간격을 줄여서 제거할 바위를 줄여야 함
        elif removed > n:
            rt = mid - 1
        mid = (lt + rt) // 2
        # print(f'mid: {mid}, removed: {removed}, n: {n}')
                
    return mid


if __name__ == "__main__":
    print(solution(25, [2, 14, 11, 21, 17], 2), 4)