all_cnt = 0
for q in range(100000000, 200000000):
    n = q
    cnt = 0
    for i in str(n):
        cnt += int(i)
    r = str(bin(cnt)).replace('0b', '')
    cnt = 0
    for i in r:
        cnt += int(i)
    if cnt % 2 == 0:
        r = '1' + r + '00'
    else:
        r = '10' + r + '1'
    if int(r, 2) == 21:
        all_cnt += 1
print(all_cnt)
