def removeOuterParentheses(self, S: str) -> str:
        '''
        1. 原语化。2. 拆除各原语最外层括号。
        双指针查找各原语下标
        (()())()
        12121010
        '''
        # 双指针 寻找原语化的最外层括号下表
        primitive_indices = []
        left, count = 0, 0
        for i in range(len(S)):
            if S[i] == "(": count += 1
            elif S[i] == ")": count -= 1
            if count == 0:                        # 找到最外层右括号
                primitive_indices.append((left, i))  # 添加答案
                left = i + 1                         # 更新最外层左括号指针
        # 根据下标，提取原语，切片拆除括号
        return "".join( S[m+1:n] for m, n in primitive_indices )
        

def removeOuterParentheses(self, S):
        res, count = [], 0
        for c in S:
            if c == '(' and count > 0: res.append(c)
            if c == ')' and count > 1: res.append(c)
            count += 1 if c == '(' else -1
        return "".join(res)
