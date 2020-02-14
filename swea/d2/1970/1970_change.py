import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    change = int(input())
    oman, man, ocheon, cheon, obaek, baek, osib, sib = 0, 0, 0, 0, 0, 0, 0, 0
    oman += change // 50000
    change -= 50000 * oman
    man += change // 10000
    change -= 10000 * man
    ocheon += change // 5000
    change -= 5000 * ocheon
    cheon += change // 1000
    change -= 1000 * cheon
    obaek += change // 500
    change -= 500 * obaek
    baek += change // 100
    change -= 100 * baek
    osib += change // 50
    change -= 50 * osib
    sib += change // 10
    change -= 10 * sib
    print('#{0}'.format(test_case))
    print(oman, man, ocheon, cheon, obaek, baek, osib, sib)