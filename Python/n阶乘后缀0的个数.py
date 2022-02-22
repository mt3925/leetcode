"""
N的阶乘后缀包含连续0的个数
与5相关，5有充足的2相乘得到10
思路1：
    遍历从5到n，递增5的数，对每个数重复整除5，整除的次数即为5的个数，即为后缀0的个数，时间复杂度O(Nk), 5^k <= n 且k最大
思路2：
    遍历从5到n，递增5的x次方，x递增，且依次计算出n=5，25，125...的结果，直到n < 5^k，再计算 n - 5^(k-1) 到 n 的数量，时间复杂度O(k)
"""


def solution(n):
    rst = 1
    for i in range(2, n + 1):
        rst *= i
    cnt = 0
    for i in str(rst)[::-1]:
        if i == '0':
            cnt += 1
        else:
            break
    return cnt


def solution2(n):
    start = 5
    if n < start:
        return 0

    cnt_map = {5: 1}
    cnt_5 = 1
    cnt = 1
    while 1:
        end = start * 5
        if n < end:
            total = n - start
            div = start
            while div >= 5 and total:
                _cnt, total = divmod(total, div)
                cnt += cnt_map[div] * _cnt
                div //= 5
            return cnt

        cnt_5 += 1
        cnt = cnt_map[start] * 5 + 1
        start = end
        cnt_map[start] = cnt


if __name__ == '__main__':
    for i in range(200):
        print(i, solution2(i), solution(i))

    import time
    s = time.time()
    print(10000, solution(100000), time.time() - s)
    s = time.time()
    print(10000, solution2(100000), time.time() - s)
