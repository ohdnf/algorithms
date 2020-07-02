import sys
input = lambda: sys.stdin.readline()
n = int(input())
scores = list(map(int, input().split()))
avg = int(sum(scores)/n+0.5)    # Python의 round() 함수는 round-half-even 방식을 취한다
min_diff = 101
min_score = 101
res_number = 101
for idx, score in enumerate(scores):
    diff = abs(score - avg)
    if diff < min_diff:
        min_diff = diff
        res_score = score
        res_number = idx + 1
    elif diff == min_diff:
        if score > res_score:
            res_score = score
            res_number = idx + 1
print(avg, res_number)