박영준 선생님

# APS Python 기본

Algorithm(Advanced) Problem Solving

~~Advanced Planning and Scheduling~~



## 1. Array I

내가 짜놓은 코드가 항상 똑같이 돌아가는 것은 아니다. C, Java는 하드웨어, 가상환경에 따라 컴파일이 달라질 수 있다. 이를 이해하기 위해선 컴퓨터 구조를 알아야 한다.

- 알고리즘

    - Code 짤 때 주석 먼저 짜보기(Pseudo Code)

- 배열

    - Memory 안에 번호를 붙여서 접근하기 쉽게 만든 자료구조
    - `for`문 등 `index` 접근을 할 때는 배열의 처음부터 마지막 범위를 적어놓기(적어도 주석처리)

- 디버깅

    - 에러가 나지 않는 상황에서 논리적인 오류를 찾는 과정

- 완전검색

    - 순열
    

- 그리디(Greedy Algorithm)
- 버블 정렬(Bubble Sort)
- 카운팅 정렬(Counting Sort)



## 2. Array II



## 3. String



## 4. Stack I

- Linear structure

- LIFO(Last-In-First-Out)



### Memoization

- 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술이다. 동적 계획법의 핵심이 되는 기술이다.

- `memoization`은 글자 그대로 해석하면 '메모리에 넣기(to put in memory)'라는 의미이며 '기억되어야 할 것'이라는 뜻의 라틴어 `memorandum`에서 파생되었다. 흔히 '기억하기', '암기하기'라는 뜻의 `memorization`과 혼동하지만, 정확한 단어는 `memoization`이다. 동사형은 `memoize`이다.



#### Fibonacci & Memoization

- recursion function for pibonacci in Python

    중복 호출이 존재 -> 실행시간 = `O(2**n)`

    ```python
    def fibo(n):
        if n < 2:
            return n
        else:
            return fibo(n-1) + fibo(n-2)

    fibo(7)
    ```



- fibonacci applying memoization

    실행시간을 `O(n)`으로 줄일 수 있다.

    ```python
    # memo를 위한 배열을 할당하고, 모두 0으로 초기화한다.
    # memo[0]을 0으로 memo[1]는 1로 초기화한다

    def fibo(n):
        global memo
        if n >= 2 and len(memo) <= n:
            memo.append(fibo(n-1) + fibo(n-2))
        return memo[n]

    memo = [0, 1]
    ```



### DP(Dynamic Programming)

- **최적화 문제**를 해결하는 알고리즘

- 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘

- pibonacci applying DP

    ```python
    def fibo(n):
        f = [0, 1]

        for i in range(2, n+1):
            f.append(f[i-1] + f[i-2])
        
        return f[n]
    ```

- `memoization`을 재귀적 구조에 사용하는 것보다 반복적 구조로 `DP`를 구현한 것이 성능면에서 보다 효율적

- 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문



### Graph 탐색

- 비선형구조인 그래프는 모든 자료(노드)를 빠짐없이 검색하는 것이 중요

- 종류

    1. 깊이 우선 탐색(Depth First Search, DFS)

    2. 너비 우선 탐색(Breadth First Search, BFS)

- 순회 방법

    1. 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색
    
    2. 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아 감
    
    3. 다른 방향의 정점으로 탐색을 계속 반복

- **LIFO** 구조의 **Stack** 사용

    가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 DFS를 반복



#### DFS

1. 시작 정점 `v`를 결정하여 방문

2. 정점 `v`에 인접한 정점 중

    2-1. 방문하지 않은 정점 `w`가 있으면, 정점 `v`를 스택에 `push`하고 정점 `w`를 방문하고 `w`를 `v`로 하여 다시 `2.` 반복

    2-2. 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 `pop`하여 받은 가장 마지막 방문 정점을 `v`로 하여 다시 `2.` 반복

3. 스택이 공백이 될 때까지 `2.`를 반복

Python 구현

```python
def dfs(v):
    stack = list()
    visited[v] = True
    # visit_action(v)
    # print(v, end=' ')
    stack.append(v)
    # 첫 노드는 무조건 연결된다고 가정
    while stack:
        for w in adj[v]:    # 인접 노드 방문
            if not visited[w]:
                visited[w] = True
                # visit_action(w)
                # print(w, end=' ')
                stack.append(w)
                v = w
                break
        else:   # 인접노드가 없거나 모두 방문했을 경우
            v = stack.pop()
```



## 5. Stack II

### 중위 표기법에서 후위 표기법으로의 변환 I

1. 연산자 우선순위에 따라 괄호 표기

2. 각 연산자를 대응하는 오른쪽 괄호 뒤로 이동

3. 괄호 제거



### 중위 표기법에서 후위 표기법으로의 변환 II

Using stack

```python
formula = '(6+5*(2-8)/2)'
result = ''
stack = []
flag = True

# in-coming priority
def icp(operand):
    if operand in ('*', '/'):
        return 2
    elif operand in ('+', '-'):
        return 1
    elif operand == '(':
        return 3

# in-stack priority
def isp(operand):
    if operand in ('*', '/'):
        return 2
    elif operand in ('+', '-'):
        return 1
    elif operand == '(':
        return 0

for token in formula:
    if token not in ('(', ')', '+', '-', '*', '/'):
        result += token
    else:
        if stack:
            if token == ')':
                while stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
            elif isp(stack[-1]) < icp(token):
                stack.append(token)
            elif isp(stack[-1]) >= icp(token):
                if stack[-1] == '(':
                    stack.pop()
                else:
                    while isp(stack[-1]) > icp(token):
                        result += stack.pop()
                        if stack[-1] == '(':
                            stack.pop()
                            break
                    stack.append(token)
        else:
            stack.append(token)
print(result)
```



### Backtracking

- 해를 찾는 도중에 막히면(즉, 해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법

- 최적화(optimization) 문제와 결정(decision) 문제를 해결

- 절차

    1. 상태 공간 트리의 깊이 우선 검색 실시

    2. 각 노드가 유망한지 점검

    3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속



#### 부분집합의 합 구하기

#### `{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}`의 powerset 중 원소의 합이 10인 부분집합을 구하시오.

```python
def powerset(n, k, s):
    if n == k:
        if s == 10:
            result.append(tmp)
    elif s > 10:
        return # Back-tracking
    else:
        chk[n] = 1
        tmp.append(n)
        powerset(n+1, k, s+arr[n])
        tmp.pop()
        chk[n] = 0
        powerset(n+1, k, s)

arr = list(range(1, 11))
chk = [0 for _ in range(len(arr))]
tmp = list()
result = list()
```

### Quick Sort

Algorithm
```python
def partition(a, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while(a[L] < a[pivot] and L < R): L += 1
        while(a[R] >= a[pivot] and L < R): R -= 1
        if L < R :
            if L == pivot: pivot = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R

def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)
```


## 6. Queue



## 7. List



## 8. Tree