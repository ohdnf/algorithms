import sys
input = lambda: sys.stdin.readline().rstrip()

# sys.stdin = open('in3.txt')

code = list(input())
l = len(code)
# print(code)
words = set()

def decode(code):
    nums = list(code.split(','))
    res = ''
    for num in nums:
        if num.isdigit():
            res += chr(int(num)+64)
    return res

def dfs(lvl, nums):
    if lvl == l:
        # print(nums)
        words.add(decode(nums))
    else:
        last = nums[-1]
        curr = code[lvl]
        if last == ',':
            if curr == '1' or curr == '2':
                dfs(lvl+1, nums+curr)
                dfs(lvl+1, nums+curr+',')
            elif curr == '0':
                return
            else:
                dfs(lvl+1, nums+curr+',')
        elif last == '1' or last == '2':
            if curr == '0':
                dfs(lvl+1, nums+curr+',')
            else:
                dfs(lvl+1, nums+','+curr)
                dfs(lvl+1, nums+curr+',')
        elif last == '0':
            # 확실히 한다면 0 다음에도 0이 오는지 확인해야함
            # 이 문제에서는 그런 경우가 없다고 가정
            dfs(lvl+1, nums+','+curr)
        else:
            if curr == '0':
                return
            dfs(lvl+1, nums+','+curr)

dfs(1, code[0])
words = list(words)
words.sort()
for word in words:
    print(word)
print(len(words))