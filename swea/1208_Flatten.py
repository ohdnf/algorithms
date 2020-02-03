for t in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    mx = mn = 0
    for idx in range(100):
        if boxes[idx] > boxes[mx]:
            mx = idx
        elif boxes[idx] < boxes[mn]:
            mn = idx

    while dump > 0:
        if boxes[mx] == boxes[mn]:
            break
        boxes[mx] -= 1
        boxes[mn] += 1
        for idx in range(100):
            if boxes[idx] > boxes[mx]:
                mx = idx
            elif boxes[idx] < boxes[mn]:
                mn = idx
        dump -= 1
    
    result = boxes[mx] - boxes[mn]
    
    print('#{0} {1}'.format(t, result))
