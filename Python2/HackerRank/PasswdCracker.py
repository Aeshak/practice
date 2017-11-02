import sys

sys.setrecursionlimit(2000)

def find_password(d, w, cur, mem):
    if w == '':
        return cur
    if w in mem:
        return ''

    if w[0] in d:
        for i in d[w[0]]:
            if w[:len(i)] == i:
                cur_ans = find_password(d, w[len(i):], cur + i + " ", mem)
                if cur_ans != '':
                    return cur_ans

    mem.add(w)
    return ''


t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    l = raw_input().split()
    w = raw_input()
    password_set = set(''.join(l))
    word_set = set(w)
    list_set = set(l)
    if not password_set >= word_set:
        print('WRONG PASSWORD')
        continue

    if word_set <= list_set:
        print(" ".join(list(w)))
        continue

    d = {}
    mem = set()
    for i in l:
        if i[0] in d:
            d[i[0]].append(i)
        else:
            d[i[0]] = [i]

    ans = find_password(d, w, '', mem)
    print("WRONG PASSWORD" if ans == '' else ans)