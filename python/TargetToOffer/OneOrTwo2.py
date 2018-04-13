#迭代思路：对数字串从头往后一个一个看，第一个数直接加入结果列表，从第二个数之后，每个数都有两种选择，要么自己单独加入结果列表，要么和结果列表中的前一个数合并
#合并的情况有个条件：结果列表的最后一个数必须只有一位（因为题目要求最多只能两位一起组合）
s = list(input().strip())

def process(s):
    if len(s) < 2:
        return s
    res = [[s[0]]]
    for i in range(1, len(s)):
        tmp = []
        while res:
            cur = res.pop()
            tmp.append(cur + [s[i]])
            if len(cur[-1]) == 1:
                cur[-1] += s[i]
                tmp.append(cur)
        res = tmp
    return res


print(process(s))