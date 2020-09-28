def solution(n, costs):
    answer = 0
    pi = [-1] * n
    rank = [0] * n

    def find_set(i):
        if pi[i] == i: return i
        else:
            pi[i] = find_set(pi[i])
            return pi[i]

    def union(i1, i2):
        pi1 = find_set(i1)
        pi2 = find_set(i2)
        if rank[pi1] > rank[pi2]:
            pi[pi2] = pi1
        else:
            pi[pi1] = pi2
            if rank[pi1] == rank[pi2]:
                rank[pi2] += 1

    for i in range(n):
        pi[i] = i

    costs.sort(key=lambda c: c[2])
    for i1, i2, cost in costs:
        if find_set(i1) == find_set(i2): continue

        union(i1, i2)
        answer += cost

    return answer


if __name__ == "__main__":
    print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
