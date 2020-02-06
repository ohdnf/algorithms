T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    
    max_hap = min_hap = sum(numbers[:m])

    for i in range(n-m+1):
        temp = sum(numbers[i:i+m])
        if temp > max_hap:
            max_hap = temp
        if temp < min_hap:
            min_hap = temp
    
    print('#{0} {1}'.format(t, max_hap - min_hap))