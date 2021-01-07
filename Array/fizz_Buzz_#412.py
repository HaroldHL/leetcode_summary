class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # 暴力求解
        res = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 ==0:
                res.append("FizzBuzz")
            elif i%3 == 0:
                res.append("Fizz")
            elif i%5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res

        #return ['FizzBuzz' if i%15 == 0 else 'Buzz' if i%5 == 0 else 'Fizz' if i%3 == 0 else str(i) for i in range(1,n+1)]