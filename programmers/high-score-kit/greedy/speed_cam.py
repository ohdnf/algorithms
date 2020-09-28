def solution(routes):
    answer = 0
    routes.sort(key=lambda r: (r[0], r[1]))
    last_ent = last_out = -30001
    for ent, out in routes:
        # print(last_ent, last_out, ent, out)
        if ent not in range(last_ent, last_out+1):
            last_out = out
            answer += 1
        else:
            if last_out > out:
                last_out = out
        last_ent = ent
            
    return answer


# 다른 사람의 풀이
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer

if __name__ == "__main__":
    print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]), 2)