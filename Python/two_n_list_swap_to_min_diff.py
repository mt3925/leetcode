"""数组分割
有两个数组a,b，大小都为n,数组元素的值任意，无序； 要求：通过交换a,b中的元素，使数组a元素的和与数组b元素的和之间的差最小

数组a {1, 20, 30, 40}
数组b {10, 10, 25, 44}


假设数组A[1..2N]所有元素的和是SUM。模仿动态规划解0-1背包问题的策略，令S(k, i)表示前k个元素中任意i个元素的和的集合。显然：
S(k, 1) = {A[i] | 1<= i <= k}
S(k, k) = {A[1]+A[2]+…+A[k]}
S(k, i) = S(k-1, i) U {A[k] + x | x属于S(k-1, i-1) }
"""


def solution(a, b):
    l = a + b
    n = len(l)
    mid = sum(l) // 2
    max_total = 0
    max_choice = []

    def dp(idx, choice, total):
        if idx >= n or total > mid:
            return
        nonlocal max_total, max_choice
        if total > max_total and len(choice) == n // 2:
            max_total = total
            max_choice = choice[:]
            if total == mid:
                return True
        if dp(idx + 1, choice + [idx], total + l[idx]):
            return
        if dp(idx + 1, choice, total):
            return
    dp(0, [], 0)
    la = []
    lb = []
    for idx, i in enumerate(l):
        if idx in max_choice:
            la.append(i)
        else:
            lb.append(i)
    print(max_total, la, lb, sum(la), sum(lb))
    return la, lb


if __name__ == '__main__':
    solution([1, 20, 30, 40], [10, 10, 25, 44])
    solution([4, 7, 7, 13], [5, 5, 9, 10])
