from collections import deque as dq
from math import ceil

def my_solution(progresses, speeds):
    answer = []
    deploy_date = dq([ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))])
    
    # print(deploy_date)
    
    deploy = 1
    day = deploy_date.popleft()
    while deploy_date:
        if day >= deploy_date[0]:
            deploy += 1
            deploy_date.popleft()
        else:
            answer.append(deploy)
            deploy = 1
            day = deploy_date.popleft()
    answer.append(deploy)
    
    # deploy = 1
    # for i in range(1, len(deploy_date)):
    #     if deploy_date[i-1] >= deploy_date[i]:
    #         deploy += 1
    #     else:
    #         answer.append(deploy)
    #         deploy = 1
    # answer.append(deploy)
    
    return answer


def other_solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer