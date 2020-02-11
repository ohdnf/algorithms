import sys
input = lambda: sys.stdin.readline()

# def hundred(dwarfs):
#     for a in range(3):
#         for b in range(a+1, 4):
#             for c in range(b+1, 5):
#                 for d in range(c+1, 6):
#                     for e in range(d+1, 7):
#                         for f in range(e+1, 8):
#                             for g in range(f+1, 9):
#                                 total = dwarfs[a] + dwarfs[b] + dwarfs[c] + dwarfs[d] + dwarfs[e] + dwarfs[f] + dwarfs[g]
#                                 if total == 100:
#                                     return [dwarfs[a], dwarfs[b], dwarfs[c], dwarfs[d], dwarfs[e], dwarfs[f], dwarfs[g]]

def find(dwarfs):
    nine = len(dwarfs)
    for i in range(nine-1):
        for j in range(i+1, nine):
            tmp = list(dwarfs)
            del tmp[i]
            del tmp[j]
            heights = sum(tmp)
            if heights == 100:
                return tmp

dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

# seven = sorted(hundred(dwarfs))
seven = sorted(find(dwarfs))
for dwarf in seven:
    print(dwarf)