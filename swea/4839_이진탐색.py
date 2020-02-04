class Book:
    def __init__(self):
        self.cnt = 0
    
    def binary_search(self, l, r, goal):
        self.cnt += 1
        self.c = int((l+r)/2)
        if self.c > goal:
            self.binary_search(l, self.c, goal)
        elif self.c < goal:
            self.binary_search(self.c, r, goal)
    
    def get_cnt(self):
        return self.cnt

T = int(input())
for t in range(1, T+1):
    p, a, b = map(int, input().split())
    
    book_a = Book()
    book_b = Book()
    book_a.binary_search(1, p, a)
    book_b.binary_search(1, p, b)
    cnt_a = book_a.get_cnt()
    cnt_b = book_b.get_cnt()
    
    if cnt_a < cnt_b:
        result = 'A'
    elif cnt_a > cnt_b:
        result = 'B'
    else:
        result = 0
    print('#{0} {1}'.format(t, result))
